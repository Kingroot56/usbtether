# -*- coding: utf-8 -*-
import os
def command(deger):
    if deger == 1:
        print ("Android 4.x.x")
        return os.system("adb shell su -c service call connectivity 34 i32 1")
        print ("\a")
    if deger == 2:
        print ("Android 5.x.x")
        return os.system("adb shell su -c service call connectivity 30 i32 1")
        print ("\a")
    if deger == 3:
        print ("Android 6.x.x")
        return os.system("adb shell su -c service call connectivity 30 i32 1")
        print ("\a")
    if deger == 4:
        print ("Android 7.x.x")
        return os.system("adb shell su -c service call connectivity 33 i32 1")
        print ("\a")
    if deger == 5:
        print("ADB KİLLED")
        return os.system("adb kill-server")
        print ("\a")
    if deger == 6:
        print ("driver kuruluyor...")
        return os.system("fast_install.exe")
        print ("\a")
        print ("driver kurululdu...")
    if deger == 7:
        exit()
