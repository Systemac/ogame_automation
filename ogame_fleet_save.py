from ogame import OGame
from ogame.constants import Ships, Speed, Missions, Buildings, Research, Defense

def log_in():
    return OGame('Indus', 'hotgigi82@hotmail.com', '1101982.Ogame')

def ship_to_moon_from_moons(n=9999):
    ships = [(Ships['LargeCargo'], n) ,(Ships['LightFighter'], n), (Ships['EspionageProbe'], n),(Ships['Cruiser'], n), (Ships['Recycler'], n), (Ships['Battleship'], n),
    (Ships['Destroyer'], n),(Ships['Bomber'], n),(Ships['Battlecruiser'], n)]
    speed = Speed['10%']
    where_Mediaworld = {'galaxy': 1, 'system': 434, 'position': 10, 'type':3}
    where_Saturn = {'galaxy': 5, 'system': 432, 'position': 8, 'type':3}
    where_Decathlon = {'galaxy': 1, 'system': 435, 'position': 8, 'type':3}
    mission = Missions['Park']
    resources = {'metal': 999999999, 'crystal': 999999999, 'deuterium': 9999999999}
    ogame.send_fleet(ogame.get_moon_ids()[1], ships, speed, where_Decathlon, mission, resources)
    ogame.send_fleet(ogame.get_moon_ids()[2], ships, speed, where_Saturn, mission, resources)



if __name__=="__main__":
    ogame = log_in()
    ship_to_moon_from_moons(n=9999)
    ogame.logout()
