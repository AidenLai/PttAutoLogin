# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 04:00:33 2019

@author: minto
"""

from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import os

def job():
    os.system("AutoPtt.py")

scheduler=BlockingScheduler()
scheduler.add_job(job, 'cron', day_of_week='0-6',hour=00,minute=1)
scheduler.start()