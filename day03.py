__author__ = 'Thomas Stach'

import pandas as pd

def calculate_power_consumption(df):
    df = separate_bits(df)

    df = df.mean().round().astype(int)
    byte_gamma, byte_epsilon = '', ''
    for b in df:
        byte_gamma += str(b)
        byte_epsilon += str((b - 1) * -1)

    decimal_gamma = int(byte_gamma, 2)
    decimal_epsilon = int(byte_epsilon, 2)
    return decimal_gamma, decimal_epsilon

def verify_life_support_rating(df):
    df_bitwise = separate_bits(df)

    # Todo: Check again whether my algorithm for this rating is working right.

    oxygen_generator_rating = int(calculate_oxygen_generator_rating(df_bitwise), 2)
    co2_scrubber_rating = int(calculate_co2_scrubber_rating(df_bitwise), 2)

    return oxygen_generator_rating * co2_scrubber_rating

def separate_bits(df_):
    df = pd.DataFrame()
    for n in range(len(df_.loc[0, 0])):
        df[str(n + 1)] = df_[0].astype(str).str[n].astype(int)
    return df

def calculate_oxygen_generator_rating(df_bitwise):
    df_most_common_bits = df_bitwise.mean().round().astype(int)

    byte_most_common_bits = ''
    for b in df_most_common_bits:
        byte_most_common_bits += str(b)

    q = False
    for n in range(len(byte_most_common_bits)):
        if n == 0:
            q = byte_most_common_bits in df[0].unique()
            if q:
                return byte_most_common_bits
        else:
            q = byte_most_common_bits[:-n] in df[0].astype(str).str[:-n].unique()
            if q:
                return df.loc[df[0].astype(str).str[:-n] == byte_most_common_bits[:-n]]

def calculate_co2_scrubber_rating(df_bitwise):
    df_least_common_bits = (df_bitwise.mean() - 0.001).round().astype(int)

    byte_least_common_bits = ''
    for b in df_least_common_bits:
        byte_least_common_bits += str(b)

    q = False
    for n in range(len(byte_least_common_bits)):
        if n == 0:
            q = byte_least_common_bits in df[0].unique()
            if q:
                return byte_least_common_bits
        else:
            q = byte_least_common_bits[:-n] in df[0].astype(str).str[
                                              :-n].unique()
            if q:
                return df.loc[
                    df[0].astype(str).str[:-n] == byte_least_common_bits[:-n]]


if __name__ == '__main__':
    filepath = 'src/day03_report'
    df = pd.read_csv(filepath, header=None, dtype=str)
    gamma, epsilon = calculate_power_consumption(df)
    print(f'The power consumption equals: {gamma * epsilon}')
    life_support_rating = verify_life_support_rating(df)
    print(f'The life_support_rating equals: {life_support_rating}')