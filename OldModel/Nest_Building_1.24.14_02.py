#How to represent the nest in the model
#nest = [] #empty list, that you can add Wasp objects to it, iterate through the list with a for loop and run their methods
    #instead, making a Nest class that has cell counts and other attributes

class Worker(object):
    def __init__(self, age):
        self.age = age

class Brood(object):
    def __init__(self, age):
        self.age = age

#HERE IS A FUNCTION TO ADD WASPS TO THE NEST WOOO
def populate_nest(num, nest): #takes the argument num(ber of wasps to add) and the list nest
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
#below are the Queen and Nest classes

class Queen(object):
    mortality_rate = 10
    #egg_laying_rate - have a funciton instead for lay_egg
    def __init__(self, age, build_rate):
        self.age = age
        self.build_rate = build_rate
    def build_cell(): #takes 0 positional arguments, but 1 was given
        if nest.free_cell_count == 0:
            nest.total_cell_count += build_rate
            nest.free_cell_count += build_rate #remember to make sure that Queen only lays eggs when there is a complete cell
            

class Nest(object):
    max_cell_count = randint(34, 130) #maximum nest size from field data
    brood_list = []
    wasp_list = []
    current_cell_count = 0
    total_cell_count = 0
    free_cell_count = 0
    def __init__(self, species): 
        self.species = species
        if species == "Pd":
            build_options = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5]
            queen = Queen(0, choice(build_options)) #BUILD IN HAPLOMETROSIS AFTER PRELIMINARY MODEL IS RUNNING
            Nest.wasp_list.append(queen) 
        
#make the instance of the class Nest() named nest (lowercase n)
#pass_day():

#to sort a list of complex objects

#peepz = sorted(people, key=lambda person: person.age) #command is sorted(listname, key=lambda, 
    #for p in peepz:
        #print(p.name, p.age)
