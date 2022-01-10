__author__ = 'Thomas Stach'

import statistics

def main(original_file, method):
    with open(original_file) as f:
        crabs_positions = list(map(int, f.read().split(',')))

    if method == 'constant':
        best_position = round(statistics.median(crabs_positions))
        fuel_consumption = sum([abs(position - best_position) for position in crabs_positions])
    elif method == 'linear':
        fuel_consumptions = {}
        for test_position in range(min(crabs_positions), max(crabs_positions) + 1):
            individual_fuel_consumptions = [sum(range(1, abs(position - test_position) + 1)) for position in crabs_positions]
            fuel_consumptions[test_position] = sum(individual_fuel_consumptions)
        best_position = min(fuel_consumptions, key=fuel_consumptions.get)
        fuel_consumption = fuel_consumptions[best_position]
    return best_position, fuel_consumption

if __name__ == '__main__':
    original_file = 'src/day07_crabs'
    best_position, fuel_consumption = main(original_file=original_file, method='linear')
    print(f'Most efficient position {best_position} at fuel consumption of {fuel_consumption}')
