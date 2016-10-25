import datetime
date= str(datetime.datetime.now())
print("enter three action to schedule your day!")

print (date)
hours= int(time[0:2])
minutes= int(time[4:5]
time1 = hours minutes
for i in range (hours:minutes):
    action = input()
    time2 = time1 + int(input("how much time (in hours) would you like to allocate for this action? "))
    print ("you will have " + str(action) + "  " + "from " + str(time1) + " " + "until " + str(time2) + " .Is there anything else you would like to add to your schedule?")
    time1 = time2
    i += 1
    
