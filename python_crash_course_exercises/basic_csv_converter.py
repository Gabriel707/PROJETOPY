import csv


def convert_to_csv(input_file, output_file, delimiter=','):
    with open(input_file, 'r', encoding='latin-1') as f:
        # Read data from input file
        data = [line.strip().split(delimiter) for line in f.readlines()]

    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        # Write data to CSV file
        writer = csv.writer(f)
        writer.writerows(data)


# Example usage
# Replace with the path to your input file
input_file = r"C:\Users\Gabriel\Downloads\LoginData"
# Replace with the desired path for the output CSV file
output_file = r"C:\Users\Gabriel\Downloads\LoginData.csv"
convert_to_csv(input_file, output_file)
