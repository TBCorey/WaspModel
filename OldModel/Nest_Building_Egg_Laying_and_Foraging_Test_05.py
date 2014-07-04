#combining weather data with egg laying and nest building - getting a preliminary schedule of wasp activity together
#Ver 02 - building in worker mortality (18% chance/worker/day, brood at first at 7% chance/brood/day), changed to 0.3% chance/brood day
#Ver 03 - removing max cell limit - see if it winds up being in range at carlisle (which is randint 34, 130)
    #The workers need a build method! That's why the nests are consistently smaller than max size in runs.
        #So I've added the build_cell() method to the workers too with their own rate
#Ver 04 - main() function of bulk of model to run a bunch of times (how it should/will be eventually, but not yet)
#Ver 05 - Try adding another build command in each routine so foundress builds more? She does throughout the day?
    #Tried in no_print_mult_run file, didn't change things much in terms of nest size,  build rate/rules should probably change
    #Fixing __init__ functions (taking out unnceccesary arguments)
#Ver 06 - making an actual foraging function for queen and workers

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
    #maximum nest size from field data is randint(34, 130), changing to super high so the limit comes from behavior and not a predetermined value
    brood_list = []
    worker_list = []
    repro_list = [] #list for reproductives, which do not forage for the nest (but do they still go kill caterpillars?)
    total_cell_count = 0 #removed current_cell_count - that's the same as the present total!
    free_cell_count = 0
    def __init__(self, species): 
        self.species = species

class Queen(object):
    mortality_rate = 10
    build_options = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5]
    def __init__(self, age, status):
        self.age = age
        self.build_rate = choice(self.build_options)
        self.mass = round(uniform(0.086, 0.114), 3) #important to compare to usurper, mean = 0.10 g +/- SE 0.002g, n = 48, so SD is +/- 0.014
        self.death_date = randint(61, 113)
        self.status = status
    def build_cell(self):
        if nest.free_cell_count < 1 and self.status == "alive":
            nest.total_cell_count += self.build_rate
            nest.free_cell_count += self.build_rate #remember to make sure that Queen only lays eggs when there is a complete cell
        if self.status == "dead":
           pass
    def lay_egg(self):
        while nest.free_cell_count >= round(1, 0) and self.status == "alive": #while there is at least 1 empty cell (round makes sure wasp doesn't lay in incomplete cell)
            b = Brood(0, "egg", "alive") 
            nest.brood_list.append(b) #add a brood b to nest.brood_list with the above arguments
            nest.free_cell_count -= 1 #subtract 1 free cell from the nest for each egg laid
    def death(self): #queen longevity is 87 +/- 26 days (Gamboa 2002)
        if self.death_date == self.age:
            print("THE QUEEN IS DEAD!")
            self.status = "dead"

class Brood(object):
    def __init__(self, age, dev_stage, status):
        self.age = age
        self.food_need = 0 #food need could be calculated as: 1. total need to pupate, subtract from each day, 2. daily need that always increases, if reach threshold, dies
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
#pssibly used sorted() here if need be: I want to sort the brood by age, so I can put the oldest brood (the ones turning 40 who will metamorphose) at the end and then pop them out of the list
                w = Worker(40) #will also want some kind of eclosion success rate here perhaps? if not some value, then brood dies rather than becomes worker?
                nest.worker_list.append(w)
                nest.brood_list.remove(b)#but is there a way that I can remove the 40-day brood, specifically? I want to make sure this takes off as many brood at the end of the list that are at age 40
                nest.free_cell_count += 1               

class Worker(object):
    mortality_rate = 10 #in daily_mortality function, random number generate (0, 100), if randint < mortality_rate then wasp dies
    def __init__(self, age):
        self.age = age
    def mortality(self):
        if randint(1, 100) <= 19:#whiteboard over summer had 81% chance for worker to return to nest - double check this? Seems high. But hey, predation.
            nest.worker_list.remove(w)
            print("A worker has died!")

#START OF INSTANCES AND WHILE LOOP (THE MODEL ITSELF)
    
day_count = 0 #set count to 0 outside while block
total_caterpillars_killed = 0 #initial total at start = 0, so we can increment
total_flesh_gathered = 0
nest = Nest("Pd") #generate the instance of the nest
queen = Queen(0, "alive") #can build in haplometrosis eventually by having two queens, queen_a and queen_b, called via a random number generator based on frequency of multiple foundress nesting
#removed max_nest_size
print("Queen's build rate =", queen.build_rate)
print("Queen will live to be", queen.death_date, "days old")

while day_count < 20:
    day_count += 1 #increment by day - put increment at top because "1" = first key in dictionary, and day_count = 0 outside loop
    weather_key = str(day_count) #turn day_count into a string to use as a key in the weather_dict
    print("--- DAY", weather_key, "---")
    print("Queen builds:")
    queen.build_cell() #run queen's cell building method
    print("Free cells =", round(nest.free_cell_count, 1)) #show how many free cells there are, rounded to 1 decimal place (same sig. fig. as build rate)
    print("Queen lays egg(s):")
    queen.lay_egg() #run queen's egg laying method
    print("Free cells remaining =", round(nest.free_cell_count, 1)) #rounding to eliminate excessive decimal places
    date_foraging_hours = choice(weather_data[weather_key]) #foraging hours for a day is a random choice from the list for each date in the weather dictionary
    print("Foraging + Hours:", date_foraging_hours) 
    if len(nest.worker_list) == 0 and queen.status == "alive": #if there are no workers and the queen's alive, she forages
        print("Queen forages:")
        caterpillars_killed_today = 0.665*(date_foraging_hours)
        flesh_gathered_today = caterpillars_killed_today*0.0173 #0.0173 is queen's average payload capacity
    elif len(nest.worker_list) == 0 and queen.status == "dead":
        print("Queen is dead!")
        caterpillars_killed_today = 0
        flesh_gathered_today = 0
    elif len(nest.worker_list) >= 1:
        print(len(nest.worker_list), "workers forage:")
        caterpillars_killed_today = 0.665*(len(nest.worker_list))*(date_foraging_hours) #multiply murder constant by # workers and # foraging + hours
        flesh_gathered_today = caterpillars_killed_today*0.014 #0.014 is worker's average payload capacity
    print("Leps killed today =", caterpillars_killed_today)
    print("Flesh gathered today =", flesh_gathered_today)
    total_caterpillars_killed += caterpillars_killed_today
    total_flesh_gathered += flesh_gathered_today
    print("Total kills =", total_caterpillars_killed)
    print("Total flesh =", total_flesh_gathered)
    print("End of day - wasps age, workers eclose:")
    for w in nest.worker_list: #age workers first so a brood doesn't age, metamorphose, and then age again as worker
        w.age += 1
    print("Brood List:", len(nest.brood_list), "in total")
    for b in nest.brood_list:
        b.age += 1
        b.metamorphose(b.age)
    #for b in nest.brood_list: #maybe breaking this up will get rid of the whole 40-day pupae thing?
        #print(b.age, b.dev_stage)
    print("Worker List:", len(nest.worker_list), "in total")
    #for w in nest.worker_list:
    #   print(w.age)
    for b in nest.brood_list:
        b.mortality()
    for w in nest.worker_list:
        w.mortality()
    queen.age += 1
    print("# brood after metamorph:", len(nest.brood_list))
    queen.death()

print("Final cell count:", nest.total_cell_count)

#Add a total count of all brood and workers produced over the course of the cycle to use as a check to see how many died as a result of
#emergent behavior in model compared to expected amount (i.e. 5.6% of total brood dead at end of summer)
