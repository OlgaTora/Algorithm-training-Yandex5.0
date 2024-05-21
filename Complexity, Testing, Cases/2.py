g1 = list(map(int, input().split(':')))
g2 = list(map(int, input().split(':')))
flag = int(input())
goals = 0
gamer1 = g1[0] + g2[0]
gamer2 = g1[1] + g2[1]
if gamer1 > gamer2:
    goals = 0
elif gamer1 < gamer2:
    match flag:
        case 1:  # home
            goals = gamer2 - gamer1
            if (goals + g2[0]) <= g1[1]:
                goals += 1
        case 2:
            goals = gamer2 - gamer1
            if g1[0] <= g2[1]:
                goals += 1
else:
    match flag:
        case 1:  # home
            if g2[0] <= g1[1]:
                goals = 1
        case 2:
            if g1[0] <= g2[1]:
                goals = 1
print(goals)
