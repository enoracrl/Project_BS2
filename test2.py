file = "false_file_example-2.txt"
with open(file, 'r', encoding="utf-8") as file_reader:
    print(file_reader.readlines())