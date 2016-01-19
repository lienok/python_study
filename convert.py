import sys

#Read inputs from user. 
#Expects to have on 1.index real number and on 2.index the unit which from which you convert (either "inch" or "cm")
if len(sys.argv) < 3:
	sys.exit("Error, missing inputs! Expected number and units. Example: 3 cm or 4 inch")

value = float(sys.argv[1])
units = sys.argv[2]

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
	sys.exit("Wrong inputs! Expected number and units. Example: 3 cm or 4 inch !")

print
print ("You want to convert %s %s ?") % (value, units)
answer = raw_input("Enter yes or y to continue: ") 
if not answer.startswith("y") :
	sys.exit("You choose TO NOT continue. We will not convert it for you! ")
	
# make conversion according to the enterd value
if (unitsEntered == cm):	
	result = value * coeficient	
else: 
	result = value / coeficient
		
print
print ("**** %5.2f %s is %5.2f %s ***") % (value, unitsEntered, result, unitsReturn)
print