from ogame import OGame
from ogame.constants import Ships, Speed, Missions, Buildings, Research, Defense, Facilities

ogame = OGame("Indus", "hotgigi82@hotmail.com", "1101982.Ogame")

planets = ['Saturn','Amazon','Trony','Alibaba','Unieuro','MediaWorld','Decathlon','Ikea']

def check_fleet():
    for planet in planets:
        planet_id = ogame.get_planet_by_name(planet)
        if ogame.get_ships(planet_id)['large_cargo'] < 50:
            ogame.build(planet_id,(Ships['LargeCargo'], 50))

def ship_everything_to_Void(n=999):
    ships = [(Ships['LargeCargo'], n)]
    speed = Speed['100%']
    where_Void = {'galaxy': 2, 'system': 476, 'position': 9, 'type':3}
    mission = Missions['Transport']
    for planet in planets:
        resources = {'metal': 999999999, 'crystal': 999999999, 'deuterium': 9999999999}
        ogame.send_fleet(ogame.get_planet_by_name(planet),
                         ships, 
                         speed, 
                         where_Decathlon,
                         mission, 
                         resources)
    

if __name__ == "__main__":
    check_fleet()
    ship_everything_to_Void(n=99)

