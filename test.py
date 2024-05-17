import webbrowser
from pyautogui import hotkey, write, hold, press
import time

def form_entry():
    # Regular pyautogui commands
    hotkey('shift', 'esc')
    write("```")
    hotkey('command', 'v')
    write("```")
    with hold('shift'):
        press(['enter'])

def main():

    webbrowser.open("https://chatgpt.com", new=0)

    # Edit this to your liking
    time.sleep(1.5)

    form_entry()

if __name__ == "__main__":
    main()
