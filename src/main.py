import json
import csv


def get_json_data():
    with open("./data/data.json", "r") as f:
        # https://docs.python.org/3/library/json.html#json.load
        return json.load(f)


if __name__ == "__main__":
    print(
        "\n--------------------------------------------\n\t\tJSON to CSV\n--------------------------------------------\n"
    )

    json_data = get_json_data()

    header = json_data[0].keys()

    print(f"header: {header}\n")

    # https://docs.python.org/3/library/csv.html
    with open("./data/data.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(json_data)
