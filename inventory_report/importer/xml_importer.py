import xmltodict
from .importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(self, path: str):
        if ".xml" in path:
            with open(path, encoding="utf-8") as file:
                report_data = xmltodict.parse(file.read())
                return list(report_data["dataset"]["record"])
        else:
            raise ValueError("Arquivo inválido")
