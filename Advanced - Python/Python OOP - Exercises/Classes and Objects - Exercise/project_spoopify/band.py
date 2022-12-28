from project.album import Album


class Band:

    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        for album in self.albums:
            if album.name == album_name:
                if album.published:
                    return "Album has been published. It cannot be removed."
                self.albums.remove(album)
                return f"Album {album_name} has been removed."
        return f"Album {album_name} is not found."

    def details(self):
        output = [f"Band {self.name}"]
        for album in self.albums:
            output.append(f"{album.details()}")
        return '\n'.join(output)


# from project.album import Album
#
#
# class Band:
#
#     def __init__(self, name: str):
#         self.name = name
#         self.albums = []
#
#     def add_album(self, album: Album):
#         if album.name not in [x.name for x in self.albums]:
#             self.albums.append(album)
#             return f"Band {self.name} has added their newest album {album.name}."
#         return f"Band {self.name} already has {album.name} in their library."
#
#     def remove_album(self, album_name: str):
#         for item in self.albums:
#             if item.name == album_name:
#                 if item.published:
#                     return "Album has been published. It cannot be removed."
#                 self.albums.remove(item)
#                 return f"Album {album_name} has been removed."
#         return f"Album {album_name} is not found."
#
#     def details(self):
#         output = [f"Band {self.name}"]
#         for item in self.albums:
#             output.append(item.details())
#         return '\n'.join(output)
