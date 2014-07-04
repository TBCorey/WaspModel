#Test for foraging function

from random import randint, choice, uniform



class Nest(object):
    max_cell_count = randint(34, 130) #maximum nest size from field data
    brood_list = []
    worker_list = []
    repro_list = [] #list for reproductives, which do not forage for the nest (but do they still go kill caterpillars?)
    total_cell_count = 0 #removed current_cell_count - that's the same as the present total!
    free_cell_count = 0
    def __init__(self, species): 
        self.species = species

nest = Nest("Pd")

class Worker(object):
    mortality_rate = 10 #in daily_mortality function, random number generate (0, 100), if randint < mortality_rate then wasp dies
    def __init__(self, age, alive):
        self.age = age
    def forage(self):
        kills_today = 0
        flesh_today = 0
        for w in nest.worker_list: #But how to build in foraging success rate here?
            today_foraging_hours = 5
            caterpillars_killed = 0.665*today_foraging_hours #*len(nest.worker_list) #len(worker_list) gives the # of workers!
            flesh_gathered = caterpillars_killed*0.014 #average payload capacity of workers
            print("Slain caterpillars =", caterpillars_killed)
            print("Gathered flesh =", flesh_gathered, "g")
        kills_today += caterpillars_killed
        flesh_today += flesh_gathered
        print(kills_today)
        print(flesh_today)
        



print(nest.worker_list)

count = 0

while count < 5:
    w = Worker(40, "alive")
    nest.worker_list.append(w)
    count += 1

print(nest.worker_list)

caterpillars_killed_today = 0
flesh_gathered_today = 0
        
for w in nest.worker_list:
    w.forage()
