from random import choice, randint #two random functions i'm using at the moment
#below, build_options, are the possible rates of cell building (cell/day) that a Queen could have
    #i'm not entirely sure where to put it in the Queen class
build_options = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5]

#below are the Queen and Nest classes

class Queen(object):
    mortality_rate = 10
    def __init__(self, age, build_rate):
        self.age = age
        self.build_rate = build_rate #but I want build_rate to a random number from build_options
                                     #how can I get this without having to input it when generating an instance?
    def build_cell(): #takes 0 positional arguments, but 1 was given
        if nest.free_cell_count == 0:
            nest.total_cell_count += build_rate
            nest.free_cell_count += build_rate #remember to make sure that Queen only lays eggs when there is a complete cell
    #def lay_egg(): need to figure out still

class Nest(object):
    max_cell_count = randint(34, 130) #maximum nest size from field data
    brood_list = []
    wasp_list = []
    current_cell_count = 0
    total_cell_count = 0
    free_cell_count = 0
    def __init__(self, species): 
        self.species = species
        if species == "Pd": #"Pd" is shorthand for Polistes dominulus, the invasive wasp species (ideally, eventually, the model may work for multiple Polistes wasp species)
            build_options = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5]
            queen = Queen(0, choice(build_options)) #but when I do this, if I try to print queen.attribute or call queen.method, it says that the name 'queen' is not defined
            Nest.wasp_list.append(queen) #this does, however, successfully add a Queen object to wasp_list

nest = Nest("Pd") #This makes an instance of Nest, with a Queen instance in wasp_list
#However, if I try to call anything involving queen, I get a NameError saying that 'queen' is not defined

#Test code below? I would either run this and add code, or plug the above into interactive mode and mess around there
