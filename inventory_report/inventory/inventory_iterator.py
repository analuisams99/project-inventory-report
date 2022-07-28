from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data_list: list):
        self.data_list = data_list
        self.current_index = 0

    def __next__(self):
        data = self.data_list[self.current_index]
        if not data:
            raise StopIteration()
        self.current_index += 1
        return data
