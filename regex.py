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

