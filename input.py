import datetime
print("enter three action to schedule your day!")
date= str(datetime.datetime.now())

print (date)
time= int(date[11:19])
i = 0
time1 = date
for i in range (date):
    action = input()
    time2 = time1 + int(input("how much time (in hours) would you like to allocate for this action? "))
    print ("you will have " + str(action) + "  " + "from " + str(time1) + " " + "until " + str(time2) + " .Is there anything else you would like to add to your schedule?")
    time1 = time2
    i += 1
    
