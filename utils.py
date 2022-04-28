from flask import request

from equipment import Equipment
from hero_classes import unit_classes
from unit import PlayerUnit, EnemyUnit, BaseUnit


def get_data_for_choosing(hero=False) -> dict:
    classes = unit_classes
    weapons = Equipment().get_weapons_names()
    armors = Equipment().get_armors_names()
    data = {
        "classes": classes,
        "weapons": weapons,
        "armors": armors,
    }
    if hero:
        header = 'Выберите героя'
        data['header'] = header
    header = 'Выберите врага'
    data['header'] = header
    return data

def get_unit_from_form(hero=False) -> BaseUnit:
    name = request.form['name']
    armor_name = request.form['armor']
    weapon_name = request.form['weapon']
    unit_class = request.form['unit_class']
    if hero:
        player = PlayerUnit(name=name, unit_class=unit_classes.get(unit_class))
        player.equip_weapon(Equipment().get_weapon(weapon_name))
        player.equip_armor(Equipment().get_armor(armor_name))
        return player
    enemy = EnemyUnit(name=name, unit_class=unit_classes.get(unit_class))
    enemy.equip_weapon(Equipment().get_weapon(weapon_name))
    enemy.equip_armor(Equipment().get_armor(armor_name))
    return enemy
