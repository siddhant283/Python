class User():
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')

    def attack(self):
        print("do nothing")


class wizards(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows left: {self.num_arrows}')

    def run(self):
        print("ran really fast")

class HybridBorg(wizards,Archer):
    def __init__(self,name,power,arrows):
        Archer.__init__(self,name,arrows)
        wizards.__init__(self,name,power)

    def attack(self):
        Archer.attack(self)    

wizard1 = wizards('Merlin', 50)
archer1 = Archer('Robin', 100)

hb1 = HybridBorg('Borgies',99,124)

print(hb1.attack())
