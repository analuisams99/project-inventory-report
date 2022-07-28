import json
from .importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(self, path: str):
        if ".json" in path:
            with open(path) as json_file:
                return json.load(json_file)
        else:
            raise ValueError("Arquivo inválido")
