import sys
import random

#https://stackoverflow.com/questions/10488719/generating-a-sudoku-of-a-desired-difficulty
#file donde se va a escribir
file = sys.argv[1]

nums = [1,2,3,4,5,6,7,8,9]


#difficulty
dif = int(input("dificultad (1-9)?:"))

su_info = {}
su_info["square"] = {i:[] for i in range(9)}
su_info["row"] = {i:[] for i in range(9)}
su_info["col"] = {i:[] for i in range(9)}

nums = [1,2,3,4,5,6,7,8,9]
numsused = []
#first
for i in range(3):
    for j in range(3):
        num = random.choice([i for i in nums if i not in numsused])
        numsused.append(num)
