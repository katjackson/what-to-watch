from movie_lib import *
from get_data import all_movie_data, all_user_data, all_rating_data, dict_of_ratings


dict_of_more_than_4_ratings = {key: dict_of_ratings[key] for key in dict_of_ratings if len(dict_of_ratings[key]) >= 5}


def get_highest_rated_movies():
    highest_rated_movies = []

    for movie in all_movie_data:
        avg_rating = Rating.get_average_rating(movie.movie_id, all_rating_data)


    return highest_rated_movies

# return top 10 movies by avg rating with avg rating

# def main():
#
#
# if __name__ == '__main__':
#     main()
