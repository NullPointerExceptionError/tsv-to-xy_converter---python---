import csv # read csv/tsv file
from glob import glob # read file without filename
import os # working with paths, creating folders, etc.



def is_header(line:dict, characteristic:dict=["x", "y"]) -> bool:
    """
    returns Boolean if parameter header is a header.
    returns True if element of characteristic was found in line (case-insensitive).

    Parameters
    ----------
    header:dict -> line to be tested
    characteristic:dict -> letters to be tested
    """
    line_copy = [elem.lower() for elem in line] # copy line to avoid lower-cases wanted header
    for data_idx in range(0, len(characteristic)):
        if characteristic[data_idx].lower() in line_copy: # if lower-case was found in line
            return True # letter of characteristic found in line
    return False # line is no header

def create_folder(name:str):
    """
    creates subfolder if doesnt exist yet.

    Parameters
    ----------
    name:str -> name of subfolder
    """
    path = "./" + name
    try:
        os.mkdir(path) # create folder
    except FileExistsError:
        pass # folder already exists

def main():
    xy_folder_name = "xy-files"
    create_folder(xy_folder_name)
    all_tsv_files = glob("*.tsv") # catch all .tsv-files in current folder
    for tsv_file in all_tsv_files:
        with open(tsv_file, "r") as current_tsv:
            tsv = csv.reader(current_tsv, delimiter="\t") # read .tsv-file as .csv-file
            
            xy_file_path = "./" + xy_folder_name + "./" + tsv_file[0:-3] + "xy"
            with open(xy_file_path, "w", newline="") as current_xy: # create or open .xy file
                csv_writer = csv.writer(current_xy, delimiter='\t') # create tabstop-separating csv writer
                first_line = next(tsv)
                if not (is_header(first_line)): # writes first line if no header
                    csv_writer.writerow(first_line)
                    print(first_line[0] + "is no header")
                for line in tsv:
                    modified_line = [elem.replace(",", ".") for elem in line] # replaces all , with .
                    csv_writer.writerow(modified_line) # writes modified line into .xy-file
        try:
            os.remove(tsv_file) # remove the .tsv-file
        except FileNotFoundError:
            pass # .tsv-file doesnt exist


if __name__ == "__main__":
    main()
