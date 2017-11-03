#!/usr/bin/python3
# Decomposes character into components

from sys import argv
from pymongo import MongoClient
import re

client = MongoClient()
db = client.dictionary


def decom(argument):
# Finds the in database and returns the object with its dictionary
    counter = 0
    seen = []
    final = []
    # Validates that Chinese character passed
    valid = re.findall(r'[\u4e00-\u9fff]+', argument)
    if valid == []:
        return ("Please enter a Chinese character")
    while (counter < len(argument)):
        for i in valid:
            for j in i:
                search_char = (db.characters.find({"character": j}))
                for decomp in search_char:
                    character = (decomp["character"])
                    definition = (decomp["definition"])
                    char_def = character + "  " + definition
                seen.append(char_def)
                for character in seen:
                    if character not in final:
                        final.append(char_def)
                counter += 1
        return (final)


def ele(argument):
# Finds elements from one db and their meanings from another
    counter = 0
    rad_mean = []
    valid = re.findall(r'[\u4e00-\u9fff]+', argument)
    seen = []
    if valid == []:
        return ("Please enter a Chinese character")

    while (counter < len(argument)):
        for i in valid:
            for j in i:
                search_char = (db.characters.find({"character": j}))
                for decomp in search_char:
                    elements = (decomp["decomposition"])
                    for each in elements:
                        search_radical = db.radicals.find({"radical": each})
                        for radical in search_radical:
                            r = (each + " " + radical["meaning"])
                            seen.append(r)
                            for i in seen:
                                if i not in rad_mean:
                                    rad_mean.append(i)
                counter += 1
        return (rad_mean)

if __name__ == '__main__':
    pass
