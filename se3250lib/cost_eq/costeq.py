import random

ship_costs = {
    # BLUFOR friendly
    "CG-Ticonderoga": 1000000000,
    "DDG-Arleigh-Burke": 1800000,
    "LCS-Freedom": 700000,
    "LCS-Independence": 800000,
    "Test-1": 1000000,
    "Test-2": 1000000    
}

ship_salvage_rates = {
    # BLUFOR friendly
    "CG-Ticonderoga": 0.45,
    "DDG-Arleigh-Burke": 0.35,
    "LCS-Freedom": 0.15,
    "LCS-Independence": 0.18
    "Test-1": 0.12,
    "Test-2": 0.20
}

wpn_costs ={
    # BLUFOR friendly
    "AGM-114L": 150000, #Hellfire (LCS Only - Offensive)
    "AGM-84E": 1527416, #Harpoon Variant (Offensive)
    "BGM-109": 1900000, #Tomahawk (Offensive)
    "RIM-116": 920000, #Rolling Airframe Missile (LCS Only - Defensive)
    "RIM-66M": 2400000, #SM-2MR (DDG and CG - Both defensive and offensive)
    "RGM-84": 1500000, #Harpoon (Defensive)
    "RGM-184A": 2200000, #Naval Strike Missile (Offensive)
    "Test-1": 2300000,
    "Test-2": 1990000 
}

def calculate_ship_cost(ship_type, num_ships_lost, num_ships_damaged):
    ship_cost = ship_costs[ship_type]
    salvage_rate = ship_salvage_rates[ship_type]
    cost_without_salvage = ship_cost * num_ships_lost
    salvage_cost = cost_without_salvage * salvage_rate
    repair_cost = 0
    for _ in range(num_ships_damaged):
        repair_rate = random.normalvariate(0.125, 0.05) #Mean 12.5%, std dev 5%
        repair_rate = max(0.05, min(0.2,repair_rate)) #restrict rates between 5-20%
        repair_cost += ship_cost * repair_rate
    total_ship_cost = cost_without_salvage - salvage_cost + repair_cost
    return total_ship_cost

def calculate_weap_cost(weapon_type, num_weapons_fired):
    wpn_cost = wpn_costs[weapon_type] * num_weapons_fired
    return wpn_cost