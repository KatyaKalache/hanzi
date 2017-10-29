#!/usr/bin/python3
# Decomposes character into components

from sys import argv
from pymongo import MongoClient
import re

if __name__ == "__main__":
    client = MongoClient()
    db = client.dictionary
    if (len(argv) < 2):
        print ("Please enter at least one character")
    else:
        argument = argv[1]
        valid = re.findall(r'[\u4e00-\u9fff]+', argument)
        if valid == []:
            print ("Please enter a chinese character")
        for i in valid:
            search_char = db.characters.find({"character": i})
            for decomp in search_char:
                elements = decomp["decomposition"]
                print (decomp["character"])
                print (decomp["definition"])
                for each in elements:
                    search_radical = db.radicals.find({"radical": each})
                    for radical in search_radical:
                        print (each, end=" - ")
                        print (radical["meaning"])
