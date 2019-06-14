import sys
import random

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
        board[i][j] = num
        numsused.append(num)


with open(file, "w") as f:
    for i in range(9):
        for j in range(9):
            if random.random() > dif/9:
                 options = [k for k in range(1,10) if \
                 (k not in su_info["square"][(i//3)*3+j//3] and \
                 k not in su_info["row"][i] and\
                 k not in su_info["col"][j])]
                 option = random.choice(options)
                 str = f"{option}," if j < 8 else f"{option}"
                 su_info["square"][(i//3)*3+j//3].append(option)
                 su_info["row"][i].append(option)
                 su_info["col"][j].append(option)
                 f.write(str)
            else:
                str = " ," if j < 8 else " "
                f.write(str)
        f.write("\n")
