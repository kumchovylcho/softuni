from math import ceil


class PhotoAlbum:

    def __init__(self, pages: int):
        self.pages = int(pages)
        self.photos = [[] for _ in range(self.pages)]

    @staticmethod
    def from_photos_count(photos_count: int):
        return PhotoAlbum(ceil(photos_count / 4))

    def add_photo(self, label: str):
        for row in range(len(self.photos)):
            if len(self.photos[row]) < 4:
                self.photos[row].append(label)
                return f"{label} photo added successfully on page {row + 1} slot {len(self.photos[row])}"
        return "No more free slots"

    def display(self):
        output = ['-' * 11]
        for row in range(self.pages):
            how_many_items = len(self.photos[row])
            add_labels = '[] ' * how_many_items
            output.append(add_labels.rstrip())
            output += ['-' * 11]
        return '\n'.join(output)
