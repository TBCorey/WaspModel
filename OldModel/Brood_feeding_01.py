#feeding time! feeding time! Blood and guts and feeding time.
#Brood feeding program - how much do they need to eat, and in how much time? That is the question.

from random import randint, choice, uniform

class Nest(object):
    max_cell_count = 9999 #maximum nest size from field data is randint(34, 130), changing to super high so the limit comes from behavior and not a predetermined value
    brood_list = []
    worker_list = []
    repro_list = [] #list for reproductives, which do not forage for the nest (but do they still go kill caterpillars?)
    total_cell_count = 0 #removed current_cell_count - that's the same as the present total!
    free_cell_count = 0
    def __init__(self, species): 
        self.species = species

#Brood class definition
class Brood(object):
    def __init__(self, age, food_need, dev_stage, status):
        self.age = age
        self.food_need = 0.0278 #food need could be calculated as: 1. total need to pupate, subtract from each day, 2. daily need that always increases, if reach threshold, dies
        self.dev_stage = dev_stage #egg, larvae, or pupae
        self.status = status
    #def feed(self, food_need, status): #if status = "larvae", b/c they're the only ones who eat
    def mortality(self):
        if randint(1,100) <= 5:
            nest.brood_list.remove(b)
            print("A brood has died!")
            nest.free_cell_count += 1
    def metamorphose(self, age):
        for b in nest.brood_list:
            if 11 <= b.age < 27: #whiteboard dump from summer had 94.4% survival rate for larvae - is this from 5.6% mortality rate?
                b.dev_stage = "larvae"
            if 27 <= b.age < 40:
                b.dev_stage = "pupae"
            if b.age == 40: #this will later have to break down into reproductives or workers at the end of the colony cycle
#possibly used sorted() here if need be: I want to sort the brood by age, so I can put the oldest brood (the ones turning 40 who will metamorphose) at the end and then pop them out of the list
                w = Worker(40, "alive") #will also want some kind of eclosion success rate here perhaps? if not some value, then brood dies rather than becomes worker?
                nest.worker_list.append(w)
                nest.brood_list.remove(b)#but is there a way that I can remove the 40-day brood, specifically? I want to make sure this takes off as many brood at the end of the list that are at age 40
                nest.free_cell_count += 1
    def feed(self):
        global flesh_gathered_today
        if self.food_need > 0 and flesh_gathered_today > 0:#if the larvae has a food need
            flesh_gathered_today = flesh_gathered_today - self.food_need #but what if flesh_gathered_today - food_need is negative?
            self.food_need -= self.food_need
        if self.food_need > 0 and flesh_gathered_today - self.food_need < 0:#if food need is greater than flesh supply
            self.food_need -= flesh_gathered_today #take what is left of the flesh gathered
            flesh_gathered_today = 0 #reduce flesh_gathered_today to 0 (no flesh is left)
        if flesh_gathered_today == 0: #if no flesh is gathered or left, do nothing
            pass
                
        

#Remember that chinensis is a very different size than dominulus! (about 10x bigger)
#so the amount of flesh needed to be consumed during the larval stage is going to be different
#Suzuki 1980 - flesh intake and the production of workers - efficiency of flesh conversion = 73%
#So should the assumption be mass of a worker is 73% of the food given

nest = Nest("Pd") #Make a nest
b = Brood(11, "need", "egg", "alive") #make a brood

nest.brood_list.append(b) #add brood to brood list
flesh_gathered_today = 0.5 #set flesh gathered today


for b in nest.brood_list:
    print("Flesh gathered:", flesh_gathered_today)
    print("Food need:", b.food_need)
    b.feed()
    print("Eat, now needs:", b.food_need)
    print("Flesh left:", flesh_gathered_today)

b.hunger
for b in nest.brood_list:
    print(flesh_gathered_today)
    print(b.food_need)
    b.feed()
    print(b.food_need)
    print(flesh_gathered_today)

####THOUGHTS FOR FIGURING OUT THE ABOVE
    #Okay, so the food need for the larvae over ALL its development is 0.0278 g DRY WEIGHT!!!!
    #Is that really one prey ball? I don't think that can make sense, pretty much.
    #Maybe we just have to say this is for chinensis? Maybe I can code it as chinensis presently and change it later when i'm more sure
    #So according to Suzuki (1980), the dry weight avg. of foundress pellets is 0.0031 g, and 0.0033 g for workers
        #interesting that foundress payload is lower than workers... but could this be due to small sample size? (n = 9)
    #But anyway, 0.0031 g means about 9 prey balls are needed to get a larvae to develop (0.0278/0.0031 = 8.967)
    #Wait! Don't forget to multiply by 90%, because 10% of prey are re-used: so 8.967*0.9 = 8.07, so 8 caterpillars over ~17 days
        #Okay, that's about 1 caterpillar every other day. Given how many brood are on the nest, and foraging conditions early in
        #the season are not the best, that might be reasonable. Also factor in oophagy and cannibalism! So now to code this business.
