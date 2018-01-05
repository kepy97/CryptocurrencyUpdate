# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 10:44:43 2018

@author: admin
"""

from win10toast import ToastNotifier
toaster = ToastNotifier()
from datetime import datetime

a = 1
while(True):
	print("Done", +a)
	print(datetime.now())
	toaster.show_toast("---------------Reminder---------------", "Python is awsm by default! Drink Water Please", duration = 1800)
	a = a + 1