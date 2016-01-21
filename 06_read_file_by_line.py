from sys import argv

script, input_file = argv

#read all file and print it on screen
def print_all(f): 
    print f.read()

#move on the begining of the file
def rewind(f):
    f.seek(0)

#print f. line of the file
def print_a_line(line_count, f):
    print line_count, f.readline(),  #comma at the end will avoid the \n new line between prints
	
current_file = open(input_file)

print "First let's print the whole file:\n"
print_all(current_file)

print "Now let's rewind, kind of like a tape."
rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)