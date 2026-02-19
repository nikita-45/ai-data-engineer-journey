import csv

def read_csv(file_path):
    data = []
    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data


def calculate_total_sales(data):
    total = 0
    for row in data:
        total += float(row["sales"])
    return total


if __name__ == "__main__":
    file_path = "sales.csv"
    data = read_csv(file_path)
    total_sales = calculate_total_sales(data)
    print("Total Sales:", total_sales)
