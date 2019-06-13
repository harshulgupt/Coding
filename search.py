#!/usr/bin/python3
import time
from googlesearch import search

web=input("KIndly enter search query")

url=[]
for i in search(web,stop=10):
	print(i)
	
	url.append(i)
print(url)

