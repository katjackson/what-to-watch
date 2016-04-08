import csv
from movie_lib import Movie, Rating, User

all_rating_data = []

with open('u.data', encoding='latin_1') as ratings_file:
    reader = csv.reader(ratings_file, delimiter='\t')
    for row in reader:
        rating = Rating(row)
        all_rating_data.append(rating)


all_movie_data = []
dict_of_ratings = {}

with open('u.item', encoding='latin_1') as movie_file:
    reader = csv.reader(movie_file, delimiter='|')
    for row in reader:
        movie = Movie(row)
        all_movie_data.append(movie)
        dict_of_ratings[movie.movie_id] = movie.get_movie_ratings_from_object(all_rating_data)

# print(Movie.get_name(242, all_movie_data))
# print(all_movie_data[:10])


all_user_data = []

with open('u.user', encoding='latin_1') as user_file:
    reader = csv.reader(user_file, delimiter='|')
    for row in reader:
        user = User(row)
        all_user_data.append(user)







# dict_of_ratings = {movie.movie_id: (movie.get_movie_ratings_from_object(all_rating_data)) for movie in all_movie_data}

# print([x.movie_id for x in all_rating_data[:10]])
# print([str(x) for x in all_rating_data[:10]])
# print([[x.user_id, x.movie_id, x.rating] for x in all_rating_data[:25]])
# print([[x.user_id, x.movie_id, x.rating] for x in all_rating_data if x.movie_id == 242])
# rating_objects_for_movie_18_n_19 = [rating_object for rating_object in all_rating_data if (17 < int(rating_object.movie_id) < 20)]
#
# print(rating_objects_for_movie_18_n_19)

# all_ratings_for_movie_22 = []
#
# for rating_object in all_rating_data:
#     if rating_object.movie_id == '22':
#         all_ratings_for_movie_22.append(rating_object.rating)
#
# print(all_ratings_for_movie_22)
