class Song:
  count = 0  # Class attribute to track total songs
  genres = []  # Class attribute to store unique genres
  artists = []  # Class attribute to store unique artists
  genre_count = {}  # Class attribute to track genre count
  artist_count = {}  # Class attribute to track artist count

  def __init__(self, name, artist, genre):
    self.name = name
    self.artist = artist
    self.genre = genre
    Song.add_song_to_count()  # Call class method to increment count
    Song.add_to_genres(genre)  # Add genre to unique genres list
    Song.add_to_artists(artist)  # Add artist to unique artists list
    Song.add_to_genre_count(genre)  # Update genre count
    Song.add_to_artist_count(artist)  # Update artist count

  @classmethod
  def add_song_to_count(cls):
    cls.count += 1

  @classmethod
  def add_to_genres(cls, genre):
    if genre not in cls.genres:
      cls.genres.append(genre)

  @classmethod
  def add_to_artists(cls, artist):
    if artist not in cls.artists:
      cls.artists.append(artist)

  @classmethod
  def add_to_genre_count(cls, genre):
    if genre in cls.genre_count:
      cls.genre_count[genre] += 1
    else:
      cls.genre_count[genre] = 1

  @classmethod
  def add_to_artist_count(cls, artist):
    if artist in cls.artist_count:
      cls.artist_count[artist] += 1
    else:
      cls.artist_count[artist] = 1

