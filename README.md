## Movie Recommendations

The purpose of this project is to recommend movies based on MovieLens data. The program reccommends movies to a specific user from the MovieLens dataset. This is a command line program that was created without the help of pandas or relational databases. This project was written in Python3 and can be used by running what_should_i_watch.py from the command line. To use the program, clone the repository and pick a user id (between 1 - 943) to check it out.

### What Should I Watch
This file contains the user interface for 'WHAT FREAKING MOVIE SHOULD I WATCH'. After providing their id number, a user can see the top rated movies, top rated movies they have not seen yet, or more personalized recommendations. This is the best user interface I can make. Sorry.

#### Get Data
This file takes in movie, ratings, and user info from MovieLens and stores it in useful classes and dictionaries.
all_movie_data is a list of Movie class objects.
all_user_data is a list of User class objects.
all_rating_data is a list of Rating class objects.
ratings_by_id is a dictionary of ratings sorted by movie id.
ratings_by_user is a dictionary of tuples of movies and their ratings sorted by user.

#### Movie Lib
This file contains the classes Move, User, and Rating. In addition to initializing class objects with helpful variables, there are several static methods that allow you to manipulate lists of class objects.

#### Recommender
This file contains a whole mess of functions that manipulate the movie, rating, and user data. Here you will find functions that return the top rated movies of the data set, movies with more than n ratings, and movies a user has not yet rated. Using a formula for euclidean distance, you can compare users tastes and return recommendations based on like users ratings.
