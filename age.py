#!/usr/bin/python3

import datetime


nm=input("Please enter your name:")
age=int(input("Enter your age as per this year"))

current=datetime.datetime.now().year


final=current+95-age

print("Ans is ",final)


