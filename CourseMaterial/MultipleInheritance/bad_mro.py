class Animal(object):
    def sleep(self):
        print "ZZZzzz"

class Squirrel(Animal):
    def sleep(self):
        print "zzzzz"

class SquirrelBear(Animal, Squirrel):
    def sleep(self):
        print "ZZZZZZ"
