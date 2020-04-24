# Chika's Script
A simple anime downloader built with Python.

## How it works

Basically, the core consists in an automated process to open the anime URL with Selenium and perform the download with youtube-dl API.

## Features

NOTE: Currently, animeshouse.net is the only supported URL.

NOTE: If your OS is Windows, the program may not display some special characters on your cmd or powershell. To fix that, open it on Windows Terminal (Preview), which can be downloaded from Microsoft Store.

Use Chika's Script to:

* Download your favorite animes from your terminal
* Keep track of downloaded episodes with the History

## Getting Started
* Clone or download the project

* Install requirements.txt using the following command:
    ```
    pip install -r requirements.txt
    ```
* Execute main.py from inside the project directory:
    ```
    python main.py
    ```

![Alt Text](https://i.imgur.com/gOrns9k.gif)

### How to use
First of all, you must define your username and path to save the files at settings.json inside of data folder:
    ```
    {
        "username": "Your Name",
        "path_to_save": "C:/Users/your-user/Desktop/"
    }
    ```
    
NOTE: Currently you have to do this manually using a text editor.

After that, you can start the program and add an URL from an anime. The steps are:

* Enter 2 as option to add a new anime
* Type just ONE WORD for the name
* Type the URL from animeshouse.net and replace the episode number by "()"

![Alt Text](https://i.imgur.com/3wWYH0R.gif)

Now you can download any episode of that anime calling it by the name and episode:

* Enter 1 as option to perform download
* Type the anime name and episode, separated by one common space (e.g: kaguya 2)

NOTE: The loading process (before the download start) depends on your internet speed, but it usually does not take more than 30sec.
If you close the program, the download will be stopped and you will have to start it again.

![Alt Text](https://i.imgur.com/5LFUBxI.gif)

Finally, you can check the download history by typing 3 in the menu:

![Alt Text](https://i.imgur.com/Wn57V0b.png)

## Next Steps

If you have any suggestions or want to contribute, feel free to open a PR or contact me!

The future plans include:

- [ ] Improve UI
- [ ] Support other anime websites
- [ ] Add option to change language to Portuguese
- [ ] Add option to change username and path to save
- [ ] Improve core routine and add proper exceptions
- [ ] Support download multiple episodes/animes together
- [ ] Integrate with MAL to set downloaded episodes as "watched"
