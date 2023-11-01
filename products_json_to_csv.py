import csv
import json
from typing import Union

def extract_fields (product: dict[str, Union[str, dict[str, str]]], fields: list[str]) -> list[str]:
    """Extract fields from dictionary to list of strings

    :param product: Product dictionary with data
    :param fields: Field keys to extract from data
    :return: list of extracted fields in order
    """
    response = []
    for field in fields:
        if field in product:
            response.append(product[field])
    
    return response

def write_to_csv (fields: list[str], data: list[list[str]], csv_path: str) -> None:
    """Create CSV file with provided data

    :param fields: Fields in data for csv header
    :param data: Data to write to csv
    :param csv_path: Path for csv file
    """
    with open(csv_path, mode="w+", newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(fields)
        writer.writerows(data)

def main () -> None:
    json_path = r'C:\Users\loren\Desktop\products.json'
    csv_path = r'C:\Users\loren\Desktop\PC\Dadosfera\products.csv'
    data = []
    fields = ["product_name", "product_category", "material", "features"]

    with open(json_path) as json_file:
        file_data = json.load(json_file)
        
        for product in file_data["products"]:
            data.append(extract_fields(product, fields))
    
    write_to_csv(fields, data, csv_path)

if __name__ == '__main__':
    main()