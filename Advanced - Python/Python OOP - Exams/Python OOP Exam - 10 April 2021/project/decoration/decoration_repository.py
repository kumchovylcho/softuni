class DecorationRepository:

    def __init__(self):
        self.decorations = []

    def add(self, decoration):
        if decoration not in self.decorations:
            self.decorations.append(decoration)

    def remove(self, decoration):
        if decoration in self.decorations:
            self.decorations.remove(decoration)
            return True
        return False

    def find_by_type(self, decoration_type: str):
        for item in self.decorations:
            if type(item).__name__ == decoration_type:
                return item
        return "None"
