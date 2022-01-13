import PySimpleGUI as sg
import time
mylist = [1,2,3,4,5,6,7,8]
for i, item in enumerate(mylist):
 sg.one_line_progress_meter('This is my progress meter!', i+1, len(mylist), '-key-')
 time.sleep(1)