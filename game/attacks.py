class Attack:
    def __init__(self, MAX_DAMAGE, SUCCESS_RATE, damage_type):
        self.MAX_DAMAGE = MAX_DAMAGE
        self.SUCCESS_RATE = SUCCESS_RATE
        self.damage_type = damage_type


class EffectAttack(Attack):
    def __init__(self, MAX_DAMAGE, SUCCESS_RATE, damage_type, effect):
        self.effect = effect
       
        super().__init__(
                MAX_DAMAGE,
                SUCCESS_RATE,
                damage_type
                )


class Slash(EffectAttack):
    def __init__(self):
        super().__init__(
                MAX_DAMAGE=10,
                SUCCESS_RATE=0.8,
                damage_type="melee",
                effect="bleed"
                )


