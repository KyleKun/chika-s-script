import os
import sys
import json
import subprocess as sp
from colorama import init
from termcolor import colored
from core.history import History
from core.download import Download
from core.add_anime import AddAnime
from utils.ascii_art import MenuArt


def main():
    # Init Colorama
    init(strip=not sys.stdout.isatty())

    # Constants
    root_dir = os.path.dirname(os.path.abspath(__file__))
    title = "Chika's Script\nv0.1"

    # Set routines
    add_anime = AddAnime()
    download = Download()
    history = History()

    # Grab ASCII Art to display
    chika = MenuArt().chika

    # Get username
    try:
        with open(os.path.join(root_dir, 'data\\settings.json'), 'r', encoding='utf-8') as settings:
            data = json.load(settings)
            username = ', '+data["username"] if data["username"] != '' else ''

    except Exception as e:
        username = ''
        print("Error parsing JSON settings file: ", e)

    exit_script = False
    while not exit_script:

        # Clear the screen
        sp.call('cls', shell=True)

        # Show main menu
        print(title)
        print(colored(chika, "cyan"))
        print('\t\t\t\tOptions:', end="")
        print(colored(' 1) Download ', 'magenta'), end="")
        print('⡇', end="")
        print(colored(' 2) Add new anime ', 'green'), end="")
        print('⡇', end="")
        print(colored(' 3) History ', 'yellow'), end="")
        print('⡇', end="")
        print(colored(' 0) Exit ', 'red'))

        # Run routines
        try:
            opt = int(input(f'Welcome{username}!\nPlease, select an option: '))

            if opt == 1:
                download.start()
                download.join()
            elif opt == 2:
                add_anime.start(root_dir)
            elif opt == 3:
                history.display_history(root_dir)
            elif opt == 0:
                print('See ya ;)')
                exit_script = True
            else:
                print('This is not a valid option!')

        except Exception as e:
            print('Error: ', e)


if __name__ == '__main__':
    main()
