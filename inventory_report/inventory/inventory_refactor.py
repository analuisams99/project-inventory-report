from collections.abc import Iterable

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def file_data(self, path):
        self.data.extend(self.importer.import_data(path))

    def __iter__(self):
        return InventoryIterator(self.data)

    def import_data(self, path, tipo):
        self.file_data(path)
        if tipo == "simples":
            return SimpleReport.generate(self.data)
        if tipo == "completo":
            return CompleteReport.generate(self.data)
        else:
            raise ValueError
