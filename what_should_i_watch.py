import os
import math
from movie_lib import *
from get_data import all_movie_data, all_user_data, all_rating_data, ratings_by_id, ratings_by_user
from recommender import *

# significantly_rated_movie_ids = get_significantly_rated_movie_ids(5, ratings_by_id)

def clear():
    return os.system('clear')

def display_menu():
    print('\n')
    print('MENU')
    print('1. View most popular movies of all time')
    print("2. View great movies I haven't seen yet")
    print('3. View movie recommendations just for me')
    print("Enter 'x' to exit")
    print('\n')


def return_to_menu():
    if input('\n Press any key to return to the menu: '):
        clear()
        return True

def print_movies(movies):
    print('\n')
    for i, movie in enumerate(movies):
        print(i + 1, movie)



def main():

    clear()
    print('\n')
    print('WHAT FUCKING MOVIE SHOULD I WATCH?'.center(80, '-'))
    print('\n')

    user_id = 0

    while not 0 < user_id < 945:
        input_value = input("Please enter your user_id: ")

        try:
            user_id = int(input_value)
        except:
            continue
    while True:

        display_menu()

        version = input("What do you want to do? ")
        clear()
        if version == '1':
            #show most popular movies
            movies = get_highest_rated_movies(significantly_rated_movie_ids, ratings_by_id, all_movie_data)

        elif version == '2':
            #view best unseen movies
            movies = get_best_movies_for_user(user_id, all_rating_data, all_movie_data, ratings_by_id)

        elif version == '3':
            #view personal recommendations
            movies = get_recommendations_for_user(user_id)

        elif version.lower() == 'x':
            break

        print_movies(movies)
        return_to_menu()

        continue




if __name__ == '__main__':
    main()
