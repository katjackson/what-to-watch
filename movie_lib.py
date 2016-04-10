import csv

class Movie():

    def __init__(self, movie_data):
        self.movie_id = int(movie_data[0])
        self.title = movie_data[1]
        self.release = movie_data[2]
        self.imdb = movie_data[4]
        self.genre_code = movie_data[5:]

    @staticmethod
    def get_name(movie_id, list_of_movie_objects):
        for movie_object in list_of_movie_objects:
            if movie_object.movie_id == movie_id:
                return movie_object.title

    def get_movie_ratings_from_object(self, rating_data):
        return [rating_object.rating for rating_object in rating_data if rating_object.movie_id == self.movie_id]


class User():

    def __init__(self, user_data):
        self.user_id = int(user_data[0])
        self.age = int(user_data[1])
        self.binary_gender_identity = user_data[2]
        self.occupation = user_data[3]



class Rating():

    def __init__(self, rating_data):
        self.user_id = int(rating_data[0])
        self.movie_id = int(rating_data[1])
        self.rating = int(rating_data[2])

    def __str__(self):
        return "{} | {} | {}".format(self.user_id, self.movie_id, self.rating)

    def list(self):
        return [self.user_id, self.movie_id, self.rating]

    @staticmethod
    def get_movie_ratings(movie_id, list_of_rating_objects):
        list_of_ratings = [rating_object.rating for rating_object in list_of_rating_objects if rating_object.movie_id == movie_id]
        return list_of_ratings

    @staticmethod
    def get_user_ratings(user_id, list_of_rating_objects):
        list_of_movie_ids_and_ratings = [(rating_object.movie_id, rating_object.rating) for rating_object in list_of_rating_objects if rating_object.user_id == user_id]
        return list_of_movie_ids_and_ratings

    @staticmethod
    def get_average_rating(movie_id, ratings_by_id_dict):
        average = sum(ratings_by_id_dict[movie_id]) / len(ratings_by_id_dict[movie_id])
        return round(average, 2)


    # @staticmethod
    # def get_average_rating(movie_id, list_of_rating_objects):
    #     list_of_ratings = Rating.get_movie_ratings(movie_id, list_of_rating_objects)
    #     average = sum(list_of_ratings) / len(list_of_ratings)
    #     return round(average, 2)
