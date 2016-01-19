print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow'  	#single-quotes or double-quotes - either way is acceptable
print "And everywhere that Mary went."
print "." * 10  # prints ten times the string in quotes.

end1 = "K"
end2 = "r"
end3 = "a"
end4 = "s"
end5 = "n"
end6 = "y"
end7 = "D"
end8 = "n"
end9 = "i"
end10 = "k"
end11 = "!"

print end1 + end2 + end3 + end4 + end5 + end6,  #comma at the end connect it with a next line without an empty line between
print end7 + end8 + end9 + end10 + end11

#funny moving slash :)
while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,