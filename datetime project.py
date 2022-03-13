
# ######Choose a format you’d like to use for the date
# Input the date in that format as a string
# Convert the string to a datetime.datetime object using strptime()
# Either use the weekday() or isoweekday() methods
# to get the day of the week, or use strftime() to get the name of the weekday straight away


d=str(input("Enter your birthdate in-->>\n \033[0;31;47m   dd/mm/yyyy format \033[2;41;40m \nNOTE THE FORMAT IS IMPORTANT"))
from time import sleep
import sys
li=f"COOL!!! {d} is your birthdate!!!!!"
for x in li:
    print(x, end='')
    sys.stdout.flush()
    sleep(0.1)
import datetime
dw=datetime.datetime.strptime(d, "%d/%m/%Y")
#print(f"\n{dw.isoweekday()}")
dw.weekday()
r=dw.strftime("\n The day on your Birthday was %A ")
for x in r:
    print(x, end='')
    sys.stdout.flush()
    sleep(0.1)
print(r)
