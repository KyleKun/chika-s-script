import os
import json
import youtube_dl
from time import time
from pathlib import Path
from threading import Thread
from datetime import datetime
from selenium import webdriver
from core.history import History
from core.loading_thread import Loading
from utils.download_info import DownloadInfo
from utils.utils import MyLogger, LoaderCondition


class Download(Thread):
    # Constants
    THIS_PATH = os.path.dirname(os.path.abspath(__file__))

    def __init__(self):
        Thread.__init__(self)

        # Root dir
        self.root_dir = Path(self.THIS_PATH).parent

        # Condition for loading thread
        self.loader = LoaderCondition()

        # Reading path to save from config file
        with open(os.path.join(self.root_dir, 'data\\settings.json')) as settings:
            self.path_to_save = json.load(settings)["path_to_save"]
            if self.path_to_save == '':
                self.path_to_save = os.path.join(self.root_dir, 'downloads')
        settings.close()

        # Name of the video to be downloaded - e.g.: kaguya_ep2.mp4
        self.file_name = ''

        # Selenium config
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('headless')
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=self.options)

        # User config options
        self.add_url = ''

    def set_url_episode(self, anime: str, episode: str):
        """
        Set the URL to the proper format, seeking for it at urls.json and replacing the episode number

        :param anime: Name of the anime which is the key at urls.json

        :param episode: The number of episode to be downloaded

        :return: The URL ready to be used by selenium
        """
        with open(os.path.join(self.root_dir, 'data\\urls.json')) as urls:
            _url = json.load(urls)
            for index, link in enumerate(_url['urls']):
                try:
                    if link[anime]:
                        final_index = index
                        break
                except KeyError:
                    continue
            final_url = _url['urls'][final_index][anime]
        urls.close()
        if len(episode) == 1:
            return final_url.replace('(', episode).replace(')', "")
        return final_url.replace('(', episode[0]).replace(')', episode[1])

    def run(self):
        # User input
        to_download = input("Anime/episode -> ")

        # User input properly divided
        # TODO this in a function with option to multiple episodes and animes
        anime = to_download.split()[0]
        episode = to_download.split()[1]

        # Setting the file name
        self.file_name = anime+'_ep'+episode+'.mp4'

        # Starting loading thread
        loading_thread = Loading()
        loading_thread.start()

        try:
            # GET request
            self.driver.get(self.set_url_episode(anime, episode))

            # Finding and switching context to the iframe holding the video
            frame = self.driver.find_element_by_css_selector('div.pframe iframe')
            self.driver.switch_to.frame(frame)

            # Getting video URL
            video = self.driver.find_element_by_tag_name('video').get_attribute('src')

            # Close selenium
            self.driver.close()

            # Finish loading thread
            LoaderCondition.loaded = True

            # Set complete path of file
            complete_path = os.path.join(self.path_to_save, self.file_name)

            # Setting youtube-dl options
            ydl_opts = {'outtmpl': complete_path, 'quiet': True,
                        'logger': MyLogger(), 'progress_hooks': [DownloadInfo.download_progress_bar]}

            # Get start time
            start = time()
            today = datetime.now()
            hour = str(today.hour)
            minute = str(today.minute) if len(str(today.minute)) > 1 else '0'+str(today.minute)

            # Performing the download
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                # TODO the possibility to download more than one episode
                print(f'Downloading {anime} episode {episode} to {self.path_to_save}')
                ydl.download([video])

                # Prepare to add to history
                end = time()
                total_time = DownloadInfo.calc_time(start, end)
                size = str(int(os.path.getsize(complete_path) / 1000000))

                new_item = {DownloadInfo.current_day(): {"anime": anime,
                                                         "episode": episode,
                                                         "start-hour": f"{hour}:{minute}",
                                                         "file-size": f"~{size}Mb",
                                                         "took:": total_time}}

                # Add the current download to history
                History.add_to_history(new_item, self.root_dir)
            return

        except Exception as e:
            print('\nError: ', e)
