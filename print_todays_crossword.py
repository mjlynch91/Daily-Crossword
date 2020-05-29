# -*- coding: utf-8 -*-
"""
Created on Fri May 29 14:45:39 2020

@author: mjlyn
"""

import os
from datetime import datetime

today=datetime.today().strftime('%d-%m-%Y')
month=datetime.now().strftime("%B")
path="C:/Users/mjlyn/Documents/Marias_Crosswords"
crossword_url="http://puzzles.freedailycrosswords.com/" + month + "/old/" + today + ".pdf"
file=wget.download(url=crossword_url,out=path)