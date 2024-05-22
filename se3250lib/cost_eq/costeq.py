ship_costs ={
    #BLUFOR friendly
    "DDG_52": 1200000,
    "DDG_84": 1300000,
    "DDG_105": 1500000
}

ship_salvage_rates = {
    #BLUFOR friendly
    "DDG_52": 0.3,
    "DDG_84": 0.2,
    "DDG_105": 0.4
}

wpn_costs ={
    #BLUFOR friendly
    "DDG_52": 1200000,
    "DDG_84": 1300000,
    "DDG_105": 1500000
}

def calculate_ship_cost(ship_type, num_ships_lost, num_ships_damaged):
    ship_cost = ship_costs[ship_type]
    salvage_rate = ship_salvage_rates[ship_type]
    cost_without_salvage = ship_cost * num_ships_lost
    salvage_cost = cost_without_salvage * salvage_rate
    repair_cost = 0
    for _ in range(num_ships_damaged):
        repair_rate - random.normalvariate(0.125, 0.05) #Mean 12.5%, std dev 5%
        repair_rate = max(0.05, min(0.2,repair_rate)) #retrict rates between 5-20%
        repair_cost += ship_cost * repair_rate
    total_ship_cost = cost_without_salvage - salvage_cost + repair_cost
    return total_ship_cost

def calculate_weap_cost(weapon_type, num_weapons_fired):
    wpn_cost = wpn_costs[weapon_type] * num_weapons_fired
    return wpn_cost