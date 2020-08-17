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
n = int(input("Enter number of lines of text00"))
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
