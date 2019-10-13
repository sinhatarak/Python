import
file = open("account.csv", r)
file.read()
print("done")

for x in range(1,11):

    if x == 2:
       break
    print (x)
--------------------

We have a bunch of stickers which say
"twitter" and we decide to cut these up
into their separate letters to make new words.
So, for example, one sticker would give us the
letters "T", "W", "I", "T", "T", "E", "R",
which we could rearrange into other word[s]
(like "write", "wit", "twit", etc)



Challenge:

Write a function that takes as its input an arbitrary
string and as output, returns the number of intact
“twitter” stickers we would need to cut up to recreate
that string.



Example: twitter_stickers(“write wit twit”) would
return "3", since we would need to cut up 3 stickers
to provide enough letters to write “write wit twit”

import math
import os
import random
import re
import sys

#
# Complete the 'twitter_stickers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING phrase as parameter.
#

def twitter_stickers(phrase):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    phrase = input()

    result = twitter_stickers(phrase)

    fptr.write(str(result) + '\n')

    fptr.close()

Books:-
    1) Unix internals by uris ahilivia
    2) advanced programming by richard
    3) How SRE workbook from google
    Desighn the unix OS by moris orks

    Coding:- elements in interviw, amit prakash
    Prorammng pearls by john pently kalpana Books


    ######
    Computer networking:- Top down approach by jeff ross
    Kernel by robert love (Kernel development)
    Understand the linux kernel by daniel and markos
    Leetcode.# COMBAK:


Question:- Fork Bomb (:(){ :|: & };:)
