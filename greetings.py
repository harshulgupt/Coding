import datetime
print("Kindly enter your name")
nm=input()
present=datetime.datetime.now()

if present.hour>=4 and present.hour<12     :
   print("Good Morning",nm)
elif present.hour>1 and present.hour<4    :
   print("Good Night...",nm)
elif present.hour>=12 and present.hour<17 :
   print("Good Afternoon",nm)
elif present.hour>=17 and present.hour<23 :
   print("Good Night...",nm)

