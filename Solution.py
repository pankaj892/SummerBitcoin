import csv
csv_file = "mempool.csv" #Read the csv file
txt_file = "block.txt" # Read the text file
with open(txt_file, "w") as output_file:
    with open(csv_file, "r") as input_file:
        [output_file.write("".join(row[0])+'\n') for row in csv.reader(input_file)] #Write the tx_id contents to block.txt file
    output_file.close()