__author__ = 'Thomas Stach'

import numpy as np

def main(original_file, days_of_reproduction, method='list'):
    fish_timers = prepare_fish_data(original_file)

    if method == 'list':
        fish_timers = simulate_fish_reproduction_list(days_of_reproduction, fish_timers)
    elif method == 'numpy':
        fish_timers = simulate_fish_reproduction_numpy(days_of_reproduction,
                                                       fish_timers)
    elif method == 'dict':
        #Todo: Calculate via numbers of fish, i.e. something dict-like, but not an entry for each individual fish
        pass

    return len(fish_timers)


def simulate_fish_reproduction_numpy(days_of_reproduction, fish_timers):
    for day in range(1, days_of_reproduction + 1):
        fish_timers = np.array(fish_timers)
        fish_timers = fish_timers - 1
        timer, count = np.unique(fish_timers, return_counts=True)
        timer_counts = dict(zip(timer, count))
        new_fish = timer_counts.get(-1, 0)
        np.place(fish_timers, fish_timers == -1, 6)
        fish_timers = np.append(fish_timers, new_fish * [8])
    return fish_timers


def simulate_fish_reproduction_list(days_of_reproduction, fish_timers):
    for day in range(1, days_of_reproduction + 1):
        fish_timers = [t - 1 for t in fish_timers]
        new_fish = fish_timers.count(-1)
        new_fish_timers = new_fish * [8]
        fish_timers = [6 if t == -1 else t for t in fish_timers]
        fish_timers = fish_timers + new_fish_timers
    return fish_timers


def prepare_fish_data(original_file):
    with open(original_file) as f:
        data = f.read()
    fish_timers = list(data.split(','))
    fish_timers = [int(t) for t in fish_timers]
    return fish_timers


if __name__ == '__main__':
    original_file = 'src/day06_fish'
    first_solution = main(original_file, days_of_reproduction=80, method='list')
    print(f'First solution: {first_solution}')

    second_solution = main(original_file, days_of_reproduction=80, method='numpy')
    print(f'Second solution: {second_solution}')