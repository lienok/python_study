from sys import argv

script, filename = argv
prompt = "> "

txt = open(filename)  #open file = create a file object 
print "Here's your file %r:" % filename
print txt.read()  #print content of the file on a consoles
txt.close()  #better to close the file