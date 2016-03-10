print ":) :) :)"
\
date=raw_input("Please input a date in correct type: dd/mm/yyyy:")
date=date.split("/")
day=int(date[0])
month=int(date[1])
year=int(date[2])
century=year/100
var_for_disekto=int(date[1])

#code for month
if (month==2 or month==3 or month==11):
	month=4
elif (month==4 or month==7):
	month=0
elif (month==5):
	month=2
elif (month==6):
	month=5
elif (month==8):
	month=3
elif (month==9 or month==12):
	month=6
elif (month==1 or month==10):
	month=1
	
#code for century	
if (century==16 or century==20):
	century=6
elif (century==17 or century==21):
	century=4
elif (century==18 or century==22):
	century=2
elif (century==19 or century==23):
	century=0


#code for year
codeyear=(century+(year%100)+(year%100)/4)%7

#the outcome
day=(codeyear+month+day)%7	

#measure disektou
etos=1
if (year%4==0):
	etos=2
	
if (etos==2 and (var_for_disekto==1 or var_for_disekto==2)):
	day=day-1


print "The day was:"

if (day==0):
	print "Saturday"
elif (day==1):
	print "Sunday"
elif (day==2):
	print "Monday"
elif (day==3):	
	print "Tuesday"
elif (day==4):
	print "Wednesday"
elif (day==5):
	print "Thursday"
elif (day==6):
	print "Friday"
elif (day==-1):
	print "Friday"
	
print ":) :) :)"