from random import randint, choice, uniform
#below are the Queen and Nest classes, with Brood and Worker too


class Nest(object):
    max_cell_count = randint(34, 130) #maximum nest size from field data
    brood_list = []
    worker_list = []
    repro_list = [] #list for reproductives, which do not forage for the nest (but do they still go kill caterpillars?)
    total_cell_count = 0 #removed current_cell_count - that's the same as the present total!
    free_cell_count = 0
    def __init__(self, species): 
        self.species = species
        
    #def pass_day: #see above, add age to all the wasps, factor in daily mortality rate too?
    #def add_cell that checks to see if queen can add an egg - necessary?

class Brood(object):
    def __init__(self, age, food_need, dev_stage, status):
        self.age = age
        self.food_need = food_need #food need could be calculated as: 1. total need to pupate, subtract from each day, 2. daily need that always increases, if reach threshold, dies
        self.dev_stage = dev_stage #egg, larvae, or pupae
        self.status = status
    #def eclose(self): - call when age is 40 or greater
    def metamorphose(self, age):
        def metamorphose(self, age): #should sort brood by age first
            for b in nest.brood_list:
                if 11 <= age < 27:
                    self.dev_stage = "larvae"
                if 27 <= age < 40:
                    self.dev_stage = "pupae"
                if age == 40: #and also day in colony cycle, b/c they could be reproductives
                    nest.brood_list.pop()#but how can I remove the 40-day brood, specifically?
                    w = Worker(40, "alive")
                    nest.worker_list.append(w)

class Queen(object):
    mortality_rate = 10
    build_options = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5]
    #egg_laying_rate - have a funciton instead for lay_egg
    def __init__(self, age, build_rate, mass):
        self.age = age
        self.build_rate = choice(self.build_options)
        self.mass = round(uniform(0.086, 0.114), 3) #important to compare to usurper, mean = 0.10 g +/- SE 0.002g, n = 48, so SD is +/- 0.014
    def build_cell(self): #takes 0 positional arguments, but 1 was given
        if nest.free_cell_count < 1 and nest.total_cell_count < nest.max_cell_count:
            nest.total_cell_count += self.build_rate
            nest.free_cell_count += self.build_rate #remember to make sure that Queen only lays eggs when there is a complete cell
    def lay_egg(self):
        while nest.free_cell_count >= round(1, 0): #while there is at least 1 empty cell (round makes sure wasp doesn't lay in incomplete cell
            b = Brood(0, "need", "egg", "alive") 
            nest.brood_list.append(b) #add a brood b to nest.brood_list with the above arguments
            nest.free_cell_count -= 1 #subtract 1 free cell from the nest for each egg laid

count = 0
nest = Nest("Pd")
queen = Queen(40, "build", "mass")
print("Max nest size =", nest.max_cell_count)
print("Queen's build rate =", queen.build_rate)
while count < 120:
    print("--- DAY", count, "---")
    queen.build_cell()
    print("After building cells, before laying eggs:")
    print("Free cells =", round(nest.free_cell_count, 1))
    print("# brood =", len(nest.brood_list))
    print("Queen lays egg(s):")
    queen.lay_egg()
    print("# brood:", len(nest.brood_list))
    print("Free cells =", round(nest.free_cell_count, 1))
    count += 1
