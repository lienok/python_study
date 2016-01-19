from sys import argv

script, filename = argv
prompt = "> "

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."  #interrupt the script
print "If you do want that, hit RETURN."

raw_input(prompt)  
print "Opening the file..."
target = open(filename, 'w')  # passing w to make the file writable, Overwrites the file if the file exists. 

print "Truncating the file.  Goodbye!"
target.truncate()  #delete the content of the file in target variable - but becouse the overwriting, it is not needed.

print "Now I'm going to ask you for three lines."
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
empty_line = "\n"
target.write(line1 + empty_line + line2 + empty_line + line3)

print "And finally, we close it."
target.close()

