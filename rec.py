class Human:
    def __init__(self):
        self.head = "head"
        self.eyes = {"eye":2}
        self.mouth = "closed"
        self.heart = {"rate":"normal","beating":True,"pains":None}
        self.hand = {"arms":2,"condition":"good"}
        self.stomach = None
        self.bowel = {"stool":0}
        self.bladder = {"piss":"empty"}
        self.legs = {"speed":10,"condition":"good"}
        self.race = "African"
        self.gender = "Female"
        self.age = 1
        self.car = {"car":"Bugatti","color":"black"}

    def eat(self,food):
        self.stomach = food
        self.bowel[U"stool"] += 1
        return (f"Thank You for the {food}, It was Good")

    def drink(self,drink):
        self.stomach = drink
        self.bladder[U"piss"] = 1
        return (f"Drank {drink}")

    def stool(self):
        if self.bowel[u"stool"] <= 0:
            return "Bowels are empty"
        else:
            self.bowel[u"stool"] = 0
            self.stomach = None
            return "That Stinks, Hmmmmmmn"
    def piss(self):
        if not self.bladder[u"piss"] == "empty":
            return "I was actually pressed after that drink, I needed to use the bathroom"
    def grow(self,years):
        self.age += years
        return f"{years} Years later, I am now {self.age} years Old"

    def how_are_you(self):
        state = str()
        if self.stomach != "Full":
            state = "I am Starving I need to eat"
            # add other possible situations here
        else:
            state = state + "I am fine"
        return state


    def what_color_is_your_car(self):
        color = self.car[u"color"]
        car = self.car[u"car"]
        return f"mine is {color}, What about you? what color is your {car}"
        

    def __repr__(self):
        return f"Breathes Air: I am created an Alpha {self.gender},\nI am {self.age} years old and I have a Bugatti "

andrew = Human()
# andrew is created 
print("Behold The Top G is Born")
print(andrew)

print(andrew.how_are_you())

print(andrew.eat("Cake"))
print(andrew.drink("Sparkling Water"))
# someone add a function for him to get drunk whem he takes wine

print(andrew.piss())
print(andrew.stool())
print(andrew.grow(30))
print(andrew.what_color_is_your_car())


# Signed Japheth 
# FREE TO USE 