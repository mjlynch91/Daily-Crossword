# -*- coding: utf-8 -*-
"""
Created on Fri May 29 14:45:39 2020

@author: mjlyn
"""

import os
from datetime import datetime
import schedule
import time

def job():

    print("Test Successful!")
    
schedule.every(60).seconds.do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)
