import csv

from collections import defaultdict


def read_csv(path):
    """Reads a CSV from a given path.
    Stores it as a list of lists.

    Args:
        path (str): path to the CSV file.

    Returns:
        list: list of lists, each corresponds
        to a different line in the given CSV file.
    """
    with open(path, newline='') as csv_file:
        csv_file = csv.reader(csv_file, delimiter=',')
        rows = [row for row in csv_file]
    return rows


def create_dict(csv_files, unique):
    """Creates a dict from a list of lists.
    Firs element stored should contain the information
    about column names. The keys in the dictionary
    will be taken from the `unique` column.

    Args:
        csv_files (list): list of lists. Each contains
        one line from a CSV file,
        unique (str): name of the column. It's values will
        be used as ids (this column should contain only
        unique values).

    Returns:
        tuple: the first element is the dictionary
        made from the list of lists which corresponds
        to the CSV file. The second element is a list
        which containt the names of all columns.
    """
    csv_dict = defaultdict(dict)
    all_columns = set()
    for csv_file in csv_files:
        col_names = csv_file[0]
        for col_name in col_names:
            all_columns.add(col_name)
    all_columns = list(all_columns)
    all_columns.remove(unique)
    for csv_file in csv_files:
        col_names = csv_file[0]
        unique_id = col_names.index(unique)
        for line in csv_file[1:]:
            tmp = {}
            for i in range(len(col_names)):
                if i == unique_id:
                    continue
                tmp[col_names[i]] = line[i]
            if tmp.keys() == all_columns:
                continue
            else:
                missing_columns = list(set(all_columns).difference(set(tmp.keys())))
                for missing_column in missing_columns:
                    tmp[missing_column] = ''
            csv_dict[line[unique_id]] = tmp
    return csv_dict, all_columns


def merge_csv(csv_list, output_path, unique):
    """Merges two CSV files by a unique column.

    Args:
        csv_list (list): list of paths to CSV files,
        output_path (str): path to save the new, merged CSV file,
        unique (str): column name, should be unique.
    """
    csv_files_list = [read_csv(path) for path in csv_list]
    csv_files_dict, col_names = create_dict(csv_files_list, unique)
    merged_csv = [[unique, *col_names]]
    for unique_key, value in csv_files_dict.items():
        tmp = [value.get(col_name, unique_key) for col_name in merged_csv[0]]
        merged_csv.append(tmp)
    with open(output_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(merged_csv)


if __name__ == "__main__":
    merge_csv(
        csv_list=['files/students1.csv', 'files/students2.csv'],
        output_path='files/all_students.csv',
        unique='Name'
    )
