
class SpreadSheet:

    def __init__(self):
        self._cells = {}

    def set(self, cell: str, value: str) -> None:
        self._cells[cell] = value

    def get(self, cell: str) -> str:
        return self._cells.get(cell, '')

    def evaluate(self, cell: str) -> str:
        value = self.get(cell)
        if value.isdigit():
            return value
        elif value.startswith("'") and value.endswith("'"):
            return value
        elif value.startswith("='") and value.endswith("'"):
            return value[1:]
        else:
            return '#Error'

