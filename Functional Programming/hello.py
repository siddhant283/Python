
class PlayerCharacters:
    membership = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')
        return 'done'

    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Teddy',num1+num2)

    @staticmethod
    def adding_things2(num1,num2)
        return num1+num2    


player1 = PlayerCharacters('Cindy', 22)
player2 = PlayerCharacters('Tom', 44)
player3 = PlayerCharacters.adding_things(2,3)


print(player3.age)
