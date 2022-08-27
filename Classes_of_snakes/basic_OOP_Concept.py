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
    self.legs = {"speed":10}
    self.race = None
    self.gender = None
    self.age = None

  def eat(self,food):
    self.stomach = f"Food"
    self.bowel += 1 

  def stool(self):
    if self.bowel[u"stool"] <= 0:
        return "Bowels are empty"
    else:
        self.bowel[u"stool"] = 0
        self.stomach = None

  def piss(self):
    if not self.bladder[u"piss"] ==  'empty':
        self.bladder[u"piss"] = "empty"
    else:
        return "Bladder is empty"
 
  def grow(self, years):
    self.age += years

  def How_are_you(self):
    state = None
    if self.stomach != "Full":
        state = state + "I am Hungry"
    else: 
        return "I am Fine"


  
