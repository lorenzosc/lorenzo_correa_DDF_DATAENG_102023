import csv

def find_nth_occurrence(string, substring, n):
    start = string.find(substring)
    while start >= 0 and n > 1:
        start = string.find(substring, start+1)
        n -= 1
    return start
        

with open(r"C:\Users\loren\Downloads\corpus.jsonl", "r") as file, open("corpus.csv", "a+", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["ID", "Item", "Description"])
    for i, line in enumerate(file):
        first_comma = line.find(",")
        first_column = line.find(":")
        second_column = find_nth_occurrence(line, "\"", 4)
        third_column = find_nth_occurrence(line, "\"", 8)
        second_comma = find_nth_occurrence(line, "\"", 6)
        third_comma = len(line) - line[::-1].find("\"")
        
        writer.writerow([line[first_column+2:first_comma], 
                         line[second_column+4:second_comma], 
                         line[third_column+4:third_comma]])
        

