from ogame import OGame
from ogame.constants import Ships, Speed, Missions, Buildings, Research, Defense

def ship_slow_everything_to_Saturn():
    ships = [(Ships['LargeCargo'], 999),(Ships['light_fighter'], 999), (Ships['recycler'], 999)]
    speed = Speed['10%']
    where = {'galaxy': 5, 'system': 432, 'position': 8}
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
    ships = [(Ships['LargeCargo'], 999),(Ships['light_fighter'], 999), (Ships['recycler'], 999)]
    speed = Speed['10%']
    where = {'galaxy': 1, 'system': 434, 'position': 10}
    mission = Missions['Transport']
    resources = {'metal': 999999999, 'crystal': 999999999, 'deuterium': 9999999999}
    ogame.send_fleet(ogame.get_planet_by_name('Saturn'),
                     ships, 
                     speed, 
                     where, 
                     mission, 
                     resources)

def log_in():
    return OGame('Indus', 'hotgigi82@hotmail.com', '1101982.Ogame')

if __name__=="__main__":    
    ogame = log_in()
    if ogame.is_under_attack():
        ship_slow_everything_to_Mediaworld()
        ship_slow_everything_to_Saturn()
        ogame.logout()
    else:
        ogame.logout()