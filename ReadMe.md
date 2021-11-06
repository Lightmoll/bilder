# Bilder
Bilder *pron: builder* is a cross-platform screenshot utility, orginally intendet for saving live lecture screenshots conviniently via an easy to use keybind. Though I guess it can really be used for anything. It supports multiple monitors. Take screenshots of all, or just one. Will automatically switch monitors, if selected one is disconnected.

## Features
 - multi-monitor support
 - cross-platform (linux + win)
 - wacky key combinations
 - auto detect existing folders

## Installation
1. Download the git repository
2. *Install python3 if not preinstalled*
2. Install dependecies via `pip3 install -r requirements.txt`
3. Create `pics/` folder in script folder

## Usage
1. Run Script with `python3 bilder.py`
2. Enter Lecture name, or any other name. *Will be grouped in folders*
3. Enter Monitor *(will only show up, if multiple monitors were detected)*
4. Press `L + CTRL_R` or `L + ALT_R`. Note: You have to press the `L` key first! °

° don't ask me why. It's a "feature".

## FAQ

### Can you change the keybindings?
Yes, if you edit the python file. Simply change the `COMBINATIONS` list, to whatever you desire.

### HELP! I get an Error
Try to delete the entire folder, and carefully follow the installation steps. If the error still persits open an Issue, stating your problem, platform, and Error/Traceback as clearly as possible.

### Dependency installation fails under Windows
Try using `py -m pip` instead of `pip3`.

### Why such strange combination?
Because none of my applications have default keybinds for that specifc combination.

### Will there be updates?
If you find breaking bugs which I can replicate, I will try to push new updates to solve them. But probably not more features.

### Can I add a pull-requst?
I won't stop you.