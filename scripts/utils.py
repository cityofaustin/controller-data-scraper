import csv
import os


def outpath(filename, child_dir):
    parent_dir = os.path.dirname(os.getcwd())
    return os.path.join(parent_dir, child_dir, filename)


def to_csv(rows, fieldnames=[], filename='data.csv', header=True):
    with open(filename, 'w', newline='\n') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        
        if header:
            writer.writeheader()

        writer.writerows(rows)

    return len(rows)
