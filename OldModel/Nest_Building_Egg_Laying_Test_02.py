#combining weather data with egg laying and nest building - getting a preliminary schedule of wasp activity together

from random import randint, choice, uniform

weather_data = {"1" : [0, 0, 0, 0, 0, 5, 0, 0, 0],#May 1st
                "2" : [0, 0, 0, 0, 1, 5, 0, 2, 5],
                "3" : [0, 0, 0, 0, 0, 3, 0, 5, 0],
                "4" : [0, 4, 0, 0, 0, 5, 0, 0, 0],
                "5" : [0, 5, 0, 2, 0, 5, 0, 0, 0],
                "6" : [0, 0, 0, 5, 0, 3, 0, 3, 0],
                "7" : [0, 0, 2, 5, 2, 3, 1, 2, 5],
                "8" : [0, 0, 5, 5, 5, 0, 0, 0, 2],
                "9" : [0, 0, 5, 0, 5, 0, 0, 1, 0],
                "10": [0, 0, 5, 0, 0, 0, 0, 0, 5],
                "11": [5, 0, 1, 0, 0, 0, 0, 0, 1],
                "12": [0, 0, 0, 0, 0, 0, 5, 0, 2],
                "13": [0, 0, 0, 2, 5, 2, 5, 0, 0],
                "14": [0, 0, 5, 1, 0, 1, 3, 0, 0],
                "15": [0, 0, 3, 0, 5, 4, 1, 0, 0],
                "16": [0, 0, 1, 0, 2, 5, 0, 0, 5],
                "17": [0, 0, 0, 4, 0, 5, 1, 0, 0],
                "18": [0, 0, 0, 3, 0, 0, 2, 0, 5],
                "19": [0, 0, 0, 0, 2, 0, 5, 0, 2],
                "20": [0, 0, 0, 0, 5, 5, 5, 0, 5],
                "21": [0, 0, 0, 1, 5, 5, 1, 5, 4],
                "22": [0, 0, 4, 0, 5, 5, 0, 0, 0],
                "23": [0, 0, 5, 2, 0, 5, 5, 0, 2],
                "24": [0, 1, 5, 0, 5, 5, 5, 5, 1],
                "25": [0, 5, 5, 5, 5, 5, 4, 5, 0],
                "26": [0, 5, 5, 5, 0, 5, 5, 5, 0],
                "27": [0, 2, 5, 3, 0, 5, 5, 5, 4],
                "28": [5, 5, 5, 0, 0, 5, 2, 5, 5],
                "29": [3, 5, 5, 5, 0, 4, 5, 5, 1],
                "30": [2, 5, 5, 4, 5, 5, 5, 5, 5],
                "31": [0, 5, 0, 0, 5, 5, 5, 5, 5],#May 31st
                "32": [0, 5, 4, 5, 2, 3, 5, 5, 5],#June 1st
                "33": [5, 0, 5, 5, 5, 5, 3, 0, 5],
                "34": [5, 0, 0, 5, 4, 5, 0, 0, 4],
                "35": [5, 0, 0, 0, 5, 5, 0, 0, 4],
                "36": [5, 0, 5, 0, 3, 5, 4, 0, 5],
                "37": [2, 5, 2, 0, 4, 2, 5, 0, 5],
                "38": [5, 0, 3, 5, 5, 5, 5, 4, 0],
                "39": [5, 0, 5, 5, 5, 4, 5, 3, 4],
                "40": [5, 0, 0, 5, 0, 4, 1, 5, 1],
                "41": [5, 0, 5, 5, 0, 0, 5, 5, 0],
                "42": [5, 0, 5, 5, 0, 0, 0, 5, 0],
                "43": [5, 5, 3, 5, 3, 0, 0, 5, 2],
                "44": [5, 5, 0, 5, 4, 0, 0, 0, 0],
                "45": [4, 2, 0, 5, 0, 5, 0, 5, 2],
                "46": [0, 5, 5, 0, 0, 5, 5, 5, 5],
                "47": [0, 5, 4, 0, 3, 5, 5, 0, 5],
                "48": [3, 5, 4, 5, 5, 5, 2, 1, 2],
                "49": [0, 5, 5, 4, 1, 5, 4, 3, 3],
                "50": [0, 5, 5, 5, 3, 5, 5, 5, 5],
                "51": [5, 4, 3, 4, 5, 4, 5, 5, 5],
                "52": [5, 5, 5, 5, 0, 5, 5, 5, 5],
                "53": [0, 5, 3, 2, 0, 5, 0, 5, 0],
                "54": [4, 3, 4, 0, 0, 5, 0, 5, 1],
                "55": [5, 1, 5, 3, 0, 5, 0, 5, 4],
                "56": [5, 2, 5, 5, 5, 5, 0, 1, 5],
                "57": [5, 3, 5, 3, 3, 5, 5, 5, 5],
                "58": [5, 5, 5, 2, 5, 4, 5, 5, 5],
                "59": [2, 0, 5, 5, 1, 5, 5, 5, 5],
                "60": [3, 4, 5, 4, 4, 5, 5, 5, 5],
                "61": [5, 5, 5, 5, 2, 5, 5, 5, 5],#June 30th
                "62": [4, 5, 4, 5, 0, 5, 5, 5, 2],#July 1st
                "63": [5, 4, 4, 1, 1, 5, 5, 4, 5],
                "64": [5, 4, 4, 1, 1, 5, 5, 4, 5],
                "65": [5, 5, 5, 5, 5, 5, 5, 5, 5],
                "66": [5, 4, 5, 2, 5, 5, 5, 5, 5],
                "67": [0, 5, 4, 5, 5, 5, 5, 5, 5],
                "68": [0, 5, 5, 5, 2, 5, 5, 3, 5],
                "69": [0, 5, 4, 5, 0, 5, 5, 5, 5],
                "70": [5, 5, 4, 5, 0, 5, 5, 5, 5],
                "71": [5, 5, 5, 5, 5, 2, 5, 5, 5],
                "72": [5, 2, 5, 5, 5, 5, 5, 5, 4],
                "73": [5, 4, 5, 5, 5, 4, 5, 5, 5],
                "74": [5, 2, 5, 5, 5, 5, 4, 5, 5],
                "75": [5, 5, 5, 5, 5, 1, 5, 5, 5],
                "76": [5, 5, 5, 5, 5, 5, 5, 5, 5],
                "77": [5, 5, 5, 5, 5, 5, 5, 5, 5],
                "78": [5, 5, 5, 5, 5, 5, 5, 5, 5],
                "79": [5, 5, 1, 5, 5, 5, 1, 3, 5],
                "80": [5, 5, 4, 5, 5, 5, 5, 5, 5],
                "81": [5, 5, 5, 3, 5, 5, 5, 5, 4],
                "82": [5, 5, 5, 4, 0, 5, 5, 5, 5],
                "83": [5, 2, 5, 5, 5, 5, 5, 5, 5],
                "84": [5, 4, 1, 1, 2, 2, 5, 5, 2],
                "85": [5, 5, 5, 1, 2, 5, 5, 3, 5],
                "86": [5, 5, 5, 5, 5, 5, 5, 5, 0],
                "87": [5, 5, 5, 5, 5, 5, 5, 5, 1],
                "88": [5, 5, 5, 4, 5, 5, 5, 1, 5],
                "89": [5, 5, 1, 5, 5, 5, 5, 5, 5],
                "90": [5, 5, 5, 5, 5, 5, 4, 4, 5],
                "91": [5, 5, 4, 5, 5, 5, 5, 5, 5],
                "92": [2, 5, 5, 5, 0, 5, 5, 5, 4],#July 31st
                "93": [5, 5, 5, 5, 5, 5, 5, 4, 5],#August 1st
                "94": [5, 5, 5, 4, 4, 5, 5, 5, 5],
                "95": [5, 5, 5, 3, 5, 5, 5, 5, 5],
                "96": [5, 4, 5, 5, 5, 5, 5, 5, 4],
                "97": [5, 5, 5, 5, 5, 5, 5, 5, 5],
                "98": [5, 5, 1, 1, 0, 5, 5, 5, 5],
                "99": [5, 5, 5, 3, 5, 5, 1, 5, 4],
                "100":[5, 5, 5, 5, 5, 4, 4, 5, 5],
                "101":[5, 5, 5, 5, 5, 5, 5, 5, 0],
                "102":[5, 5, 1, 5, 5, 5, 5, 4, 5],
                "103":[5, 5, 4, 4, 1, 5, 5, 5, 3],
                "104":[5, 5, 3, 4, 4, 5, 4, 4, 5],
                "105":[5, 5, 2, 5, 3, 5, 5, 5, 2],
                "106":[4, 5, 4, 3, 5, 5, 3, 4, 5],
                "107":[0, 4, 5, 5, 5, 5, 0, 5, 5],
                "108":[5, 5, 5, 3, 5, 5, 0, 5, 5],
                "109":[5, 5, 5, 5, 5, 5, 5, 5, 5],
                "110":[5, 5, 5, 5, 5, 5, 4, 5, 5],
                "111":[5, 5, 5, 3, 4, 5, 4, 5, 5],
                "112":[5, 4, 5, 5, 5, 5, 5, 5, 5],
                "113":[4, 5, 5, 5, 5, 5, 3, 5, 5],
                "114":[5, 5, 5, 5, 3, 0, 5, 4, 5],
                "115":[5, 5, 5, 5, 5, 0, 5, 5, 5],
                "116":[4, 5, 5, 5, 3, 0, 5, 5, 5],
                "117":[5, 0, 5, 5, 5, 0, 4, 5, 5],
                "118":[5, 4, 4, 5, 5, 5, 5, 5, 5],
                "119":[5 ,1, 5, 5, 5, 5, 3, 5, 5],
                "120":[4, 3, 5, 5, 5, 5, 0, 5, 5],
                "121":[5, 0, 5, 0, 0, 5, 5, 5, 0],
                "122":[0, 5, 5, 5, 5, 5, 5, 5, 5],
                "123":[4, 5, 5, 3, 5, 5, 5, 5, 4]}

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
    #def feed(self, food_need, status): #if status = "larvae", b/c they're the only ones who eat
    def metamorphose(self, age):
        for b in nest.brood_list:
            if 11 <= b.age < 27:
                self.dev_stage = "larvae"
            if 27 <= b.age < 40:
                self.dev_stage = "pupae"
            if b.age == 40: #this will later have to break down into reproductives or workers at the end of the colony cycle
                sorted(nest.brood_list, key=lambda b:b.age) #Am I doing this right? I want to sort the brood by age, so I can put the oldest brood (the ones turning 40 who will metamorphose) at the end and then pop them out of the list
                w = Worker(40, "alive")
                nest.worker_list.append(w)
                nest.brood_list.pop()#but is there a way that I can remove the 40-day brood, specifically? I want to make sure this takes off as many brood at the end of the list that are at age 40
                

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
        while nest.free_cell_count >= round(1, 0): #while there is at least 1 empty cell (round makes sure wasp doesn't lay in incomplete cell)
            b = Brood(0, "need", "egg", "alive") 
            nest.brood_list.append(b) #add a brood b to nest.brood_list with the above arguments
            nest.free_cell_count -= 1 #subtract 1 free cell from the nest for each egg laid

class Worker(object):
    mortality_rate = 10 #in daily_mortality function, random number generate (0, 100), if randint < mortality_rate then wasp dies
    def __init__(self, age, alive):
        self.age = age

day_count = 0 #set count to 0 outside while block
nest = Nest("Pd")
queen = Queen(40, "build", "mass")
print("Max nest size =", nest.max_cell_count)
print("Queen's build rate =", queen.build_rate)

while day_count < 20:
    day_count += 1 #increment by day - put increment at top because "1" = first key in dictionary, and day_count = 0 outside loop
    weather_key = str(day_count) #turn day_count into a string to use as a key in the weather_dict
    print("--- DAY", weather_key, "---")
    print("Queen builds:")
    queen.build_cell() #run queen's cell building method
    print("Free cells =", round(nest.free_cell_count, 1)) #show how many free cells there are, rounded to 1 decimal place (same sig. fig. as build rate)
    print("Queen lays egg(s):")
    queen.lay_egg() #run queen's egg laying method
    print("# brood start:", len(nest.brood_list))
    print("# workers:", len(nest.worker_list))
    print("Free cells remaining =", round(nest.free_cell_count, 1))
    print("Foraging + Hours:", choice(weather_data[weather_key]))
    for b in nest.brood_list:
        b.age += 1
        b.metamorphose(b.age)
        print(b.age)
    print("# brood after metamorph:", len(nest.brood_list))
