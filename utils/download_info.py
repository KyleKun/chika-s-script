from time import sleep
from termcolor import colored
from datetime import datetime


class DownloadInfo:
    @staticmethod
    def current_day():
        return datetime.today().strftime('%Y-%m-%d')

    @staticmethod
    def calc_time(start, end):
        total_time = end - start
        final_time = str(int(total_time / 60))
        return f'{final_time}min'

    @staticmethod
    def download_progress_bar(d):
        estimated_size = str(int((d["total_bytes"] / 1000000)))
        if d['status'] == 'finished':
            print(colored('\nDownload completed!', 'green'))
            sleep(3)
            return
        if d['status'] == 'downloading':
            message = f' Completed:{d["_percent_str"]} | ' \
                      f'Time remaining: {d["_eta_str"]} | ' \
                      f'Size: ~{estimated_size}Mb      '
            print(colored(message, 'white', 'on_blue'), end="\r", flush=True)
