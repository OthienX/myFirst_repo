import calendar
dec = calendar.TextCalendar(calendar.MONDAY)
#dec.prmonth(2022,12)
#use to display the number of leap years between specific years
print("<<<<<<<<<<<displaying the number of leap years>>>>>>>>>>>>")
#year1 = int(input("enter first yr\n"))

#year2 = int(input("second yr\n"))
#leaps= calendar.leapdays(year1,year2)
#print(leaps)
# to display the days, weeks and year of a given year
#year= int(input("enter a given year\n"))
#print(calendar.prcal(year))
#to display the number of days in a given month by using a simple loop
#cal =calendar.TextCalendar(calendar.SUNDAY)
#for i in cal.itermonthdays(2022, 6):
   # print(i)
    #printing of the individual months or days of the week
#print(calendar.weekday(2022,12,4))
#print(calendar.month(2022,12))
#year1 = int(input("first yr\n "))
#year2 = int(input("second yr\n"))

#print(calendar.leapdays(year1, year2))
year =int(input("year"))
print(calendar.calendar(year))
