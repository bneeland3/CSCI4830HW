import csv

def read_csvs(files):
    neg_data = []
    pos_data = []
    field_data = []
    for file in files:
        with open(file, 'r') as f:
            csv_reader = csv.reader(f)
            for row in csv_reader:
                # Assuming each file contains only one column of data
                if file == files[0]:
                    neg_data.append(float(row[0]))  # Assuming first column contains negative data
                elif file == files[1]:
                    pos_data.append(float(row[0]))  # Assuming first column contains positive data
                elif file == files[2]:
                    field_data.append(float(row[0]))  # Assuming first column contains field data
    return neg_data, pos_data, field_data

def find_c():
    return None