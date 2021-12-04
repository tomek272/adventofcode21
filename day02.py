__author__ = 'Thomas Stach'

import pandas as pd

def move(movements, aim=True):
    if aim == False:
        x = movements.loc[movements['type'] == 'forward']['steps'].sum()
        y = movements[movements['type'] == 'down']['steps'].sum() - movements[movements['type'] == 'up']['steps'].sum()
    if aim == True:
        movements['aim'] = pd.concat([movements.loc[movements['type'] == 'down']['steps'], -1 * movements.loc[movements['type'] == 'up']['steps']])
        movements['aim'] = movements['aim'].fillna(0).cumsum()
        movements['depth'] = movements.loc[movements['type'] == 'forward']['steps'] * movements.loc[movements['type'] == 'forward']['aim']
        x = movements.loc[movements['type'] == 'forward']['steps'].sum()
        y = (movements.loc[movements['type'] == 'forward']['steps'] * movements.loc[movements['type'] == 'forward']['aim']).sum()
    return (x,y)

def main(filepath, position_initial=(0, 0)):
    movements = pd.read_csv(filepath, sep=' ', header=None, names=['type', 'steps'])
    position_end = tuple([position_initial[i] + move(movements)[i] for i in range(2)])
    print(f'The position of our submarine is: {position_end}')
    print(f'x multiplied by y equals: {position_end[0] * position_end[1]}')

if __name__ == '__main__':
    filepath = 'src/day02_movements'
    main(filepath)
    pass