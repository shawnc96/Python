import random


articles = ["the", "a", "another"]
subjects = ["cat", "dog", "man", "woman"]
verbs = ["sang", "ran", "jumped", "hoped", "laughed"]
adverbs = ["loudly", "quietly", "well", "badly"]



i=0
while i < 5:
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
    
