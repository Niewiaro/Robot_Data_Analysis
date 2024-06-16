import csv


def convert_txt_to_csv(input_name, output_name, LIMIT: int = 0):
    with open(input_name + ".txt", "r") as in_file:
        lines = [line.strip().split("\t") for line in in_file if line.strip()]
        if LIMIT > 0:
            lines = lines[:LIMIT]
        with open(output_name + ".csv", "w", newline="") as out_file:
            writer = csv.writer(out_file)
            writer.writerows(lines)


if __name__ == "__main__":
    convert_txt_to_csv("data", "data")
