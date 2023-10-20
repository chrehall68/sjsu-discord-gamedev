from discord.ext import commands
import discord

class Tile:
    def __init__(self, x, y) -> None:
        self.village = None
        self.armies = set()
        self.owner = None
        self.x = x
        self.y = y

    def display(self) -> str:
        if self.village is not None:
            return ":homes:"
        elif len(self.armies) > 0:
            return ":crossed_swords:"
        else:
            return ":green_square:"
        
    def claim(self, id) -> None:
        self.owner = id
    
    def description(self, bot) -> str:
        user = None
        if self.owner is not None:
            user = bot.get_user(self.owner)
        desc = ""
        if user is not None:
            desc = f"Owner: {user.display_name}"
        else:
            desc = f"Unclaimed tile"
        if self.village is not None:
            desc += f"\nVillage: {self.village.type} | Level: {self.village.level}"
        if len(self.armies) > 0:
            desc += f"\nArmies: "
            desc += "\n".join(map(lambda army: army.description(), self.armies))
        return desc
        
class Village:
    def __init__(self, tile, type, baseLevel = 1) -> None:
        self.level = baseLevel
        self.tile = tile
        self.type = type
    
    def upgrade(self) -> None:
        self.level += 1
    
    def spawnArmy(self) -> None:
        if len(self.tile.armies) < 3:
            self.tile.armies.add(Army(self.level))

class Army:
    def __init__(self, attackPower) -> None:
        self.power = attackPower

    def description(self) -> str:
        desc = f"Army | Power {self.power}"
        return desc