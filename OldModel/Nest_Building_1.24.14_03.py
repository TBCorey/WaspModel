#How to represent the nest in the model #Ver 03 - brood and worker classes
#nest = [] #empty list, that you can add Wasp objects to it, iterate through the list with a for loop and run their methods
    #instead, making a Nest class that has cell counts and other attributes


#HERE IS A FUNCTION TO ADD WASPS TO THE NEST WOOO #except that this should be a method in Nest(object) and/or Queen(object)
def populate_nest(num, nest): #takes the argument number of wasps to add) and the list nest
    for i in range(num): #for each item in the range num
        w = Worker(40) #new wasp! w is just a placeholder name, but it will create a new instance of the object with age 40, adult
        nest.append(w) #use the .append command used in lists to add w (the wasp instance) to the list nest

def pass_day(nest): #this a function to age the wasps in this example, could also do anything for
    for w in nest: #for w, each instance of wasp in the list nest
        w.age += 1 #remember that .notation can change the attribute of the instance(s) w
    for b in nest.brood_list: #for the instances of brood, b, in the list brood_list
        b.age += 1 #add 1 to the age of each brood in the list
        if b.age >= 40:
            populate_nest(1, nest) #call the populate nest function, which will add 1 wasp to the list nest
            nest.free_cell_count += 1 #increment free_cell_count when the brood ecloses
            
        #if w.age > MAX_AGE:
            #w.die() #method for wasp to die
populate_nest(15, nest)
pass_day(nest)

#class Nest()
    #brood_list
    #list_of_wasps
    #total_cell_count
    #max_cell_count
    #free_cell_count
    #queen
    #lifespan #don't need this - instead the lifespand will be determined by the survival of individuals on the nest
    #add_egg() #method for adding eggs in the nest itself, but have a method in queen class for lay_egg that calls add_egg
        #if free_cell_count > 0 and queen.alive == True:
            #queen.lay_egg()
                #b = Brood(0) #b is an instance of the Brood(age) class, with an age of 0
                #brood_list.append(b) ##add b to the list brood_list, where 0 represents the age of the brood
                #free_cell_count -= 1

from random import randint, choice
#below are the Queen and Nest classes, with Brood and Worker too


class Nest(object):
    max_cell_count = randint(34, 130) #maximum nest size from field data
    brood_list = []
    adult_list = []
    current_cell_count = 0
    total_cell_count = 0
    free_cell_count = 0
    def __init__(self, species): 
        self.species = species
        if species == "Pd":
            build_options = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5]
            queen = Queen(0, choice(build_options), 0.5) #BUILD IN HAPLOMETROSIS AFTER PRELIMINARY MODEL IS RUNNING, 0.5 is test
            Nest.adult_list.append(queen)
    #def pass_day: #see above, add age to all the wasps, factor in daily mortality rate too?
    #def add_cell that checks to see if queen can add an egg - necessary?

class Queen(object):
    mortality_rate = 10
    #egg_laying_rate - have a funciton instead for lay_egg
    def __init__(self, age, build_rate, mass):
        self.age = age
        self.build_rate = build_rate
        self.mass = mass #important to compare to usurper
    def build_cell(self): #takes 0 positional arguments, but 1 was given
        if nest.free_cell_count == 0:
            nest.total_cell_count += build_rate
            nest.free_cell_count += build_rate #remember to make sure that Queen only lays eggs when there is a complete cell
    def forage(self):
       foraging_success = #value
        if randint(1, 100) > foraging_success:
            caterpillars_killed_today = 0.655*date_foraging_hours #need to define outside this?
            flesh_gathered = 0.014*caterpillars_killed_today #0.014 should be max payload capacity - check!
            total_caterpillars_killed += caterpillars_killed_today
        
    #def feed_brood():

nest = Nest("Pd") #test making a nest - still need to debug this quite a bit

class Brood(object):
    def __init__(age,food_need, dev_stage):
        self.age = age
        self.food_need = food_need #food need could be calculated as: 1. total need to pupate, subtract from each day, 2. daily need that always increases, if reach threshold, dies
        self.dev_stage = dev_stage #egg, larvae, or pupae
    #def eclose(): - call when age is 40 or greater
    def metamorphose(self, age):
        for b in nest.brood_list
        if 11 <= age < 27:
            self.dev_stage = "larvae"
        if 27 <= age < 40:
            self.dev_stage = "pupae"
    #def daily_mortality(): - check against daily mortality rates for each dev stage; egg, larvae, pupae

        
class Worker(object):
    mortality_rate = 10 #in daily_mortality function, random number generate (0, 100), if randint < mortality_rate then wasp dies
    def __init__(self, age):
        self.age = age

class Usurper(Queen): #A usurper is a queen, after all, so it should inherit the same methods, except that it also has usurp()
    def __init__(self, mass): #make sure to add same args to __init__ as for Queen
        self.mass = mass
        
        
    #def build_cell: #should workers have this method too?
        
#make the instance of the class Nest() named nest (lowercase n)
#pass_day():

#to sort a list of complex objects

#peepz = sorted(people, key=lambda person: person.age) #command is sorted(listname, key=lambda, 
    #for p in peepz:
        #print(p.name, p.age)
