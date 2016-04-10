import math
from movie_lib import *
from get_data import all_movie_data, all_user_data, all_rating_data, ratings_by_id, ratings_by_user


def get_significantly_rated_movie_ids(cutoff, ratings_by_id):
    significantly_rated_movies = []
    for key in ratings_by_id:
        if len(ratings_by_id[key]) >= cutoff:
            significantly_rated_movies.append(key)
    return significantly_rated_movies


significantly_rated_movie_ids = get_significantly_rated_movie_ids(5, ratings_by_id)


def get_movie_ids_by_avg_rating(ratings_by_id):
    # returns a sorted list of tuples (movie_id, avg rating)
    movie_id_avg_rating_list = [(movie_id, Rating.get_average_rating(movie_id, ratings_by_id)) for movie_id in ratings_by_id]
    return sorted(movie_id_avg_rating_list, key=lambda movie_and_rating: movie_and_rating[1], reverse=True)


def get_highest_rated_movies(movie_id_list, ratings_by_id, movie_object_list):
    # takes a list of movie_ids (like significantly rated ones or ones that a user has not rated), a dicts of ratings, and movie objects for getting titles.
    # returns a list of movie titles
    movie_ratings = []

    movie_ids_by_avg_rating = get_movie_ids_by_avg_rating(ratings_by_id)
    # print([len(ratings_by_id[key]) for key in ratings_by_id if key in movie_id_list])
    movie_names_in_order = [Movie.get_name(tuple_thing[0], movie_object_list) for tuple_thing in movie_ids_by_avg_rating if tuple_thing[0] in movie_id_list]

    return movie_names_in_order[:20]


def make_userless_list(user_id, all_rating_data, all_movie_data):
    # returns a list of movie ids for movies that the user has not rated
    list_of_movie_ids_and_ratings = Rating.get_user_ratings(user_id, all_rating_data)
    list_of_movie_ids = [rating_tuple[0] for rating_tuple in list_of_movie_ids_and_ratings]
    list_of_movie_ids_user_has_not_rated = [movie.movie_id for movie in all_movie_data if movie.movie_id not in list_of_movie_ids]
    return list_of_movie_ids_user_has_not_rated


def get_best_movies_for_user(user_id, rating_data, movie_data, ratings_by_id):
    userless_ids = make_userless_list(user_id, rating_data, movie_data)

    userless_ids = [movie_id for movie_id in userless_ids if movie_id in (get_significantly_rated_movie_ids(5, ratings_by_id))]

    return get_highest_rated_movies(userless_ids, ratings_by_id, movie_data)



def get_matched_ratings_for_2_users(user_id_1, user_id_2, ratings_by_user):
    user_1_ratings = ratings_by_user[user_id_1]
    user_2_ratings = ratings_by_user[user_id_2]
    # user_1_ratings = Rating.get_user_ratings(user_id_1, all_rating_data)
    # user_2_ratings = Rating.get_user_ratings(user_id_2, all_rating_data)
    user_1_ratings.sort(key=lambda x: x[0])
    user_2_ratings.sort(key=lambda x: x[0])

    movie_ids_in_both = [x[0] for x in user_1_ratings for y in user_2_ratings if x[0] == y[0]]
    user_1_matched_ratings = [x[1] for x in user_1_ratings if x[0] in movie_ids_in_both]
    user_2_matched_ratings = [x[1] for x in user_2_ratings if x[0] in movie_ids_in_both]
    return user_1_matched_ratings, user_2_matched_ratings


def euclidean_distance(v, w):
    """Given two lists, give the Euclidean distance between them on a scale
    of 0 to 1. 1 means the two lists are identical.
    """

    # Guard against empty lists.
    if len(v) is 0:
        return 0

    # Note that this is the same as vector subtraction.
    differences = [v[idx] - w[idx] for idx in range(len(v))]
    squares = [diff ** 2 for diff in differences]
    sum_of_squares = sum(squares)

    return 1 / (1 + math.sqrt(sum_of_squares))


def find_euclidean_distance_of_taste(user_id_1, user_id_2, ratings_by_user):
    list_1, list_2 = get_matched_ratings_for_2_users(user_id_1, user_id_2, ratings_by_user)
    return euclidean_distance(list_1, list_2)

# print(find_euclidean_distance_of_taste(196, 244, all_rating_data))


def find_like_users(user_1, ratings_by_user, all_user_data):
    list_of_euc_dist = []
    for user in all_user_data:
        if user.user_id != user_1:
            euc_dist = find_euclidean_distance_of_taste(user_1, user.user_id, ratings_by_user)
            list_of_euc_dist.append((user.user_id, euc_dist))

    list_of_euc_dist.sort(key=lambda x: x[1], reverse=True)
    return [x[0] for x in list_of_euc_dist if x[1] > 0.5]

# find_like_users(196, ratings_by_user, all_user_data)

def get_ratings_from_like_users(like_users, ratings_by_user, ratings_by_id):
    like_user_rating_tuples = [rating_tuple for user in like_users for rating_tuple in ratings_by_user[user]]

    dict_of_ratings_by_id = {}
    for movie in ratings_by_id:
        for rating_tuple in like_user_rating_tuples:
            if movie == rating_tuple[0]:
                try:
                    dict_of_ratings_by_id[movie].append(rating_tuple[1])
                except:
                    dict_of_ratings_by_id[movie] = [rating_tuple[1]]

    return dict_of_ratings_by_id

def get_recommendations_for_user(user_id, ratings_by_user=ratings_by_user, ratings_by_id=ratings_by_id, rating_data=all_rating_data, movie_data=all_movie_data):

    users_like_user = find_like_users(user_id, ratings_by_user, all_user_data)

    like_user_ratings_by_id = get_ratings_from_like_users(users_like_user, ratings_by_user, ratings_by_id)

    return get_best_movies_for_user(user_id, rating_data, movie_data, like_user_ratings_by_id)

# print(get_recommendations_for_user(196))
