from movie_lib import Movie, User, Rating
from recommender import *
from get_data import all_movie_data, ratings_by_id, ratings_by_user, all_user_data, all_rating_data

sample_movie_data = [['1', 'Toy Story (1995)', '01-Jan-1995', '', 'http://us.imdb.com/M/title-exact?Toy%20Story%20(1995)', '0', '0', '0', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['2', 'GoldenEye (1995)', '01-Jan-1995', '', 'http://us.imdb.com/M/title-exact?GoldenEye%20(1995)', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0'], ['3', 'Four Rooms (1995)', '01-Jan-1995', '', 'http://us.imdb.com/M/title-exact?Four%20Rooms%20(1995)', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0'], ['4', 'Get Shorty (1995)', '01-Jan-1995', '', 'http://us.imdb.com/M/title-exact?Get%20Shorty%20(1995)', '0', '1', '0', '0', '0', '1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['5', 'Copycat (1995)', '01-Jan-1995', '', 'http://us.imdb.com/M/title-exact?Copycat%20(1995)', '0', '0', '0', '0', '0', '0', '1', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0'], ['6', 'Shanghai Triad (Yao a yao yao dao waipo qiao) (1995)', '01-Jan-1995', '', 'http://us.imdb.com/Title?Yao+a+yao+yao+dao+waipo+qiao+(1995)', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['7', 'Twelve Monkeys (1995)', '01-Jan-1995', '', 'http://us.imdb.com/M/title-exact?Twelve%20Monkeys%20(1995)', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0'], ['8', 'Babe (1995)', '01-Jan-1995', '', 'http://us.imdb.com/M/title-exact?Babe%20(1995)', '0', '0', '0', '0', '1', '1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['9', 'Dead Man Walking (1995)', '01-Jan-1995', '', 'http://us.imdb.com/M/title-exact?Dead%20Man%20Walking%20(1995)', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['10', 'Richard III (1995)', '22-Jan-1996', '', 'http://us.imdb.com/M/title-exact?Richard%20III%20(1995)', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0']]
sample_movie = ['1', 'Toy Story (1995)', '01-Jan-1995', '', 'http://us.imdb.com/M/title-exact?Toy%20Story%20(1995)', '0', '0', '0', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
sample_movie_242 = [242, 'Kolya (1996)', '24-Jan-1997', 'http://us.imdb.com/M/title-exact?Kolya%20(1996)', 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
sample_movie_objects = [Movie(x) for x in sample_movie_data]

sample_rating_data = [['196', '242', '3'], ['944', '1449', '5'], ['186', '302', '3'], ['22', '377', '1'], ['244', '51', '2'], ['166', '346', '1'], ['298', '474', '4'], ['115', '265', '2'], ['253', '465', '5'], ['305', '451', '3'], ['6', '86', '3'], ['62', '257', '2'], ['286', '1014', '5'], ['200', '222', '5'], ['210', '40', '3'], ['224', '29', '3'], ['303', '785', '3'], ['122', '387', '5'], ['194', '274', '2'], ['291', '1042', '4'], ['234', '1184', '2'], ['119', '392', '4'], ['167', '486', '4'], ['299', '144', '4'], ['291', '118', '2'], ['308', '1', '4'], [196, 242, 3], [63, 242, 3], [226, 242, 5], [154, 242, 3], [306, 242, 5], [296, 242, 4], [34, 242, 5], [271, 242, 4], [201, 242, 4], [209, 242, 4], [35, 242, 2], [354, 242, 5], [199, 242, 5], [113, 242, 2], [1, 242, 5], [173, 242, 5], [360, 242, 4], [234, 242, 4], [14, 242, 4], [309, 242, 4], [331, 242, 4], [21, 242, 3], [111, 242, 4], [439, 242, 5], [355, 242, 4], [204, 242, 5], [145, 242, 5], [30, 242, 5], [463, 242, 2], [144, 242, 4], [417, 242, 3], [2, 242, 5], [497, 242, 1], [523, 242, 5], [12, 242, 5]]
sample_rating_objects = [Rating(x) for x in sample_rating_data]
sample_ratings_by_id = {}
for rating in sample_rating_objects:
    try:
        sample_ratings_by_id[rating.movie_id].append(rating.rating)
    except:
        sample_ratings_by_id[rating.movie_id] = [rating.rating]

sample_user = ['196', '49', 'M', 'writer', '55105']


""" Tests for Movie, User, Rating classes in movie_lib """
def test_Movie__init__():
    test_movie = Movie(sample_movie)
    assert (test_movie.movie_id == 1)
    assert (test_movie.title == 'Toy Story (1995)')
    assert (test_movie.release == '01-Jan-1995')
    assert (test_movie.genre_code == ['0', '0', '0', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'])

def test_Movie_get_name():
    movie_objects = [Movie(x) for x in sample_movie_data]
    assert (Movie.get_name(1, movie_objects) == 'Toy Story (1995)')

def test_Movie_get_movie_ratings_from_object():
    test_movie = Movie(sample_movie_242)
    assert (test_movie.get_movie_ratings_from_object(sample_rating_objects) == [3, 3, 3, 5, 3, 5, 4, 5, 4, 4, 4, 2, 5, 5, 2, 5, 5, 4, 4, 4, 4, 4, 3, 4, 5, 4, 5, 5, 5, 2, 4, 3, 5, 1, 5, 5])

def test_User__init__():
    test_user = User(sample_user)
    assert (test_user.user_id == 196)
    assert (test_user.age == 49)
    assert (test_user.binary_gender_identity == 'M')
    assert (test_user.occupation == 'writer')

def test_Rating__init__():
    test_rating = Rating(sample_rating_data[2])
    assert (test_rating.user_id == 186)
    assert (test_rating.movie_id == 302)
    assert (test_rating.rating == 3)

def test_Rating__str__():
    print(str(sample_rating_objects[3]))
    assert (str(sample_rating_objects[3]) == "22, 377, 1")

def test_get_movie_ratings():
    assert (Rating.get_movie_ratings(242, sample_rating_objects) == [3, 3, 3, 5, 3, 5, 4, 5, 4, 4, 4, 2, 5, 5, 2, 5, 5, 4, 4, 4, 4, 4, 3, 4, 5, 4, 5, 5, 5, 2, 4, 3, 5, 1, 5, 5])

def test_get_user_ratings():
    assert (Rating.get_user_ratings(291, sample_rating_objects) == [(1042, 4), (118, 2)])

def test_get_average_rating():
    assert (Rating.get_average_rating(242, sample_ratings_by_id) == 3.97)


""" Tests for functions in recommender """

def test_get_significantly_rated_movie_ids():
    movie_ids = get_significantly_rated_movie_ids(2, sample_ratings_by_id)
    assert (movie_ids == [242])

def test_get_movie_ids_by_avg_rating():
    ordered_movie_ids = get_movie_ids_by_avg_rating(sample_ratings_by_id)
    print(ordered_movie_ids[:20])
    assert (ordered_movie_ids[0][1] > ordered_movie_ids[9][1])

def test_get_highest_rated_movies():
    movies = get_highest_rated_movies(sample_ratings_by_id.keys(), sample_ratings_by_id, all_movie_data)
    ordered_movie_ids = get_movie_ids_by_avg_rating(sample_ratings_by_id)
    assert (movies == [Movie.get_name(movie[0], all_movie_data) for movie in ordered_movie_ids[:20]])

def test_make_userless_list():
    userless_sample_list = make_userless_list(196, sample_rating_objects, all_movie_data)
    print(userless_sample_list)
    assert(242 not in userless_sample_list)

def test_get_best_movies_for_user():
    movies = get_best_movies_for_user(944, sample_rating_objects, all_movie_data, ratings_by_id)
    assert('Pather Panchali (1955)' not in movies)

def test_get_matched_ratings_for_2_users():
    user_1, user_2 = get_matched_ratings_for_2_users(55, 145, ratings_by_user)
    assert (len(user_1) == len(user_2))

def test_find_like_users():
    like_users = find_like_users(55, ratings_by_user, all_user_data)
    assert (find_euc_dist_of_taste(55, like_users[0], ratings_by_user) > 0.5)

def test_get_ratings_from_like_users():
    dict_by_id = get_ratings_from_like_users([196, 186], ratings_by_user, ratings_by_id)
    assert(242 in dict_by_id.keys())
    assert(3 in dict_by_id[242])

def test_get_recommendations_for_user():
    movies = get_recommendations_for_user(55)
    assert(movies != get_best_movies_for_user(55, all_rating_data, all_movie_data, ratings_by_id))
    assert('Star Wars (1977)' not in movies)
