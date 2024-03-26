import pymongo


class Movie:
    """ Класс для представления фильма """

    def __init__(self, title, director, year, genres, rating):
        self.title = title
        self.director = director
        self.year = year
        self.genres = genres
        self.rating = rating

    def save_to_db(self, db):
        """ Сохранение фильма в базу данных """
        movie_data = {
            "title": self.title,
            "director": self.director,
            "year": self.year,
            "genres": self.genres,
            "rating": self.rating
        }
        db.movies.insert_one(movie_data)

    @staticmethod
    def get_movies_by_director(db, director_name):
        """ Получение фильмов по режиссеру """
        return list(db.movies.find({"director": director_name}))
