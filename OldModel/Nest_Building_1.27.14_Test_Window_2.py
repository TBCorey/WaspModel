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
        #31.2 and 24.3 mg at two diff sites (Suzuki 1980) avg? How to convert to P. dominulus? Divide avg weight?
        #or, workers consumed 1.38 +/- 0.04 times their body weight
        self.dev_stage = dev_stage #egg, larvae, or pupae
        self.status = status
    def metamorphose(self, age): #should sort brood by age first
        for b in nest.brood_list:
            sorted(nest.brood_list, key=lambda b: b.age)
        for b in nest.brood_list:
            if 11 <= age < 27:
                self.dev_stage = "larvae"
            if 27 <= age < 40:
                self.dev_stage = "pupae"
            if age == 40: #and also day in colony cycle, b/c they could be reproductives
                nest.brood_list.pop()#but how can I remove the 40-day brood, specifically?
                w = Worker(40, "alive")
                nest.worker_list.append(w)

#Test instances here
nest = Nest("Pd")

nest.brood_list.append(Brood(40, "need", "pupae", "alive"))
nest.brood_list.append(Brood(28, "need", "pupae", "alive"))

for b in nest.brood_list:
    print(b.age)
    
print("Brood list:", nest.brood_list)
print("Nest workers:", nest.worker_list)

for b in nest.brood_list:
    b.metamorphose(b.age)
    print("Post-eclosion brood:", b.age, nest.brood_list)

print("Post-eclosion nest workers: ", nest.worker_list)
