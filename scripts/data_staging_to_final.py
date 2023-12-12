import csv

source_csv_path = "data/binary_class_sentences-stage.csv"
target_csv_path = "data/binary_class_sentences.csv"

# Open the target CSV file in append mode
with open(target_csv_path, 'a', newline='', encoding='utf-8') as target_file:
    writer = csv.writer(target_file)

    # Open and read the source CSV file
    with open(source_csv_path, 'r', newline='', encoding='utf-8') as source_file:
        reader = csv.reader(source_file)
        # Append each row from the source file to the target file
        for row in reader:
            writer.writerow(row)