import csv

# def load_csv(csvpath):
#     """Reads the CSV file from path provided.

#     Args:
#         csvpath (Path): The csv file path.

#     Returns:
#         A list of lists that contains the rows of data from the CSV file.

#     """
#     with open(csvpath, "r") as csvfile:
#         data = []
#         csvreader = csv.reader(csvfile, delimiter=",")

#         # Skip the CSV Header
#         next(csvreader)

#         # Read the CSV data
#         for row in csvreader:
#             data.append(row)
#     return data

def save_csv(csvpath,result):
    """ J.Guanzon Comment-
    Saves the CSV file from path provided.

    Args:
        csvpath (Path): The CSV file path.
        data (list of lists): A list of the rows of data for the CSV file.
        header (list): A header for the csv to clearly label what the values are.
    
    Return:
        A csv file with qualifying stocks clearly labeled.

    """
    with open(csvpath, "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerows(result)
