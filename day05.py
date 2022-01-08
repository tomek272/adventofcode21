__author__ = 'Thomas Stach'
import pandas as pd

def main(original_file, prepared_file, drop_diagonal_paths=True):
    prepare_input(original_file, prepared_file)

    paths = pd.read_csv(prepared_file, sep=',', header=None, dtype=int,
                              names=['x1', 'y1', 'x2', 'y2'])

    #Consider vertical or horizontal lines only.
    if drop_diagonal_paths:
        paths = paths.loc[(paths['x1'] == paths['x2']) | (paths['y1'] == paths['y2'])]

    #Create DataFrame to collect all coordinates from all paths.
    coordinates = create_coordinates_from_paths(paths)

    #Count distinct overlapping points from all paths.
    number_overlappings = count_overlappings(coordinates)

    return number_overlappings


def count_overlappings(coordinates):
    coordinates['xy'] = coordinates['x'].astype(str) + '_' + coordinates[
        'y'].astype(str)
    counts = pd.DataFrame(coordinates['xy'].value_counts()).rename(
        columns={'xy': 'counts'}).reset_index(drop=False).rename(
        columns={'index': 'xy'})
    number_overlappings = \
    counts.loc[counts['counts'] > 1].drop_duplicates().shape[0]
    return number_overlappings


def create_coordinates_from_paths(paths):
    coordinates = pd.DataFrame(columns=['x', 'y'])
    for idx, path in paths.iterrows():
        if path['x2'] >= path['x1']:
            x = list(range(path['x1'], path['x2'])) + [path['x2']]
        else:
            x = list(range(path['x1'], path['x2'], -1)) + [path['x2']]
        if path['y2'] >= path['y1']:
            y = list(range(path['y1'], path['y2'])) + [path['y2']]
        else:
            y = list(range(path['y1'], path['y2'], -1)) + [path['y2']]

        if len(x) > len(y):
            y = y * len(x)
        elif len(y) > len(x):
            x = x * len(y)
        coordinates = coordinates.append(pd.DataFrame({'x': x, 'y': y}),
                                         ignore_index=True)
    return coordinates


def prepare_input(original_file, prepared_file):
    with open(original_file) as file_in, open(prepared_file, 'w') as file_out:
        data = file_in.read()
        data = data.replace(' -> ', ',')
        file_out.write(data)


if __name__ == '__main__':
    #Import and prepare file.
    original_file = 'src/day05_paths'
    prepared_file = 'src/day05_paths_prepared'

    # solution_without_diagonal_paths = main(original_file, prepared_file)
    # print(f'Solution without diagonal paths: {solution_without_diagonal_paths}')

    solution_with_diagonal_paths = main(original_file, prepared_file, drop_diagonal_paths=False)
    print(f'Solution with diagonal paths: {solution_with_diagonal_paths}')