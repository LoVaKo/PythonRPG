from gearhandler import GearHandler

class Character:
    gear_handler = GearHandler()
    inventory = []
    effects = []
    is_dead = False

   
    def __init__(self, name, attack_1, MAX_HP):
        self.name = name
        self.attack_1 = attack_1
        self.MAX_HP = MAX_HP
        self.current_hp = MAX_HP


class Knight(Character):

    def __init__(self, name):
        super().__init__(
            name=name,
            attack_1="Slash", 
            MAX_HP=50
            )

class Goblin(Character):

    def __init__(self, name): 
        super().__init__(
                name=name,
                attack_1="Slash",
                MAX_HP=25
                )

