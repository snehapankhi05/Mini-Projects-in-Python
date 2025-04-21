"""
# Write a python program to translate a message into secret code language.
Use the rules below to translate normal English into secret code language

Coding:
if the word contains atleast 3 characters, remove the first letter and append it at the end
now append three random characters at the starting and the end
else: simply reverse the string

Decoding:
if the word contains less than 3 characters, reverse it 11 # else:
remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

ask the user what they want encode or decode

"""

import random
import string
def encode(word):

    for i in word:

        if len(i)<3:
            print(i[::-1],end=" ")
        else:
            letter= i[1:]+i[0]
            randomletters = ''.join(random.choices(string.ascii_lowercase, k=3))
            print(randomletters+letter+randomletters,end=" ")

def decode(word):
    for i in word:
        if len(i)<3:
            print(i[::-1],end=" ")
        else:
            print(i[-4]+i[3:-4],end=" ")




print("Hello!!")
print("Welcome to the world of secret code🤐🤫")
sent=input("Please enter your sentence")
word=sent.split()
op=int(input("Please select what you want ??\n1)Encode\n2)Decode"))

if op==1:
    encode(word)

elif op==2:
    decode(word)

else:
    print("Invalid choice")