from random import choice, randint #two random functions i'm using at the moment
#below, build_options, are the possible rates of cell building (cell/day) that a Queen could have
    #i'm not entirely sure where to put it in the Queen class
build_options = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5]
#FROM MATT - Look at how you included the max_cell_count, brood_list, wasp_list, etc. in the Nest
#            class. Why couldn't you just do the same with this in the Queen class?


#below are the Queen and Nest classes

class Queen(object):
    mortality_rate = 10
    def __init__(self, age, build_rate):
        self.age = age
        self.build_rate = build_rate #but I want build_rate to a random number from build_options
                                     #how can I get this without having to input it when generating an instance?

                                     #FROM MATT - If you put the build_options inside of the Queen class, then
                                     #            you could just set self.build_rate to choice(self.build_options)

    def build_cell(): #takes 0 positional arguments, but 1 was given
                      #FROM MATT - every class method needs to accept self as the first parameter, otherwise you 
                      #            wouldn't ever be able to access the member variables of the instance. You
                      #            don't pass it in, but it is implicitly passed (so you need to accept it as a param)
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
                                                    #FROM MATT - I'm curious to see if doing the other changes does anything to this, but queen is also a local variable, so
                                                    #            when you leave this function, the reference (and therefore the name) is deleted. You should be able to make
                                                    #            the queen object and then immediately access its data, however, so I'm not totally sure what the problem is.
                                                    #            Can you leave the code that is causing that error in next time and comment it out?
            Nest.wasp_list.append(queen) #this does, however, successfully add a Queen object to wasp_list

nest = Nest("Pd") #This makes an instance of Nest, with a Queen instance in wasp_list
#However, if I try to call anything involving queen, I get a NameError saying that 'queen' is not defined

#FROM MATT - that's because the queen object was placed in the wasp_list, and therefore loses the name associated with it since
#            lists do not have names associated with the internal objects. If you want to be able to single out the queen, you could
#            have the queen be a member variable of the Nest class (and then set it to self.queen). You could then access the queen
#            object by classing nest.queen (note that you get the queen object from the nest instance and not the Nest class)

#Test code below? I would either run this and add code, or plug the above into interactive mode and mess around there
