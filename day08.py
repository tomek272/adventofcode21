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

def part_two(original_file):
    output_signals, signal_patterns = prepare_input(original_file)
    output_signal_decoded = []

    for signal_pattern, output_signal in  zip(signal_patterns, output_signals):
        signal_pattern = signal_pattern.split(' ')
        signal_pattern_length = [len(s) for s in signal_pattern]
        signal_mapping = {}

        signal_mapping = decode_output_signal(signal_mapping, signal_pattern,
                                              signal_pattern_length)

        signal_mapping_inverse = {v: k for k, v in signal_mapping.items()}

        output_number = ''
        for s in output_signal.split(' '):
            output_number += str(signal_mapping_inverse[''.join(sorted(s))])
        output_signal_decoded.append(int(output_number))

    return sum(output_signal_decoded)


def decode_output_signal(signal_mapping, signal_pattern, signal_pattern_length):
    # Decode 1
    signal_mapping[1] = signal_pattern[signal_pattern_length.index(2)]
    # Decode 4
    signal_mapping[4] = signal_pattern[signal_pattern_length.index(4)]
    # Decode 7
    signal_mapping[7] = signal_pattern[signal_pattern_length.index(3)]
    # Decode 8
    signal_mapping[8] = signal_pattern[signal_pattern_length.index(7)]
    # Decode 3
    for s in signal_pattern:
        if len(s) == 5:
            n = 0
            for c in signal_mapping[7]:
                if c in s:
                    n += 1
            if n == 3:
                signal_mapping[3] = s
    # Decode 5
    for s in signal_pattern:
        if len(s) == 5:
            n = 0
            for c in signal_mapping[4]:
                if c in s:
                    n += 1
            if (n == 3 and s != signal_mapping[3]):
                signal_mapping[5] = s
    # Decode 2
    for s in signal_pattern:
        if len(s) == 5 and s not in signal_mapping.values():
            signal_mapping[2] = s
    # Decode 0
    for s in signal_pattern:
        if len(s) == 6:
            n = 0
            n_ = 0
            for c in signal_mapping[7]:
                if c in s:
                    n += 1
            for c in signal_mapping[4]:
                if c in s:
                    n_ += 1
            if (n == 3 and n_ == 3):
                signal_mapping[0] = s
    # Decode 6
    for s in signal_pattern:
        if len(s) == 6:
            n = 0
            for c in signal_mapping[7]:
                if c in s:
                    n += 1
            if n == 2:
                signal_mapping[6] = s
    # Decode 9
    for s in signal_pattern:
        if len(s) == 6:
            n = 0
            n_ = 0
            for c in signal_mapping[7]:
                if c in s:
                    n += 1
            for c in signal_mapping[4]:
                if c in s:
                    n_ += 1
            if (n == 3 and n_ == 4):
                signal_mapping[9] = s
    signal_mapping = {k: ''.join(sorted(v)) for k, v in signal_mapping.items()}
    if (len(signal_mapping.values()) != len(set(signal_mapping.values()))):
        print('Signal mapping table contains duplicate translations.')
    return signal_mapping


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
    solution_one = part_one(original_file=original_file)
    print(f'First solution: {solution_one}')
    solution_two = part_two(original_file=original_file)
    print(f'Second solution: {solution_two}')