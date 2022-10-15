# importing easygui module
from easygui import *
import os

# user define function
def shutdown():
    return os.system("shutdown /s /t 1")
choices = ["Yes", "No"]

msg = "Did you drink water? Select any one option: PLEASE NOTE THAT IF YOU LIE, IT IS YOUR DOWNFALL"

reply = choicebox(msg, choices=choices)
if(reply=="No"):
    shutdown()

