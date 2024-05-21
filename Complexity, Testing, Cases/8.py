my_army, health_enemy, enemy = [int(input()) for _ in range(3)]


def count_steps(my_army, health_enemy, enemy_coeff):
    coeff = (1 + 5 ** 0.5) / 2
    step = 0
    enemy = 0
    if my_army >= health_enemy: return 1
    if my_army <= enemy_coeff and my_army <= (health_enemy - my_army): return -1
    if enemy_coeff >= my_army * 2: return -1
    if my_army <= enemy_coeff and my_army * coeff < enemy_coeff + (health_enemy - my_army): return -1
    if my_army >= enemy_coeff + health_enemy: return 2
    # step 1
    health_enemy -= my_army
    step = 1
    while (health_enemy + enemy) > 0:
        enemy = enemy + enemy_coeff if health_enemy > 0 else enemy + 0
        if health_enemy > 0:
            condition = int(str(round(my_army * coeff, 1))[:-2])
            if condition >= health_enemy + enemy:
                var1 = first_health(my_army, health_enemy, enemy)
                var2 = first_soldiers(my_army, health_enemy, enemy, enemy_coeff)
                if var2 == 0:
                    step += var1
                else:
                    step += var1 if var1 < var2 else var2
                break
            else:
                if enemy > my_army:
                    enemy = enemy - my_army
                    my_army -= enemy
                else:
                    health_enemy = health_enemy - (my_army - enemy) if health_enemy > my_army - enemy else 0
                    enemy = 0
            step += 1
        else:  # health_enemy = 0
            enemy = enemy - my_army if enemy > my_army else 0
            my_army -= enemy
            step += 1
    return step


def first_health(my_army, health_enemy, enemy):
    enemy = enemy - (my_army - health_enemy) if enemy > my_army - health_enemy else 0
    health_enemy = 0
    my_army -= enemy
    step_var1 = 1
    while enemy > 0:
        enemy = enemy - my_army if enemy > my_army else 0
        my_army -= enemy
        step_var1 += 1
    return step_var1


def first_soldiers(my_army, health_enemy, enemy, enemy_coeff):
    if enemy > my_army: return 0
    health_enemy = health_enemy - (my_army - enemy) if health_enemy > my_army - enemy else 0
    enemy = 0
    step_var2 = 1
    enemy = enemy + enemy_coeff if health_enemy > 0 else enemy + 0
    step_var2 += first_health(my_army, health_enemy, enemy)
    return step_var2


print(count_steps(my_army, health_enemy, enemy))
# print(count_steps(10, 11, 15)) #4
# print(count_steps(25, 200, 10)) #13 ok
# print(count_steps(250,500,208)) #5 - ok
# print(count_steps(250, 500, 187)) #4 -ok
# print(count_steps(250, 500, 218)) #6 - ok  !!!
# print(count_steps(250, 500, 230))#8 -ok
# print(count_steps(499, 500, 499))#50  3 - ok
# print(count_steps(250, 500, 249))#39  101  !!!
# print(count_steps(13, 81, 10))#131    23 ok !!!
# print(count_steps(499, 500, 499))#3 - ok
# print(count_steps(2,3,3)) #-1
# print(count_steps(9, 427,1)) #54
# print(count_steps(3000,5000,3000))
