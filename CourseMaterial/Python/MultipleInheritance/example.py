class Animal(object):
    fur = True
    tail = "short"

    def sleep(self):
        print "ZZZzzzz"
    
    def eat(self):
        print "Already in mouth"

class Bear(Animal):
    fat = True

    def sleep(self,season):
        if season == "Winter":
            super(Bear,self).sleep()
        else:
            print "Must. Find. Food."

    def make_noise(self):
        print "RAAWWR"

class Squirrel(Animal):
    tail = "long"

    def eat(self):
        print "Is it an acorn?"

    def make_noise(self):
        print "Chirp"

class SquirrelBear(Bear,Squirrel):
    pass



