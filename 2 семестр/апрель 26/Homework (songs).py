class Playlist:
    def __init__(self, name: str):
        self._name = name
        self._songs: list[Song] = []

    def add_song(self, song: "Song"):
        self._songs.append(song)

    def __repr__(self):
        return f"playlist {self._name} contains: {self._songs}"

class Album:
    def __init__(self, title: str, artist: "Artist", year: int):
        self._title = title
        self._artist = artist
        self._year = year
        self._tracks: list[Song] = []
        self._track_num = 0

    def add_track(self, title: str):
        self._track_num += 1
        self._tracks.append(Song(title, self._artist, self, self._track_num))

    def get_song(self, name: str):
        song = next((song for song in self._tracks if song.get_song_name() == name), None)
        if song is None:
            print(f"трека {name} нет в альбоме {self._title}")
        else: return song
    def __repr__(self):
        return f"Album: {self._title}, artist: {self._artist}, tracks: {self._tracks}"


class Song:
    def __init__(self, title: str, artist: "Artist", album: "Album", track_number):
        self._title = title
        self._artist = artist
        self._album = album
        self._track_number = track_number

    def get_song_name(self) -> str:
        return self._title

    def add_track_for_artist(self):
        self._artist.add_song(self)

    def __repr__(self):
        return self._title

class Artist:
    def __init__(self, name: str):
        self._name = name
        self._albums: list[Album] = []
        self._songs: list[Album] = []

    def add_album(self, album):
        self._albums.append(album)

    def add_song(self, song):
        self._songs.append(song)

    def __repr__(self):
        return self._name


if __name__ == "__main__":
    Derbenev = Artist("Kostik")
    album_1 = Album("im_looser", Derbenev, 2035)
    album_1.add_track("Bombordilo")
    album_1.add_track("Krokodilo")
    print(album_1)
    my_playlist = Playlist("Hardbass")
    my_playlist.add_song(album_1.get_song("Bombordilo"))
    my_playlist.add_song(album_1.get_song("test_for_error"))
    print(my_playlist)
