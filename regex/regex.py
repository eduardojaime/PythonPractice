# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5

@author: Eduardo Jaime
"""
# Regular expression examples
# findall

import re
# specify pattern > strip <a> tags for link and title
# e.g. <a href="test">test</a>
pat = r'<a href="(.*?)".*?>([\w ,./]*)(?=</)'
#pat = r'((?<=href\=\").*(?=\"))|((?<=\"\>).*(?=\<\/a))'

n = int(input("Enter a number"))
for _ in range(n):
    html = input("Enter n anchor tags")
    res = re.findall(pat, html) # use findall to get all matches in groups ('ahref link','title')
    for link, title in res: # iterate through every match group
        print ("{},{}".format(link, title.strip())) # extract link and clean title, remove spaces


# find all DISTINCT html tags
# aimport re
pat = r'(?<=<)\w+' #any word character after a '<'

n = int(input("Enter n of inputs"))
# Save results in a set to avoid duplicates
l = set()
for i in range(n):
    s = input("Enter html text")
    results = re.findall(pat, s)
    for r in results:
        # removed any whitespaces (if any)
        a = r.strip()
        # avoid adding empty spaces to the set (if any)
        if a != '':
            l.add(a)
# sort set
o = sorted(l)
# print set of values separated by semi-colon
print(';'.join(o))


total = 0
l = []
n = int(input("Enter number of lines of text"))
for i in range(n):
    s = input("Enter a line of text to add to the list")
    l.append(s)
    
q = int(input("Enter number of words to search for"))
for i in range(q):
    s = input("Enter a word to search in the text")
    pat = r'\B(' + s.strip() + ')\B'
    results = re.findall(pat, "\n".join(l))
    print("Found " + s + ", " + str(len(results)) + " times")
    
# Identify IPv4 and IPv6 Addresses
ipv4Pattern = r'^((([0-1]?[0-9]?[0-9]?)|([2]?[0-5]?[0-5]?))\.){3}((([0-1]?[0-9]?[0-9]?)|([2]?[0-5]?[0-5]?)))$'
ipv6Pattern = r'^(([0-9a-f])*\:){7}([0-9a-f]){4}$'

n = int(input("Enter number of addresses to test"))
for i in range(n):
    s = input("Enter an IP address")
    if re.match(ipv4Pattern, s):
        print("IPv4")
    elif re.match(ipv6Pattern, s):
        print("IPv6")
    else:
        print("Neither")
    
    
# Search for whole word
s = ""
n = int(input("Enter number of lines of text to input"))
# use two separate for loops to avoid O(n^2)
for i in range(n):
    s += input("Enter some text") + "\n"
    
l = int(input("Enter number of words to search"))
for j in range(l):
    w = input("Enter word to search")
    # \b allows you to perform whole word search
    # https://www.regular-expressions.info/wordboundaries.html
    res = re.findall(rf'\b{w}\b', s)
    print(w + " found " + str(len(res)) + " times")

# Search for email addresses in text
import sys
# Get input until end of file is reached
p = sys.stdin.read()
# simple regular expression for detecting an email address example@mail.com
pat='[\w\.]+@(?:\w+\.)+\w+'
# find all occurrences
emaillist = re.findall(pat,p)
# convert to set to eliminate duplicates, then back to list, then sort, then show as values separated by semi-colon
print(';'.join(sorted(list(set(emaillist)))))

# Search for domain names in text
pattern = r'\bhttps?://(?:www\.)?([\w-]+\..*?)(?<=\.)(com|org|in|net|tv|me)\b'
 #r'(\w{0,3}\.)?(\w*)(\.[a-zA-Z]{2,3})'

s = ""
n = int(input("Enter number of lines of text"))
for i in range(n):
    s += input("Enter a line of text") + "\n"

ls = []
# use find all to get all matches
results = re.findall(pattern, s)
for r in results:
    # join results as a single element and add to temp list
    ls.append("".join(r))
# convert list to set, then sort and join elements with semi-colon
print(";".join(sorted(set(ls))))

# Search for comments in a block of code 
# comments are specified using '// one line comment' or /*comment block*/
import sys 
# find /*, followed by any character that's not a /, then */ OR // followed by any character
pattern = r'(\/\*[^\/]+\*\/|\/\/.+)'

# read input text
s = sys.stdin.read()
results = re.findall(pattern, s)
for r in results:
    print(r)

# Validate lat/lng coordinate pairs
pattern = r'\([+\-]?(90(\.0+)?|[1-8]\d(\.\d+)?|\d(\.\d+)?), [+\-]?(180(\.0+)?|1[0-7]\d(\.\d+)?|\d{2}(\.\d+)?|\d(\.\d+)?)\)'
n = int(input("Enter number of coordinates to validate: "))
for i in range(n):
    s = input("Enter a new coordinate pair separated by '/'. Example: (77.11112223331, 149.99999999) : ")
    if re.match(pattern, s):
        print("Valid")
    else:
        print("Invalid")

# Search a word within a line of text
pattern = r'\bPYTHON3\b'
n = int(input("Enter numer of lines of text to process:"))
count = 0


for i in range(n):
    s = input("Enter text: ")
    if re.search(pattern, s, re.IGNORECASE):
        count += 1

print("Word found : " + str(count))

# Get information from HTML tags
# Get an ID from an id field, text based on a tag with a specific class, and text within a span with a specific class
# 3 capture groups > one single result with three elements
pattern = r'question-summary-(\w\w\w\w\w)".*?class="question-hyperlink">(.+?)</a>.*?class=\"relativetime\">(.+?)</span>'

html = sys.stdin.read()

# find all
results = re.findall(pattern, html, re.DOTALL)

for r in results:
    print(";".join(r))
    
# Detect what programming language a given file is
# C if it includes the keywords '#include'
C = "(?s).*(#\\s*include\\s*(<\\s*[\\w/]+(\\.\\w+)?\\s*>|\"[\\w/]+(\\.\\w+)?\"\\s*))(?s).*"
# JAVA if it includes the keywords 'private,public,protected' and 'import'
JAVA = "(?s).*(^(public\\s+|private\\s+|protected\\s+)*.*\\w+\\(.*?\\)\\s*\\{|import\\s+[\\w\\.\\*]+;)(?s).*"
# Python if it uses 'print' and 'def'
PYTHON = "(?s).*(^print\\s\".*\"$|^#\\s.*$|def\\s.*$|^if\\s[^()]+:)(?s).*"

s = sys.stdin.read()
if (re.match(C, s)):
    print("C")
elif (re.match(JAVA, s)):
    print("Java")
else:
    print("Python")