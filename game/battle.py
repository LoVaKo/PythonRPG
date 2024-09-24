import random
from characters import Knight, Goblin

class Battle:

    def set_character_order(self):
        all_characters = self.party_1 + self.party_2
        self.character_order = sorted(all_characters, key=lambda x: random.random())
    
    def battle_report(self):
        for character in self.character_order:
            print(f"{character.name} | {character.current_hp}/{character.MAX_HP}")

    def __init__(self, party_1, party_2):
        self.party_1 = party_1
        self.party_2 = party_2
        self.character_order = [] 
        self.is_active = True
    
    def remove_dead_characters(party):
        living_characters = []

        for character in party:
            if character.is_alive: 
                living_characters.append(character)
        party = living_characters

    def check_for_end(self):
        if len(self.party_1) == 0 and len(self.party_2) > 0:
             print("Party 2 won the game")
             self.is_active = False
        
        if len(self.party_1) > 0 and len(self.party2) == 0:
             print("Party 1 won the game")
             self.is_active = False

        if len(self.party_1) == 0 and len(self.party2) == 0: 
             print("Everyone is dead!")
             self.is_active = False


    def update_parties(self):
        remove_dead_characters(party_1)
        remove_dead_characters(party_2)
        

    def commence(self):
        while self.is_active:
            #  Start of round
            self.set_character_order()
            
            for character in self.character_order:
                #  Start of character turn
                if character.is_dead: continue
                self.battle_report()

                if character in self.party_1:
                    pass
                else:
                    pass
            
            #  End round
            self.update_parties()
            self.check_for_end()


hero = Knight("Hero")
villain = Goblin("Villain")

heroes = [hero]
villains = [villain]
battle = Battle(heroes, villains)
battle.commence()
