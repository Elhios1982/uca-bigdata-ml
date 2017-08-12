from genetic import *
target = 30
p_count = 50
i_length = 30
i_min = 0
i_max = 1
gen = 0
p = population(p_count, i_length, i_min, i_max)
fitness_history = [grade(p, target),]

for i in range(50):
    p = evolve(p, target, retain = 0.2, random_select = 0.7, mutate = 0.05)
    fitness_history.append(grade(p, target))

for datum in fitness_history:
   gen += 1
   print(str(gen) + ".- " + str(datum))
