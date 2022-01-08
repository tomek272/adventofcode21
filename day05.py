__author__ = 'Thomas Stach'
import pandas as pd

def main():
    #Import and prepare file.
    original_file = 'src/day05_paths'
    prepared_file = 'src/day05_paths_prepared'
    with open(original_file) as file_in, open(prepared_file, 'w') as file_out:
        data = file_in.read()
        data = data.replace(' -> ', ',')
        file_out.write(data)

    coordinates = pd.read_csv(prepared_file, sep=',', header=None, dtype=int,
                              names=['x1', 'y1', 'x2', 'y2'])

    #Consider vertical or horizontal lines only.
    coordinates = coordinates.loc[(coordinates['x1'] == coordinates['x2']) | (coordinates['y1'] == coordinates['y2'])]

    #Todo: create function which 'draws' path (idea?), i.e. create lines of coordinates via range functions
    #Todo: do repeatedily for each path, cast coordinates to strings and count duplicates
    pass

if __name__ == '__main__':
    main()