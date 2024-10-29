
class SpreadSheet:

    def __init__(self):
        self._cells = {}

    def set(self, cell: str, value: str) -> None:
        self._cells[cell] = value

    def get(self, cell: str) -> str:
        return self._cells.get(cell, '')

    def evaluate(self, cell: str) -> str:
        value = self.get(cell)
        if value.isdigit() or (value.startswith('=') and value[1:].isdigit()):
            return value.lstrip('=')
        elif value.startswith("'") and value.endswith("'"):
            return value
        elif value.startswith("='") and value.endswith("'"):
            return value[1:]
        elif value.replace('.', '', 1).isdigit() and not value.count('.') > 1:
            return '#Error'
        else:
            return '#Error'

