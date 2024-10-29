
class SpreadSheet:

    def __init__(self):
        self._cells = {}
        self._evaluating = set()

    def set(self, cell: str, value: str) -> None:
        self._cells[cell] = value

    def get(self, cell: str) -> str:
        return self._cells.get(cell, '')

    def evaluate(self, cell: str) -> str:
        if cell in self._evaluating:
            return '#Circular'
        self._evaluating.add(cell)
        
        value = self.get(cell)
        if value.isdigit():
            result = value
        elif value.startswith('='):
            inner_value = value[1:]
            if inner_value.isdigit():
                result = inner_value
            elif inner_value.startswith("'") and inner_value.endswith("'"):
                result = inner_value[1:-1]
            elif '+' in inner_value:  # Handle simple addition
                parts = inner_value.split('+')
                if all(part.isdigit() for part in parts):
                    result = str(sum(int(part) for part in parts))
                else:
                    result = '#Error'
            elif inner_value in self._cells:
                result = self.evaluate(inner_value)
                if result == '#Error':
                    result = '#Error'
            else:
                result = '#Error'
        elif value.startswith("'"):
            if value.endswith("'"):
                result = value[1:-1]
            else:
                result = '#Error'
        else:
            result = '#Error'
        
        self._evaluating.remove(cell)
        return result

