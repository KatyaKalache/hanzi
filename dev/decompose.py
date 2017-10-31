#!/usr/bin/python3
# Decomposes character into components

from sys import argv
from pymongo import MongoClient
import re

client = MongoClient()
db = client.dictionary

if (len(argv) < 2):
    print ("Please enter at least one character")
    exit()

def decom():
    argument = argv[1]
    counter = 0
    valid = re.findall(r'[\u4e00-\u9fff]+', argument)
    dictionary = {}
    if valid == []:
        print ("Please enter a Chinese character")
    while (counter < 3):
        for i in valid:
            for j in i:
                search_char = (db.characters.find({"character": j}))
                for decomp in search_char:
                    definition = (decomp["definition"])
                    print (definition)
        counter += 1
#    return (search_char)
search_char=decom()
#search_char=decom()
#print (search_char)
#def translate(search_char):
 #   for decomp in search_char:


  #      elements = (decomp["decomposition"])
   #     character = (decomp["character"])
    #    definition = (decomp["definition"])
     #   res = (character + " " + definition + '\n' + elements)
      #  print (elements)
   # return (elements)
#elements = translate(search_char)

#def radical(elements):
 #   for each in elements:
  #      search_radical = db.radicals.find({"radical": each})
   #     for radical in search_radical:
    #        rad_mean = (each + radical["meaning"])
     #       print (rad_mean)
    #return (rad_mean)
#rad_mean = radical(elements)
