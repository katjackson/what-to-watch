from movie_lib import Movie, User, Rating
import recommender

sample_movie_data = [['1', 'Toy Story (1995)', '01-Jan-1995', '', 'http://us.imdb.com/M/title-exact?Toy%20Story%20(1995)', '0', '0', '0', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['2', 'GoldenEye (1995)', '01-Jan-1995', '', 'http://us.imdb.com/M/title-exact?GoldenEye%20(1995)', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0'], ['3', 'Four Rooms (1995)', '01-Jan-1995', '', 'http://us.imdb.com/M/title-exact?Four%20Rooms%20(1995)', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0'], ['4', 'Get Shorty (1995)', '01-Jan-1995', '', 'http://us.imdb.com/M/title-exact?Get%20Shorty%20(1995)', '0', '1', '0', '0', '0', '1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['5', 'Copycat (1995)', '01-Jan-1995', '', 'http://us.imdb.com/M/title-exact?Copycat%20(1995)', '0', '0', '0', '0', '0', '0', '1', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0'], ['6', 'Shanghai Triad (Yao a yao yao dao waipo qiao) (1995)', '01-Jan-1995', '', 'http://us.imdb.com/Title?Yao+a+yao+yao+dao+waipo+qiao+(1995)', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['7', 'Twelve Monkeys (1995)', '01-Jan-1995', '', 'http://us.imdb.com/M/title-exact?Twelve%20Monkeys%20(1995)', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0'], ['8', 'Babe (1995)', '01-Jan-1995', '', 'http://us.imdb.com/M/title-exact?Babe%20(1995)', '0', '0', '0', '0', '1', '1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['9', 'Dead Man Walking (1995)', '01-Jan-1995', '', 'http://us.imdb.com/M/title-exact?Dead%20Man%20Walking%20(1995)', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['10', 'Richard III (1995)', '22-Jan-1996', '', 'http://us.imdb.com/M/title-exact?Richard%20III%20(1995)', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0']]
sample_movie = ['1', 'Toy Story (1995)', '01-Jan-1995', '', 'http://us.imdb.com/M/title-exact?Toy%20Story%20(1995)', '0', '0', '0', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
sample_movie_242 = [242, 'Kolya (1996)', '24-Jan-1997', 'http://us.imdb.com/M/title-exact?Kolya%20(1996)', 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
sample_movie_objects = [Movie(x) for x in sample_movie_data]

sample_rating_data = [['196', '242', '3'], ['186', '302', '3'], ['22', '377', '1'], ['244', '51', '2'], ['166', '346', '1'], ['298', '474', '4'], ['115', '265', '2'], ['253', '465', '5'], ['305', '451', '3'], ['6', '86', '3'], ['62', '257', '2'], ['286', '1014', '5'], ['200', '222', '5'], ['210', '40', '3'], ['224', '29', '3'], ['303', '785', '3'], ['122', '387', '5'], ['194', '274', '2'], ['291', '1042', '4'], ['234', '1184', '2'], ['119', '392', '4'], ['167', '486', '4'], ['299', '144', '4'], ['291', '118', '2'], ['308', '1', '4'], [196, 242, 3], [63, 242, 3], [226, 242, 5], [154, 242, 3], [306, 242, 5], [296, 242, 4], [34, 242, 5], [271, 242, 4], [201, 242, 4], [209, 242, 4], [35, 242, 2], [354, 242, 5], [199, 242, 5], [113, 242, 2], [1, 242, 5], [173, 242, 5], [360, 242, 4], [234, 242, 4], [14, 242, 4], [309, 242, 4], [331, 242, 4], [21, 242, 3], [111, 242, 4], [439, 242, 5], [355, 242, 4], [204, 242, 5], [145, 242, 5], [30, 242, 5], [463, 242, 2], [144, 242, 4], [417, 242, 3], [2, 242, 5], [497, 242, 1], [523, 242, 5], [12, 242, 5]]
sample_rating_objects = [Rating(x) for x in sample_rating_data]

sample_ratings_by_id = {}
for rating in sample_rating_objects:
    try:
        sample_ratings_by_id[rating.movie_id].append(rating.rating)
    except:
        sample_ratings_by_id[rating.movie_id] = [rating.rating]


def test_Movie__init__():
    test_movie = Movie(sample_movie)
    assert (test_movie.movie_id == 1)
    assert (test_movie.title == 'Toy Story (1995)')
    assert (test_movie.release == '01-Jan-1995')
    assert (test_movie.genre_code == ['0', '0', '0', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'])


def test_get_name():
    movie_objects = [Movie(x) for x in sample_movie_data]
    assert (Movie.get_name(1, movie_objects) == 'Toy Story (1995)')

def test_get_movie_ratings_from_object():
    test_movie = Movie(sample_movie_242)
    assert (test_movie.get_movie_ratings_from_object(sample_rating_objects) == [3, 3, 3, 5, 3, 5, 4, 5, 4, 4, 4, 2, 5, 5, 2, 5, 5, 4, 4, 4, 4, 4, 3, 4, 5, 4, 5, 5, 5, 2, 4, 3, 5, 1, 5, 5])

def test_get_movie_ratings():
    assert (Rating.get_movie_ratings(242, sample_rating_objects) == [3, 3, 3, 5, 3, 5, 4, 5, 4, 4, 4, 2, 5, 5, 2, 5, 5, 4, 4, 4, 4, 4, 3, 4, 5, 4, 5, 5, 5, 2, 4, 3, 5, 1, 5, 5])

def test_get_user_ratings():
    assert (Rating.get_user_ratings(291, sample_rating_objects) == [(1042, 4), (118, 2)])

def test_get_average_rating():
    assert (Rating.get_average_rating(242, sample_ratings_by_id) == 3.97)


def test_make_userless_list():
    userless_sample_list = recommender.make_userless_list(196, sample_rating_objects, sample_movie_objects)
    print(userless_sample_list)
    assert(242 not in userless_sample_list)


"""
Rating:
init, str, list
User:
init


recommender
get_significantly_rated_movie_ids
get_movie_ids_by_avg_rating
get_highest_rated_movies
get_best_movies_for_user
get_matched_ratings_for_2_users
find_euclidean_distance_of_taste
get_ratings_from_like_users
get_recommendations_for_user

What should i watch:
return_to_menu
print_movies
"""
