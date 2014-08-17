import re

# open text file of 2008 NH primary Obama speech
file = open("obama-nh.txt", "r")
text = file.readlines()
file.close()

# compile the regular expression
keyword = re.compile(r"the ")

# search file for keyword, line by line
for line in text:
  if keyword.search(line):
    print line 

# TODO: print all lines that DO NOT contain "the "
# TODO: print lines that contain a word of any length starting with s and ending with e
  
# date = raw_input("Please enter a date in the format MM.DD.YY: ")
# keyword = re.compile(r"(\d\d?)\.(\d\d?)\.(\d\d)")
# result = keyword.search(date)
# if result:
#   print "Month: ", result.group(1)
#   print "Day: ", result.group(2)
#   print "Year: ", result.group(3) 

# TODO: Write a regular expression that finds html tags in example.html and print them.