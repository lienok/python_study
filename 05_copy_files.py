from sys import argv
from os.path import exists

script, from_file, to_file = argv


print "Copying from %s to %s" % (from_file, to_file)

indata = open(from_file).read()  #kind of print the file to indata variable


print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)  #check if file exists based on its name, import is needed os.path
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w') #create file for writing
out_file.write(indata)

print "Alright, all done."

#close both file objects
out_file.close()