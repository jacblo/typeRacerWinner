#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 11:56:45 2020

@author: y3
"""

import time
import random
from screenshotAndKeypressTests import *
import cv2
import pytesseract


vals = {"waitBeforeStart":2,"char":[0.01,0.05],"word":[0.05,0.05],"mistake":{"chance":10,"mistakeChar":b"g","timeToBackspace":[0.01,0.1],"timeToNextChar":[0.01,0.1]}}
def beat(vals,text):
    
    input("Start?")
    print(vals["waitBeforeStart"]," seconds")
    #keypress(b"mousemove 144 624\nmouseclick 1")
    time.sleep(vals["waitBeforeStart"])
    print("starting")
    for x in text:
        if random.randint(0,vals["mistake"]["chance"]) == 0:
            keypress(b"str "+vals["mistake"]["mistakeChar"]+b" ")
            time.sleep(random.uniform(vals["mistake"]["timeToBackspace"][0],vals["mistake"]["timeToBackspace"][1]))
            keypress(b"key BackSpace ")
            time.sleep(random.uniform(vals["mistake"]["timeToNextChar"][0],vals["mistake"]["timeToNextChar"][1]))
        keypress(bytes("str "+x+" ","utf-8"))
        if x == " ":
            time.sleep(random.uniform(vals["word"][0],vals["word"][1]))
        time.sleep(random.uniform(vals["char"][0],vals["char"][1]))


beat(vals, input("text: "))

if input("test? (y/n) ").lower() == "y":
    time.sleep(1)
    img = pyscreenshot.grab(bbox=(768,398,1181,534))
    text = pytesseract.image_to_string(img)
    beat(vals,text[:100])
    
