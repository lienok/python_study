from sys import argv, exit  # inputs on the command line access via argv

script, value, units = argv  #set those as expected arguments!

value = float(argv[1])  #convert input to float number
units = argv[2]

#constants to use
cm = "cm"
inch = "inch"
coeficient = 0.39370079

#units to remember
unitsEntered = ""
unitsReturn = ""

if(units.lower().strip() == cm): 
	unitsEntered = cm
	unitsReturn = inch
elif (units.lower().strip() == inch) :
	unitsEntered = inch
	unitsReturn = cm
else :
	exit("Wrong inputs! Expected number and units. Example: 3 cm or 4 inch !")  #exit program with the message

print
print ("You want to convert %s %s ?") % (value, units)
answer = raw_input("Enter yes or y to continue: ")   #ask for input
if not answer.startswith("y") :
	exit("You choose TO NOT continue. We will not convert it for you! ")
	
# make conversion according to the enterd value
if (unitsEntered == cm):	
	result = value * coeficient	
else: 
	result = value / coeficient
		
print
print ("**** %5.2f %s is %5.2f %s ***") % (value, unitsEntered, result, unitsReturn)
print