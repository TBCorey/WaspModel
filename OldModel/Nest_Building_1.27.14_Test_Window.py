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

class Worker(object):
    mortality_rate = 10 #in daily_mortality function, random number generate (0, 100), if randint < mortality_rate then wasp dies
    def __init__(self, age, status):
        self.age = age
        self.status = status

class Brood(object):
    def __init__(self, age,food_need, dev_stage, status):
        self.age = age
        self.food_need = food_need #food need could be calculated as: 1. total need to pupate, subtract from each day, 2. daily need that always increases, if reach threshold, dies
        self.dev_stage = dev_stage #egg, larvae, or pupae
        self.status = status
    #def eclose(self): - call when age is 40 or greater
    def metamorphose(self, age):
        for b in nest.brood_list:
            if 11 <= age < 27:
                self.dev_stage = "larvae"
            if 27 <= age < 40:
                self.dev_stage = "pupae"
            if age >= 40:
                nest.brood_list.remove(b)
                w = Worker(40, "alive")
                nest.worker_list.append(w)


#Test instances here
nest = Nest("Pd")

nest.brood_list.append(Brood(10, "need", "egg", "alive"))
nest.brood_list.append(Brood(16, "need", "egg", "alive"))
nest.brood_list.append(Brood(28, "need", "egg", "alive"))
nest.brood_list.append(Brood(41, "need", "egg", "alive"))
print(nest.brood_list)

for b in nest.brood_list:
    print("Pre-meta() age and dev:", b.age, b.dev_stage)

for b in nest.brood_list:
    b.metamorphose(b.age)
    print("Post-meta() age and dev stage:", b.age, b.dev_stage)

print("Nest workers: ", nest.worker_list)
