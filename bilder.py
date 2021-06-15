"""

Created by: lightmoll
Created on: ? 03.2020
Version: 1.0.3
Last Edit: 04.2021

This tool is used to automatically take screenshots for various tasks.
You can take a screenshot with CTRL + L, ALT + L

Future Features:
 + automatically detect if name already exists. give warning. append pictures
 + detect if multiscreen changes to single screen. give warning. take pics of
     main monitor. if afterwards mulitscreen take screens of secondary mon.

"""

import os
from os import path
from pynput import keyboard

import mss as mssgen
try:
    from mss.windows import MSS as mss
except Exception:
    from mss.linux import MSS as mss


# The key combination to check
COMBINATIONS = [
    {keyboard.Key.ctrl_r, keyboard.KeyCode(char='l')},
    {keyboard.Key.alt_r, keyboard.KeyCode(char='l')}
]


## CONSTANTS & GLOBAL VARS
pic_id = 0
BASE_FOLDER = "pics/"
name = "VL_"
selected_monitor = 0
last_monitor_count = 1


## UTIL FUNCTIONS
def is_mulitscreen(max_selected_monitor=2):
    with mss() as sct:
        return len(sct.monitors) > max_selected_monitor


def num_monitors():
    with mss() as sct:
        return len(sct.monitors)-1

## MAIN FUNCTIONS
def take_screenshot(folder, file, monitor=0):
    global last_monitor_count

    if monitor != 0 and not is_mulitscreen(max_selected_monitor = monitor):
        print("[WARNING] Can't identify selected monitor! Using primary one instead")
        monitor  = 1

    if last_monitor_count < num_monitors():
        print("[WARNING] New monitor after init detected")
        last_monitor_count = num_monitors()

    with mss() as sct:
        file_name = os.path.join(folder, file) + ".png"

        # Grab the data
        sct_img = sct.grab(sct.monitors[monitor])

        # Save to the picture file
        mssgen.tools.to_png(sct_img.rgb, sct_img.size, output=file_name)


# The currently active modifiers
current = set()

def execute():
    global pic_id
    global name
    global selected_monitor

    print(f"Taking Screenshot {pic_id}")
    file_name = name + "_" + str(pic_id)
    picture_path = path.join(BASE_FOLDER , name)
    pic_id += 1

    take_screenshot(picture_path, file_name, selected_monitor)


def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute()


def on_release(key):
    try:
        if any([key in COMBO for COMBO in COMBINATIONS]):
            current.remove(key)
    except KeyError:
        print("KeyError")


def test_if_name_exists():
    """
    This funciton checks if the entered name already exists.
    Prints out a warning to the users.
    Sets the global pic_id var to the next available number!
    """

    global pic_id
    global name
    picture_path = path.join(BASE_FOLDER, name)

    if not os.path.isdir(picture_path):
        os.makedirs(picture_path)

    files = [f for f in os.listdir(picture_path) if path.isfile(path.join(picture_path, f))]

    curr_max_id = -1

    for file in files:
        if name == file[:len(name)]:
            curr_id = int(file.split("_")[-1].split(".")[0]) #TODO: BAD DETECTION use regex instead
            if curr_id > curr_max_id:
                curr_max_id = curr_id

    if curr_max_id > -1:
        print("[WARNING] Name already exists")
        print(f"[WARNING] Starting with id: {curr_max_id + 1}")
        pic_id = curr_max_id + 1


if __name__ == "__main__":
    print("Starting Screenshot Utility")
    print("---------------------------\n")
    name = input("Lecture Name\n+ ")

    #remove all trailing _ if they exitst.
    while name[-1] == "_":
        name = name[:-1]

    test_if_name_exists()
    if is_mulitscreen():
        mon_str = input("Which Monitor? [0] (1 = Primary, 2 = Secondary)\n+ ")
        last_monitor_count = num_monitors()
        if mon_str != "":
            selected_monitor = int(mon_str)
        print(f"Taking Full Screenshots of Monitor {selected_monitor}")


    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


