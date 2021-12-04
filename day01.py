__author__ = 'Thomas Stach'

import numpy as np

def part_one(file_path):
    numbers = np.loadtxt(file_path)
    return n_increased(numbers)


def n_increased(numbers):
    numbers_diff = np.ediff1d(numbers)
    numbers_increased = numbers_diff[numbers_diff > 0]
    return len(numbers_increased)

def part_two(file_path):
    numbers = np.loadtxt(file_path)
    return n_increased(sliding_sum3(numbers))

def sliding_sum3(array):
    return (np.delete(array, [0, 1]) + np.delete(array, [0, -1]) + np.delete(array, [-1, -2]))

if __name__ == '__main__':
    file_path = 'src/day01_numbers.txt'
    solution_1 = part_one(file_path)
    solution_2 = part_two(file_path)
    print(f'Solution 1: {solution_1}\nSolution 2: {solution_2}')