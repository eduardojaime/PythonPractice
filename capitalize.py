# -*- coding: utf-8 -*-
# Complete the solve function below.
def solve(s):
    result = ""
    index = 0
    for char in s:
        if index == 0:
          char = s[index].capitalize()  
          result += char
        else:
            if s[index-1] == " ":
                char = s[index].capitalize()  
                result += char
            else:
                result += char
        index += 1
    return result

test0 = "title example"
print(solve(test0))

test1 = "1 w 2 r 3g"
print(solve(test1))
# Expected '1 W 2 R 3g'

test2 = "hello   world  lol"
print(solve(test2))
# Expected 'Hello   World  Lol'