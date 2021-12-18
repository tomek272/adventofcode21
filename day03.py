__author__ = 'Thomas Stach'

import pandas as pd

def calculate_power_consumption(filepath):
    df_ = pd.read_csv(filepath, header=None, dtype=str)
    df = separate_bits(df_)

    df = df.mean().round().astype(int)
    byte_gamma, byte_epsilon = '', ''
    for b in df:
        byte_gamma += str(b)
        byte_epsilon += str((b - 1) * -1)

    decimal_gamma = int(byte_gamma, 2)
    decimal_epsilon = int(byte_epsilon, 2)
    return decimal_gamma, decimal_epsilon


def separate_bits(df_):
    df = pd.DataFrame()
    for n in range(len(df_.loc[0, 0])):
        df[str(n + 1)] = df_[0].astype(str).str[n].astype(int)
    return df


if __name__ == '__main__':
    filepath = 'src/day03_report'
    gamma, epsilon = calculate_power_consumption(filepath)
    print(gamma * epsilon)