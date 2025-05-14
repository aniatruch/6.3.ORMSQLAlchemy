import random

class Video:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre
        self.plays = 0

    def play(self, count=1):
        self.plays += count

    def __str__(self):
        return f"{self.title} ({self.year})"

class Movie(Video):
    pass

class Series(Video):
    def __init__(self, title, year, genre, season, episode):
        super().__init__(title, year, genre)
        self.season = season
        self.episode = episode

    def __str__(self):
        return f"{self.title} S{self.season:02d}E{self.episode:02d}"

# Biblioteka tytułów
library = []

def get_movies():
    return sorted([item for item in library if isinstance(item, Movie)], key=lambda x: x.title)

def get_series():
    return sorted([item for item in library if isinstance(item, Series)], key=lambda x: x.title)

def search(title):
    return [item for item in library if title.lower() in item.title.lower()]

def generate_views():
    item = random.choice(library)
    views = random.randint(1, 100)
    item.play(views)

def run_generate_views(times=10):
    for _ in range(times):
        generate_views()

def top_titles(n=3, content_type=None):
    if content_type == "movies":
        items = get_movies()
    elif content_type == "series":
        items = get_series()
    else:
        items = library
    return sorted(items, key=lambda x: x.plays, reverse=True)[:n]

# Dodawanie tytułów do biblioteki
library.append(Movie("Pulp Fiction", 1994, "Crime"))
library.append(Movie("Inception", 2010, "Sci-Fi"))
library.append(Series("The Simpsons", 1989, "Animation", 1, 5))
library.append(Series("Breaking Bad", 2008, "Drama", 2, 3))
library.append(Series("Breaking Bad", 2008, "Drama", 2, 4))

if __name__ == "__main__":
    run_generate_views()
    
    print("Najpopularniejsze tytuły:")
    for item in top_titles(5):
        print(f"{item} - {item.plays} odtworzeń")

    print("\nFilmy:")
    for movie in get_movies():
        print(movie)

    print("\nSeriale:")
    for series in get_series():
        print(series)

    print("\nWyniki wyszukiwania dla 'breaking':")
    for result in search("breaking"):
        print(result)