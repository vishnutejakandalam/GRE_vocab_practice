
import pickle
from learn import search_key
import os
import sys
from values import MAGOOSH_DICT
import pyttsx3 as pyttsx

engine = pyttsx.Engine()
engine.setProperty('voice', "malayalam")  #changing index, changes voices. o for male

while True:
    count = 0
    choice = input("Choose one: [1: common_words | 2: basic | 3: advanced]")
    deck = MAGOOSH_DICT[int(choice)]
    y = input('Enter roman numeral for deck: ')
    path = 'magoosh/Data/' + deck + y + '.p'

    unknowns = []
    with open(path, 'rb') as handle:
        words = pickle.load(handle)
    print()
    print("Total number of words: ",len(words))
    print("Press Enter if you know it or n and Enter if you don't know it c and Enter fi you wnat to check it: ")
    i=0
    for k in words.keys():
        # print k
        i+=1
        engine.say(k)
        engine.runAndWait()
        val = input("\t\t"+str(i)+". "+k+": ")
        if val == "":
            count +=1
        elif val in ["n", "c"]:
            search_key('meaning', k,words)       
            # search_key('mnemonic', k,words)
            if val == "c":
                val = input("Was your guess correct? <Enter>|n")
            if val == "n":
                unknowns.append(k)
            elif val == "":
                count+=1

    print("\nLength of Known words: ", count, "\n Length of Unknown words: ",len(words) - count)
    if len(unknowns) != 0:
        with open("unknowns.txt", 'a') as file:
            for k in unknowns: 
                file.write(k+"\n")
    else:
        print("Congrats you finished whole set :)")
        if os.path.exists("unknowns_"+deck+y+".txt"):
            os.remove("unknowns_"+deck + y+".txt")
    try:
        _ = input("Press enter to try another set, CTRL+C to exit. \n")
    except KeyboardInterrupt:
        print("Bye Bye..!")
        sys.exit(0)
    print()
    print()
