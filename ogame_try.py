from ogame import OGame
from ogame.constants import Ships, Speed, Missions, Buildings, Research, Defense, Facilities

ogame = OGame("Indus", "hotgigi82@hotmail.com", "1101982.Ogame")


def check_energy(planet_name):
    return (ogame.get_resources(ogame.get_planet_by_name(planet_name)))["energy"] < 0


def building_in_construction(planet_name):
    return ogame.get_overview(ogame.get_planet_by_name(planet_name))["buildings"] != ""


def build_resources(planet_name):
    """Checking first if needed energy and try to build energy resources, and after,
        trying for building other resources"""
    if check_energy(planet_name):
        print("Trying to create more energy for the planet %s" % planet_name)
        for i in ["SolarPlant", "FusionReactor"]:
            ogame.build_building(ogame.get_planet_by_name(planet_name), Buildings[i])
            if len(ogame.get_overview(planet_name)["buildings"]) != 0:
                break
    else:
        print("Trying build resources for the planet %s" % planet_name)
        for k in [
            "CrystalMine",
            "MetalMine",
            # "DeuteriumSynthesizer",
            # "MetalStorage",
            # "CrystalStorage",
            # "DeuteriumTank",
        ]:
            ogame.build_building(ogame.get_planet_by_name(planet_name), Buildings[k])
            if len(ogame.get_overview(planet_name)["buildings"]) != 0:
                print(ogame.get_overview(planet_name)["buildings"])
                break
            else:
                pass


def ship_everything_to_moon(planet_name):
    ships = [(Ships["LargeCargo"], 99)]
    speed = Speed["100%"]
    where = {"galaxy": 5, "system": 432, "position": 8,'type':3}
    mission = Missions["Transport"]
    resources = {"metal": 999999999, "crystal": 999999999, "deuterium": 9999999999}
    ogame.send_fleet(
        ogame.get_planet_by_name(planet_name), ships, speed, where, mission, resources
    )


if __name__ == "__main__":
    planets_names_list = ["MediaWorld", "Amazon", "Trony","Unieuro","Alibaba", "Saturn"]
    '''for planet in planets_names_list:
        print("evaluating planet %s" % planet)
        build_resources(planet)
    for planet in planets_names_list:
        try:
            ogame.build(planet,Facilities['RoboticsFactory'])
            ogame.build(planet,Facilities['MissileSilo'])
            ogame.build(planet,Facilities['NaniteFactory'])
        except:
            pass'''
    # Sending Resources to mother
    for planet in planets_names_list:
        print("sending resources from %s" % planet)
        ship_everything_to_moon(planet)
    # Research
    '''for i in Research:
        ogame.build(ogame.get_planet_by_name("Saturn"), Research[i])
        if len(ogame.get_overview("Saturn")["research"]) != 0:
            print(ogame.get_overview("Saturn")["research"][0])
            break'''
