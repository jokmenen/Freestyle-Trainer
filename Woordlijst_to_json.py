import json

# Function to convert the file into JSON format
def convert_to_json(input_file, output_file):
    result = {}
    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split('>')
            word = parts[0]
            definitions = parts[1:]
            result[word] = definitions
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(result, outfile, ensure_ascii=False, indent=4)

# Example usage
input_file = 'Woordenlijst.txt'  # Update this to the path of your input file
output_file = 'Woordenlijst.json'  # The output file name/path

convert_to_json(input_file, output_file)
