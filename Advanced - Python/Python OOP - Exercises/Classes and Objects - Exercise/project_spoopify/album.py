from project.song import Song


class Album:

    def __init__(self, name: str, *songs):
        self.name = name
        self.songs = [x for x in songs]
        self.published = False

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return "Cannot add songs. Album is published."
        for all_songs in self.songs:
            if song.name == all_songs.name:
                return f"Song is already in the album."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return "Cannot remove songs. Album is published."
        if song_name not in [x.name for x in self.songs]:
            return "Song is not in the album."
        for item in self.songs:
            if song_name == item.name:
                self.songs.remove(item)
                return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        output = [f"Album {self.name}"]
        for item in self.songs:
            output.append(f"== {item.get_info()}")
        return '\n'.join(output)
