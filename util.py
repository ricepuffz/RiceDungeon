from random import Random

random = Random()


def parse_damage_string(string):
    parts = string.split("d")
    dice_amount = int(parts[0])
    dice_pips = int(parts[1])

    result = 0

    for i in range(dice_amount):
        result += random.randint(1, dice_pips)

    return result
