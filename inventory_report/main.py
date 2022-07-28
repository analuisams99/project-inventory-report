import sys

from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def main():
    if len(sys.argv) < 3:
        return sys.stderr.write("Verifique os argumentos\n")
    path, type = sys.argv[1], sys.argv[2]

    if ".csv" in path:
        print(InventoryRefactor(CsvImporter).import_data(path, type), end="")
    if ".json" in path:
        print(InventoryRefactor(JsonImporter).import_data(path, type), end="")
    if ".xml" in path:
        print(InventoryRefactor(XmlImporter).import_data(path, type), end="")
