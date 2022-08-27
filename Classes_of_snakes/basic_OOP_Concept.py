# Fun Basic Intro to OOP By Japheth C
# Copy and Edit this Code, make it better, get creative.
#  for example add a name Instance add a helth method to check if he is alive etc
#  then Tag me or send to me

class Human:
  def __init__(self):
    self.head = "head"
    self.eyes = {"eye":2}
    self.mouth = "Closed"
    self.heart = {"rate":"Normal","Pains":None, "beating":True} 
    self.hands = {"arms":2,"condition":"Good"}
    self.stomach = None
    self.bowel = {"stool":0}
    self.bladder = {"piss":0}
    self.legs = {"speed":10,"condition":"Good"}
    self.race = "African"
    self.gender = "Female"
    self.age = 1
    self.car = {"car":"Bugatti","color":"black"}

  def eat(self,food):
    self.stomach = f"{food}"
    self.bowel[u"stool"] += 1 
    return(f"Thank you for the {food} it was good")

  def drink(self,drink):
    self.stomach = f"{drink}"
    self.bladder[u"piss"] = 1 
    return f"Drank {drink}"

  def stool(self):
    if self.bowel[u"stool"] <= 0:
        return "Bowels are empty"
    else:
        self.bowel[u"stool"] = 0
        self.stomach = None
        return "Thant Stinks, Eww"

  def piss(self):
    if not self.bladder[u"piss"] ==  'empty':
        self.bladder[u"piss"] = "empty"
        return "I was actually pressed, I needed to use the bathroom"
    else:
        return "Bladder is empty"
 
  def grow(self, years):
    self.age += years
    return f"{years} years later, I am now {self.age} years old"

  def How_are_you(self):
    state = ""
    if self.stomach != "Full":
        state = state + "I am Hungry"
    else: 
        state = state + "I am Fine"
    return state

  def what_color_is_your_car(self):
    color = self.car[u"color"]
    car = self.car[u"car"]
    return f"Mine is {color}, What about You, What Color is your {car} "


  def __repr__(self) -> str:
     return f"Breaths Air: I am Created my age is {self.age}, I have a bugatti and I am strong \nGet Creative with me"


# Andrew was created
Andrew = Human()
print(Andrew)
print("The Top G is born")

# We his creator asked him
print(Andrew.How_are_you())

# we gave him some food because he said he is hungry
print(Andrew.eat("Corn Flakes"))

# we gave him something to drink too 
print(Andrew.drink("Sparkling Water"))

# we want him to take a piss
print(Andrew.piss())

# we want him to take a stool
print(Andrew.stool())

# we want to make andrew grow older
print(Andrew.grow(10))

print(Andrew.what_color_is_your_car())
