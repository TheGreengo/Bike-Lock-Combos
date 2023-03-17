import enchant
import os

directory = os.path.expanduser("~/<filepath>")
os.chdir(directory)
file = open("words.txt", "w")

firstLetter = ["b","f","l","d","w","t","m","h","p","s"]
secondLetter = ["a","i","l","e","y","h","n","r","u","o"]
thirdLetter = ["t","r","l","m","n","e","k","s","o","a"]
fourthLetter = ["b","e","t","k","l","y","p","m","n","s"]

d = enchant.Dict("en_US")

for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                if d.check(firstLetter[i] + secondLetter[j] + thirdLetter[k] + fourthLetter[l]):
                    file.write(firstLetter[i] + secondLetter[j] + thirdLetter[k] + fourthLetter[l])
                    file.write("\n")

file.close()