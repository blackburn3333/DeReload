# Author: Jayendra Matarage
# Title: DeRefresh
# Date : 17, June, 2019

import webbrowser, os
from pynput import keyboard

KEY_COMBINATION = [
    {keyboard.Key.ctrl, keyboard.KeyCode(char='S')},
    {keyboard.Key.ctrl, keyboard.KeyCode(char='s')},
]

current = set()
selectedFile = ""
browser = "chrome"


def main():
    print(
        "-------------------------------------------------------------------------------------------------------------------")
    print("######### ######### ######### ######### ######### ######### ######### ######### ##     ##")
    print("   ##  ## ##        ##      # ##        ##        ##      # ##        ##        ##     ##")
    print("   ##  ## ######    ######### ######    ######    ######### ######    ######### #########")
    print("   ##  ## ##        ##   ##   ##        ##        ##   ##   ##               ## ##     ##")
    print("######### ######### ##     ## ######### ##        ##     ## ######### ######### ##     ##")
    print(
        "-------------------------------------------------------------------------------------------------------------------")


def open_website():
    try:
        select_browser = webbrowser.get(browser)
        select_browser.open('file://' + os.path.realpath(selectedFile), new=0)
    except:
        default = webbrowser.get('windows-default')
        default.open('file://' + os.path.realpath(selectedFile), new=0, autoraise=False)


def reload_page():
    open_website()
    print("Refreshing -> " + selectedFile)


def on_press(key):
    if any([key in COMBO for COMBO in KEY_COMBINATION]):
        current.add(key)


def on_release(key):
    if any([key in COMBO for COMBO in KEY_COMBINATION]):
        reload_page()
        current.remove(key)


def key_listener():
    open_website()
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


def key_get_file():
    filename = input("Enter filename that want to refresh with extension (Eg : filename.html): ")
    changeFile = os.path.isfile(filename)
    while True:
        if changeFile:
            print("Ctrl + S trigger on " + filename)
            global selectedFile
            selectedFile = filename
            key_listener()
            break
        else:
            print("File not found")
            filename = input("Enter filename that want to refresh with extension (Eg : filename.html): ")
            changeFile = os.path.isfile(filename)


if __name__ == '__main__':
    main()
    key_get_file()
