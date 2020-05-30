# -*- coding: utf-8 -*-
"""
Created on Fri May 29 14:45:39 2020

@author: mjlyn
"""

import os
import schedule
import time
import wget

def job():
    today=time.strftime('%d-%m-%Y')
    month=time.strftime("%b")
    path="C:/Users/mjlyn/Documents/Marias_Crosswords"
    #an example of daily crossword url is http://puzzles.freedailycrosswords.com/April/old/20-04-2020.pdf
    crossword_url="http://puzzles.freedailycrosswords.com/" + month + "/old/" + today + ".pdf"
    file=wget.download(url=crossword_url,out=path)
    print("Today's crossword was successfully printed!")
    os.startfile(file,"print")
    
schedule.every().day.at("8:00").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)
