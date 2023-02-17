from tkinter import ttk, END, PhotoImage
import customtkinter
import time

import keyboard
from Spammer import Spammer

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

win = customtkinter.CTk()
win.geometry("620x550")
win.title("SpamU")
photo = PhotoImage(file="swaggy-trollface-man.png")
win.iconphoto(False, photo)

# main frame
frame_1 = customtkinter.CTkFrame(master=win)
frame_1.pack(pady=15, padx=60, fill="both", expand=True)

# Text to spam text box
spamTextBox = customtkinter.CTkTextbox(master=frame_1, width=200, height=70)
spamTextBox.place(x=80, y=50)
spamTextBox.insert("0.0", "Your Text Comes Here!")
# Text to spam text box label
spamTextBoxLabel = customtkinter.CTkLabel(master=frame_1, text="Text to Spam:",
                                          font=customtkinter.CTkFont(size=14, weight="bold"),
                                          justify=customtkinter.CENTER)
spamTextBoxLabel.place(x=80, y=20)

# Status Text Box
statusTextBox = customtkinter.CTkTextbox(master=frame_1, width=300, height=30)
statusTextBox.place(x=80, y=460)
statusTextBox.insert("0.0", "Operation status comes here\n")
# Status label
statusLabel = customtkinter.CTkLabel(master=frame_1, text="Status:",
                                     font=customtkinter.CTkFont(size=14, weight="bold"),
                                     justify=customtkinter.CENTER)
statusLabel.place(x=80, y=430)

# spam parameters
# Wait till start entry box
waitTimeTillStartingSpamEntryBox = customtkinter.CTkEntry(master=frame_1, width=100, placeholder_text="(Seconds)")
waitTimeTillStartingSpamEntryBox.place(x=170, y=140)
# Wait till start entry box label
waitTimeTillStartingSpamEntryBoxLabel = customtkinter.CTkLabel(master=frame_1, text="Delay before\nStart:",
                                                               font=customtkinter.CTkFont(size=13, weight="normal"),
                                                               justify=customtkinter.LEFT)
waitTimeTillStartingSpamEntryBoxLabel.place(x=80, y=140)

# number of texts to spam entry box
numberOfTextsToSendEntryBox = customtkinter.CTkEntry(master=frame_1, width=100, placeholder_text="(number)")
numberOfTextsToSendEntryBox.place(x=170, y=180)
# number of texts to spam entry box label
numberOfTextsToSendEntryBoxLabel = customtkinter.CTkLabel(master=frame_1, text="Number of\ntexts to spam:",
                                                          font=customtkinter.CTkFont(size=13, weight="normal"),
                                                          justify=customtkinter.LEFT)
numberOfTextsToSendEntryBoxLabel.place(x=80, y=180)

# delay time between each text sent entry box
delayTimeBetweenEachTextSentEntryBox = customtkinter.CTkEntry(master=frame_1, width=100, placeholder_text="(Seconds)")
delayTimeBetweenEachTextSentEntryBox.place(x=170, y=220)
# delay time between each text sent entry box label
delayTimeBetweenEachTextSentEntryBoxLabel = customtkinter.CTkLabel(master=frame_1, text="Delay between\neach text:",
                                                                   font=customtkinter.CTkFont(size=13, weight="normal"),
                                                                   justify=customtkinter.LEFT)
delayTimeBetweenEachTextSentEntryBoxLabel.place(x=80, y=220)

# hint
# delay time between each text sent entry box hint label
delayTimeBetweenEachTextSentEntryBoxLabel = customtkinter.CTkLabel(master=frame_1,
                                                                   text="🔰 Delay between each\ntext can be in decimal",
                                                                   font=customtkinter.CTkFont(size=10, weight="normal"),
                                                                   justify=customtkinter.CENTER)
delayTimeBetweenEachTextSentEntryBoxLabel.place(x=170, y=250)

# spam progress bar
spamProgressBar = customtkinter.CTkProgressBar(master=frame_1, width=180)
spamProgressBar.place(x=80, y=400)
spamProgressBar.set(0)

# spam progress bar label
spamProgressBarLabel = customtkinter.CTkLabel(master=frame_1, text="Progress:",
                                              font=customtkinter.CTkFont(size=12, weight="bold"),
                                              justify=customtkinter.LEFT)
spamProgressBarLabel.place(x=80, y=370)

##########################

# start spamming button callback
def startSpammingButton_callback():
    waitTimeTillStartingSpamTime = waitTimeTillStartingSpamEntryBox.get()
    numberOfTextsToSendNumber = numberOfTextsToSendEntryBox.get()
    delayTimeBetweenEachTextSentTime = delayTimeBetweenEachTextSentEntryBox.get()
    if waitTimeTillStartingSpamTime == '':
        waitTimeTillStartingSpamTime = '15'
    if numberOfTextsToSendNumber == '':
        numberOfTextsToSendNumber = '50'
    if delayTimeBetweenEachTextSentTime == '':
        delayTimeBetweenEachTextSentTime = '1'

    countdown(int(waitTimeTillStartingSpamTime))  # delay countdown before stating spam

    spammer = Spammer(int(numberOfTextsToSendNumber), float(delayTimeBetweenEachTextSentTime))  # creating spammer
    # Create a Label and a Button widget
    pressEnterToExitLabel = ttk.Label(win, text="Press {ALT + ENTER} to Stop operation", font='Century 16 bold')
    pressEnterToExitLabel.pack(ipadx=10)
    # Disable the Mouse Pointer
    win.config(cursor="none")
    win.update()
    # press ctrl+shift+z to print "Hotkey Detected"
    keyboard.add_hotkey('alt + enter', exitOnEnter_callback, args=(pressEnterToExitLabel, spammer))

    # keyboard.wait('shift + enter')
    spammer.startOperation(spamTextBox.get("1.0", END), statusTextBox, win, spamProgressBar)
    exitOnEnter_callback(None, spammer)


# define the countdown func.
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        time.sleep(1)
        t -= 1
        statusTextBox.delete("0.0", END)
        statusTextBox.insert("0.0", "Stating operation in: " + str(timer))
        win.update()


def exitOnEnter_callback(label, spamObject):
    win.geometry("620x550")
    win.resizable(True, True)
    win.config(cursor="arrow")
    spamObject.breakOperationCall()
    if label is not None:
        label.destroy()
    win.update()


# start spamming button
startSpammingButton = customtkinter.CTkButton(master=frame_1, command=startSpammingButton_callback,
                                              text="Start Spam!",
                                              font=customtkinter.CTkFont(size=14, weight="normal"))
startSpammingButton.place(x=100, y=330)

# guide label
guideLabel = customtkinter.CTkLabel(master=frame_1,
                                    text="Defaults:\n  delayBeforeStart - 15s\n  numberOfTextsToSpam - "
                                         "50\n  delayBetweenEachText - 1s\n\n\n\n\n\n⚠ Safe mode: disables "
                                         "interactions till "
                                         "operation completion and lets you break operation midway ("
                                         "RECOMMENDED)\n\n⚠ Warning:\nImmediately select the desired text field to SPAM"
                                         " right after "
                                         "pressing start button",
                                    font=customtkinter.CTkFont(size=12, weight="normal"), text_color="yellow",
                                    justify=customtkinter.LEFT, wraplength=165)
guideLabel.place(x=320, y=140)

win.mainloop()
