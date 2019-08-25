from ogame import OGame
from ogame.constants import Ships, Speed, Missions, Buildings, Research, Defense

def log_in():
    return OGame('Indus', 'hotgigi82@hotmail.com', '1101982.Ogame')


def ship_slow_everything_to_Moons(n=9999):
    ships = [(Ships['LargeCargo'], n),(Ships['LightFighter'], n),(Ships['Cruiser'], n), (Ships['Recycler'], n), (Ships['Battleship'], n)]
    speed = Speed['50%']
    where_Mediaworld = {'galaxy': 1, 'system': 434, 'position': 10, 'type':3}
    where_Saturn = {'galaxy': 5, 'system': 432, 'position': 8, 'type':3}
    mission = Missions['Transport']
    for planet_name in ['Saturn','Amazon','Trony','Alibaba','Unieuro']:
        resources = {'metal': 999999999, 'crystal': 999999999, 'deuterium': 9999999999}
        ogame.send_fleet(ogame.get_planet_by_name(planet_name),
                         ships, 
                         speed, 
                         where_Mediaworld,
                         mission, 
                         resources)
    for planet_name in ['MediaWorld','Decathlon']:
        resources = {'metal': 999999999, 'crystal': 999999999, 'deuterium': 9999999999}
        ogame.send_fleet(ogame.get_planet_by_name(planet_name),
                         ships, 
                         speed, 
                         where_Saturn,
                         mission, 
                         resources)       


def ship_to_moon_from_moons(n=9999):
    ships = [(Ships['LargeCargo'], n) ,(Ships['LightFighter'], n), (Ships['EspionageProbe'], n),(Ships['Cruiser'], n), (Ships['Recycler'], n), (Ships['Battleship'], n)]
    speed = Speed['50%']
    where_Mediaworld = {'galaxy': 1, 'system': 434, 'position': 10, 'type':3}
    where_Saturn = {'galaxy': 5, 'system': 432, 'position': 8, 'type':3}
    mission = Missions['Park']
    resources = {'metal': 999999999, 'crystal': 999999999, 'deuterium': 9999999999}
    ogame.send_fleet(ogame.get_moon_ids()[1], ships, speed, where_Mediaworld, mission, resources) 
    ogame.send_fleet(ogame.get_moon_ids()[0], ships, speed, where_Saturn, mission, resources) 
 


if __name__=="__main__":    
    ogame = log_in()
    if ogame.is_under_attack():
        ship_to_moon_from_moons(n=9999)
        ship_slow_everything_to_Moons(n=9999)
        ogame.logout()
    else:
        ogame.logout()
