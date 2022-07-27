import csv
import json
import xmltodict

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(path, report_type):
        list_of_companies = Inventory.get_list_of_companies_by_path(path)
        if report_type == "simples":
            return SimpleReport.generate(list_of_companies)
        elif report_type == "completo":
            return CompleteReport.generate(list_of_companies)
        else:
            raise ValueError

    @staticmethod
    def get_list_of_companies_by_path(path):
        if ".csv" in path:
            with open(path, encoding="utf-8") as csv_file:
                report_data = csv.DictReader(csv_file)
                return list(report_data)
        if ".json" in path:
            with open(path) as json_file:
                return json.load(json_file)
        if ".xml" in path:
            with open(path, encoding="utf-8") as file:
                report_data = xmltodict.parse(file.read())
                return list(report_data["dataset"]["record"])
        else:
            raise ValueError
