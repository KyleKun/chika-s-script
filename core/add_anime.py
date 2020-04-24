import os
import json
from time import sleep


class AddAnime:
    def start(self, root_dir):

        self.show_instructions()

        # If the input is zero, go back to menu
        name = input('Anime: ')
        if name == '0':
            return

        url = input('URL: ')

        if self.add_new_url(name, url, root_dir):
            print('Saved successfully!')
        else:
            print("Failed to save :(")
        sleep(3)
        return

    @staticmethod
    def add_new_url(name, url, root_path):
        """
        Creates a new anime/url in urls.json based on user input

        :param name: Key, the word called to download the anime

        :param url: Value, the URL with () in the episode number's place

        :param root_path: root directory

        :return: None
        """
        new_url = {name: url}
        try:
            with open(os.path.join(root_path, 'data\\urls.json'), 'r+', encoding='utf-8') as urls:
                data = json.load(urls)
                data["urls"].append(new_url)
                urls.seek(0)
                urls.truncate(0)
                json.dump(data, urls, ensure_ascii=False, indent=4)
            return True
        except Exception as e:
            print("Error parsing JSON urls file: ", e)
            return False
        finally:
            urls.close()

    @staticmethod
    def show_instructions():
        # TODO make it FANCY
        print('\nInstructions:')
        print('- Type only one word for the anime name, this is how you will call it when you want to download an episode;\n')
        print('- Paste the URL replacing the episode number by "()". Example: https://animeshouse.net/episodio/baka-episodio-()-legendado-hd/\n')
        print('NOTE: Currently, it only works with animeshouse.net website.\n')
        print('Enter "0" to go back to menu.\n')
