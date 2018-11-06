#!/usr/bin/env python
# Name: Jacob Vermeule
# Student number: 11328622
"""
This script scrapes IMDB and outputs a CSV file with highest rated movies.
"""

import csv
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
soup = BeautifulSoup
TARGET_URL = "https://www.imdb.com/search/title?title_type=feature&release_date=2008-01-01,2018-01-01&num_votes=5000,&sort=user_rating,desc"
BACKUP_HTML = 'movies.html'
OUTPUT_CSV = 'movies.csv'


def extract_movies(dom):
    """
    Extract a list of highest rated movies from DOM (of IMDB page).
    Each movie entry should contain the following fields:
    - Title
    - Rating
    - Year of release (only a number!)
    - Actors/actresses (comma separated if more than one)
    - Runtime (only a number!)
    """

    # initiate list for titles
    titles = []

    # open html
    html_file = open("movies.html", 'r')
    page = soup(html_file.read(), features="html.parser")

    # skip over first two titles
    itermovie = iter(page.find_all("img"))
    next(itermovie)
    next(itermovie)

    # append movietitles to list
    for movie in itermovie:
        titles.append(movie.get("alt"))

    # initiate ratings
    ratings = []

    # find all ratings and append to list
    for movie in page.find_all("div"):
        if movie.get("data-value") != None:
            ratings.append(movie.get("data-value"))

    # initiate year of release list
    year_of_release = []

    # go to location of years of release
    for movie in page.find_all("span"):
        if movie.get("class") == ['lister-item-year', 'text-muted', 'unbold']:
            for i in movie:
                for j in i:

                    # check if year is found
                    if j.isdigit():
                        year_of_release.append(j)

    # make new list with combined digits
    years_of_release = []
    for i in range(0, len(year_of_release), 4):
        years_of_release.append(year_of_release[i] + year_of_release[i+1] + year_of_release[i+2] + year_of_release[i+3])

    # initiate actors in list
    actors = []

    # create seperate list per movie
    movie_actor = []

    # distinction in html where actors exist
    x = 'st_0'
    y = 'st_1'
    z = 'st_2'
    a = 'st_3'

    # loop over html page where actors are
    for movie in page.find_all("a"):
        if x in movie.get("href"):

            # append actors per movie to list
            for i in movie:
                movie_actor.append(i)

        elif y in movie.get("href"):
            for j in movie:
                movie_actor.append(j)

        elif z in movie.get("href"):
            for k in movie:
                movie_actor.append(k)

        # append every movie to bigger list
        elif a in movie.get("href"):
            for l in movie:
                movie_actor.append(l)
                actors.append(movie_actor)

                # empty list
                movie_actor = []

        # one movie (Its a beautiful day) does not have actors, movie 43
        elif len(actors) == 42:
            actors.append(None)

    # initiate list
    runtime = []

    # find location of runtime
    for movie in page.find_all("span"):
        if movie.get("class") == ['runtime']:

            # append number to list
            for i in movie:
                runtime.append(i.split()[0])

    # create list of all movie elements
    almost_final_list = [titles, ratings, years_of_release, actors, runtime]

    # initiate final list
    final_list = []

    # change rows to columns to create 50 rows.
    for i in range(0, 49):
        final_list.append([[item[i] for item in almost_final_list]])

    return final_list


def save_csv(outfile, movies):
    """
    Output a CSV file containing highest rated movies.
    """

    with open('movies.csv', 'w', newline='') as myfile:
       wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
       wr.writerow(['Title', 'Rating', 'Year', 'Actors', 'Runtime'])
       wr.writerows(zip(extract_movies(dom)))
    # ADD SOME CODE OF YOURSELF HERE TO WRITE THE MOVIES TO DISK


def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None
    except RequestException as e:
        print('The following error occurred during HTTP GET request to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns true if the response seems to be HTML, false otherwise
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


if __name__ == "__main__":

    # get HTML content at target URL
    html = simple_get(TARGET_URL)

    # save a copy to disk in the current directory, this serves as an backup
    # of the original HTML, will be used in grading.
    with open(BACKUP_HTML, 'wb') as f:
        f.write(html)

    # parse the HTML file into a DOM representation
    dom = BeautifulSoup(html, 'html.parser')

    # extract the movies (using the function you implemented)
    movies = extract_movies(dom)

    # write the CSV file to disk (including a header)
    with open(OUTPUT_CSV, 'w', newline='') as output_file:
        save_csv(output_file, movies)
