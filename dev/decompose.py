#!/usr/bin/python3
# Decomposes character into components

from sys import argv
from pymongo import MongoClient
import re

if __name__ == '__main__':
    client = MongoClient()
    db = client.dictionary

    if (len(argv) < 2):
        print ("Please enter at least one character")
        exit()


    def decom():
    # Finds the in database and returns the object with its dictionary
        argument = argv[1]
        counter = 0
        # Validates that Chinese character passed
        valid = re.findall(r'[\u4e00-\u9fff]+', argument)
        res = []
        if valid == []:
            print ("Please enter a Chinese character")
            exit()
        while (counter < len(argv)):
            for i in valid:
                for j in i:
                    search_char = (db.characters.find({"character": j}))
                    res.append(search_char)
                return (res)
            counter += 1
    res = decom()


    def translate(res):
    # Returning character requested and it's translation
        final = ""
        counter = 0
        while (counter < len(argv)):
            for obj in res:
                for decomp in obj:
                    character = (decomp["character"])
                    definition = (decomp["definition"])
                    char_def = character + " " + definition
                    final += char_def + "\n"
            counter += 1
        return (final)
    final = translate(res)
    print (final)
    res = decom()


    def ele(res):
    # Finds elements from one db and their meanings from another
        counter = 0
        rad_mean = ""
        while (counter < len(argv)):
            for obj in res:
                for decomp in obj:
                    elements = (decomp["decomposition"])
                    print(elements)
                    for each in elements:
                        search_radical = db.radicals.find({"radical": each})
                        for radical in search_radical:
                            r = (each + " " + radical["meaning"] + "\n")
                            rad_mean += r
            counter += 1
        return (rad_mean)
    rad_mean = ele(res)
    print (rad_mean)
