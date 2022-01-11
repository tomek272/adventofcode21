__author__ = 'Thomas Stach'
import numpy as np
from collections import Counter

def part_one(original_file):
    output_signal, signal_patterns = prepare_input(original_file)

    output_signal_decomposed = []
    for s in output_signal:
        for s_ in s.split(' '):
            output_signal_decomposed.append(s_)
    output_signal_decomposed_length = [len(s) for s in output_signal_decomposed]
    occurences = Counter(output_signal_decomposed_length)
    return occurences[3] + occurences[7] + occurences[2] + occurences[4]


def prepare_input(original_file):
    with open(original_file) as f:
        signal_patterns = []
        output_signal = []
        lines = f.readlines()
        for line in lines:
            line_separated = line.strip().split(' | ')
            signal_patterns.append(line_separated[0])
            output_signal.append(line_separated[1])
    return output_signal, signal_patterns


if __name__ == '__main__':
    original_file = 'src/day08_digits'
    first_solution = part_one(original_file=original_file)
    print(f'First solution: {first_solution}')