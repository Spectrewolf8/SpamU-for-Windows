import os
import time
from tkinter import END

import pyautogui as pt
from pyperclip import copy as copyToClipboard


class Spammer:
    def __init__(self, numberOfTextsToSend, delayTimeBetweenEachTextSent):
        self.numberOfTextsToSend = numberOfTextsToSend
        self.breakOperation = False
        self.delayTimeBetweenEachTextSent = delayTimeBetweenEachTextSent

    def breakOperationCall(self):
        self.breakOperation = True

    def startOperation(self, message, statusBox, win, spamProgressBar):

        spamProgressBar.set(0)  # reset progress bar if spam is ran again
        copyToClipboard((str(message)).strip())
        initialTime = time.time()
        i = 1
        while i <= self.numberOfTextsToSend:
            if self.breakOperation:
                break
            pt.hotkey('ctrl', 'v')  # pasting the message to spam
            pt.press("enter")  # pressing enter to send the message to spam
            spamProgressBar.set(((i / self.numberOfTextsToSend) * 100) / 100)  # setting progress bar progress
            statusBox.delete("0.0", END)  # clearing status bar
            statusBox.insert("0.0", "spammed " + str(i) + "th message")  # printing a new message in status bar
            win.update()
            time.sleep(self.delayTimeBetweenEachTextSent)
            i += 1
            finalTime = time.time()

        print()
        statusBox.delete("0.0", END)
        statusBox.insert("0.0", "spammed " + str(i) + " messages in " + str(round(finalTime - initialTime)) + "s")
        win.update()
