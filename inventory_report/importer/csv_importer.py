import csv
from .importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(self, path: str):
        if ".csv" in path:
            with open(path, encoding="utf-8") as csv_file:
                report_data = csv.DictReader(csv_file)
                return list(report_data)
        else:
            raise ValueError("Arquivo inválido")
