# SpamU-for-Windows

SpamU-for-Windows is windows version of [SpamU](https://github.com/Spectrewolf8/SpamU) with the ability to spam any text field. SpamU has ability to spam 500 messages in 105 seconds.

![image](https://user-images.githubusercontent.com/69973760/219849733-530041dd-d123-40f5-8cea-ffa9103ed2f8.png)


###


## Usage
Your text to spam goes in [Text to Spam] text box.

Moreover, You can decide the delay before starting spam(activates after [Star Spam!] button is pressed), number of messages to spam and delay between each text spammed. **Safe Mode is not available for windows version of SpamU**. You can press **ALT + ENTER** after the start of spam to stop spamming further.

Default values are used when any parameter text field is left empty.

**It is recommended that you have target window and SpamU window in view as you start Spam** 


![image](https://user-images.githubusercontent.com/69973760/219851445-af573675-f0f8-4ea4-b899-c824752aa1e7.png)


###


## SpamU executable Application
Appliction files lie inside [App directory](https://github.com/Spectrewolf8/SpamU-for-Windows/blob/master/App).

Path to intended executable is ```SpamU-for-Windows/App/dist/SpamU/SpamU.exe```
###


## Required Packages/Modules
Required packages are as:

- tkinter
- customtkinter
- time
- pyautogui
- pyperclip
- keyboard
- pyinstaller (to build .exe file from python files) [optional]

Required packages can be accquired by using this command:
```
pip install tkinter customtkinter time pyautogui pyperclip keyboard pyinstaller
```
###


### Pyinstaller Cmd to build .exe file from python files

You need to do ```ALT + F + S + A```  in the directory which has ``SpamUGUI.py``,``Spammer.py``,and ``swaggy-trollface-man.ico`` to open privilaged powershell terminal in that directory and then paste your version of cmd/script which is as follows:

```
 pyinstaller --noconfirm --onedir --windowed --icon "{directory}/swaggy-trollface-man.ico" --add-data "{directory}Spammer.py;." --add-data "C:/Users/{your username}/AppData/Local/Programs/Python/Python311/Lib/site-packages/customtkinter;customtkinter/" --add-data "{directory}/swaggy-trollface-man.ico;."  "{directory}/SpamUGUI.py"

 # replace {directory} and {your username} with your own directory where the files are kept, and your own username
```
###


### SpamU for Linux
SpamU for linux can be found [here](https://github.com/Spectrewolf8/SpamU)
