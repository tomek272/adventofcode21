__author__ = 'Thomas Stach'
import numpy as np

def main(file_path_original, file_path_prepared):
    # Read input file, prepare it appropriately and write it to output file.
    prepare_bingo_input(file_path_original, file_path_prepared)

    # Save bingo numbers sequence to list.
    bingo_numbers = extract_bingo_numbers(file_path_prepared)

    # Save bingo fields to list of numpy arrays.
    bingo_fields = extract_bingo_fields(file_path_prepared)

    # Check for bingos.
    first_solution, last_solution = check_for_bingos(bingo_fields,
                                                     bingo_numbers)

    return first_solution, last_solution


def check_for_bingos(bingo_fields, bingo_numbers):
    first_solution = 0
    last_solution = 0
    bingo_fields_with_bingos = []
    # Iterate over Bingo numbers.
    for bingo_number in bingo_numbers:
        # Mark bingo number in bingo fields, i.e. replace bingo number by nan.
        bingo_fields = mark_bingo_numbers(bingo_fields, bingo_number)

        # Count the marked fields, i.e. nan-values, in each row and column in each Bingo field.
        for idx, bingo_field in enumerate(bingo_fields):
            if idx not in bingo_fields_with_bingos:
                for row in bingo_field:
                    n_marked_cells = np.count_nonzero(np.isnan(row))
                    if n_marked_cells == 5:
                        if first_solution == 0:
                            first_solution = np.nansum(
                                bingo_field) * bingo_number
                            bingo_fields_with_bingos = []
                        if len(set(bingo_fields_with_bingos)) == 99:
                            last_solution = np.nansum(
                                bingo_field) * bingo_number
                        bingo_fields_with_bingos.append(idx)

                for column in bingo_field.T:
                    n_marked_cells = np.count_nonzero(np.isnan(column))
                    if n_marked_cells == 5:
                        if first_solution == 0:
                            first_solution = np.nansum(
                                bingo_field) * bingo_number
                            bingo_fields_with_bingos = []
                        if len(set(bingo_fields_with_bingos)) == 99:
                            last_solution = np.nansum(
                                bingo_field) * bingo_number
                        bingo_fields_with_bingos.append(idx)
    return first_solution, last_solution


def mark_bingo_numbers(bingo_fields, bingo_number):
    bingo_fields_vstacked = np.vstack(bingo_fields)
    bingo_fields_vstacked = np.where(bingo_fields_vstacked == bingo_number,
                                     np.nan, bingo_fields_vstacked)
    bingo_fields = np.split(bingo_fields_vstacked,
                            bingo_fields_vstacked.shape[0] / 5)
    return bingo_fields


def extract_bingo_fields(file_path_prepared):
    with open(file_path_prepared) as f:
        array = np.loadtxt(f, int, delimiter=' ', skiprows=2)
    bingo_fields = np.split(array, array.shape[0] / 5)
    return bingo_fields


def extract_bingo_numbers(file_path_prepared):
    with open(file_path_prepared) as f:
        first_line = f.readline()
    bingo_numbers = [int(n) for n in list(first_line.split(','))]
    return bingo_numbers


def prepare_bingo_input(file_path_original, file_path_prepared):
    with open(file_path_original) as f_in, open(file_path_prepared,
                                                'w') as f_out:
        for line_in in f_in:
            line_out = line_in.replace('  ', ' ').strip(' ')
            f_out.write(line_out)


if __name__ == '__main__':
    # Call main function and define input and output files.
    first_solution, last_solution = main(file_path_original = 'src/day04_bingo', file_path_prepared='src/day04_bingo_prepared')
    print(f'First solution: {first_solution}\nLast solution: {last_solution}')