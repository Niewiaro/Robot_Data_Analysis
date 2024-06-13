import csv

LIMIT = 1000

with open("data.txt", "r") as in_file:
    lines = [line.strip().split("\t") for line in in_file if line.strip()]
    if LIMIT > 0:
        lines = lines[:LIMIT]
    with open("data.csv", "w", newline="") as out_file:
        writer = csv.writer(out_file)
        writer.writerows(lines)
