#Exist 3 types of modules 

#1. Own Modules 
import fmath
fmath.add(4,4)
fmath.sub(10,5)



#2. thyrdy party modules 

#3. python modules
import datetime

print(datetime.date.today())
print(datetime.timedelta(minutes=100))
#tambien se puede importar solo la propiedad que se desea usar 
from datetime import timedelta, date
print(timedelta(minutes=70))
print(date.today())