from ogame import OGame
from ogame.constants import Ships, Speed, Missions, Buildings, Research, Defense

def log_in():
    return OGame('Indus', 'hotgigi82@hotmail.com', '1101982.Ogame')


def ship_slow_everything_to_Moon():
    ships = [(Ships['LargeCargo'], 999),(Ships['LightFighter'], 999),(Ships['Cruiser'], 9999), (Ships['Recycler'], 999)]
    speed = Speed['10%']
    where = {'galaxy': 5, 'system': 432, 'position': 8,'type':3}
    mission = Missions['Transport']
    for planet_name in ['MediaWorld','Saturn','Amazon','Trony','Alibaba','Unieuro']:
        resources = {'metal': 999999999, 'crystal': 999999999, 'deuterium': 9999999999}
        ogame.send_fleet(ogame.get_planet_by_name(planet_name),
                         ships, 
                         speed, 
                         where, 
                         mission, 
                         resources)    

def ship_slow_everything_to_Mediaworld():
    ships = [(Ships['LargeCargo'], 9999),(Ships['LightFighter'], 9999), (Ships['EspionageProbe'], 999),(Ships['Cruiser'], 9999), (Ships['Recycler'], 9999)]
    speed = Speed['10%']
    where = {'galaxy': 1, 'system': 434, 'position': 10, 'type':1}
    mission = Missions['Transport']
    resources = {'metal': 999999999, 'crystal': 999999999, 'deuterium': 9999999999}
    ogame.send_fleet(ogame.get_moon_ids()[0],    
                     ships, 
                     speed, 
                     where, 
                     mission, 
                     resources)

if __name__=="__main__":    
    ogame = log_in()
    if ogame.is_under_attack():
        ship_slow_everything_to_Mediaworld()
        ship_slow_everything_to_Moon()
        ogame.logout()
    else:
        ogame.logout()