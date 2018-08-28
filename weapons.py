class weapons(object):
    options = {1, 2}
    special = {3}
    wep = {
        1: {"Name": "Axe",
            "Description": "Rusty axe, low damage but high durability",
            'dam': 5,
            'cost': 25},
        2: {"Name":"Sword",
            "Description": "Weak Sharp blade, high damage",
            'dam': 10,
            'cost': 25},
        3: {"Name": "Enchanted Sword",
            "Description": "An odd purple glow comes from the sword",
            'dam': 15,
        }
    }

    def printOneItem(list):
        s = ""
        s += '\n{}'.format(list['Name'])
        s += "\n\t{}".format(list["Description"])
        s += "\n\tDamage: {}".format(list["dam"])
        return s

    def customPrint():
        s = ""
        for item in weapons.options:
            s += weapons.wep[item]["Name"]
            s += "\n\t{}".format(weapons.wep[item]["Description"])
            s += "\n\tDamage: {}".format(weapons.wep[item]["dam"])
            s += '\n\tCost: {}\n'.format(weapons.wep[item]['cost'])
        return s
