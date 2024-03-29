from player import Player

class Action():
    def __init__(self, method, name, hotkey, **kwargs):
        self.method = method
        self.name = name
        self.hotkey = hotkey
        self.kwargs = kwargs

    def __str__(self):
        return "{}: {}".format(self.hotkey, self.name)

class MoveNorth(Action):
    def __init__(self):
        super().__init__(method=Player.move_north, name="Move north", hotkey="n")

class MoveSouth(Action):
    def __init__(self):
        super().__init__(method=Player.move_south, name="Move south", hotkey="s")

class MoveEast(Action):
    def __init__(self):
        super().__init__(method=Player.move_east, name="Move east", hotkey="e")

class MoveWest(Action):
    def __init__(self):
        super().__init__(method=Player.move_west, name="Move west", hotkey="w")

class ViewInventory(Action):
    #Prints the player's inventory
    def __init__(self):
        super().__init__(method=Player.print_inventory, name="View inventory", hotkey="i")

class Attack(Action):
    #UNUSED CODE, KEPT FOR REFERENCE
    #def __init__(self, enemy):
        #super().__init__(method=Player.attack, name="Attack", hotkey="a", enemy=enemy)
    def __init__(self):
        super().__init__(method=Player.attack, name="Attack", hotkey="a")

class Flee(Action):
    def __init__(self, tile):
        super().__init__(method=Player.flee, name="Flee", hotkey="f", tile=tile)

class Heal(Action):
    def __init__(self):
        super().__init__(method=Player.heal, name="Heal", hotkey="h")