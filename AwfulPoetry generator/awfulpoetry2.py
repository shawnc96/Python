import random
import sys

articles = ["the", "a", "another"]
subjects = ["cat", "dog", "man", "woman"]
verbs = ["sang", "ran", "jumped", "hoped", "laughed"]
adverbs = ["loudly", "quietly", "well", "badly"]


try:
       
    val = 5
    if len(sys.argv)>1:
        try:
            if int(sys.argv[1])>0 and int(sys.argv[1])< 11:
                val=int(sys.argv[1])
        except ValueError as err:
            print(err)
    

    i=0
    while i < val:
        art = random.choice(articles)
        sub = random.choice(subjects)
        ver = random.choice(verbs)
        adv = random.choice(adverbs)

        x = random.randint(1,2)

        if x == 1:
            print(art, sub, ver, adv)
        elif x==2:
            print(art, sub, ver)
        i+=1

except IndexError:
    print("usage error")
except ValueError as err:
    print(err)
        
