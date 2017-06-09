import omdb, csv, re


def list_of_movies(path):
    movies_list = []
    with open(path, "r") as movie_file:
        movies_list = [movies_list.replace('\n', '') for movies_list in movie_file.readlines()]
    return movies_list


def write_to_txt (file_name, movies):
    invalid_titles = open(file_name, 'w')
    for movie in movies:
        invalid_titles.write(movie+'\n')
    invalid_titles.close()


def in_omdb (movie):
    search = omdb.search(movie) # returns list (with ALL possible names)
    for searched_movie in search:
        if searched_movie['title'].encode('utf-8') == movie:  # exact movie name
            return searched_movie
    return None


def get_item (found_movies, item_to_obtain):
        correct_metascore={}
        invalid_metascore=[]
        for searched_movie in found_movies:
            pattern_abbr = re.compile('[0-9]')
            movie_id = searched_movie['imdb_id']
            movie_info_by_id = omdb.imdbid(movie_id)

            if not re.search(pattern_abbr, movie_info_by_id[item_to_obtain]):
                invalid_metascore.append(searched_movie['title'].encode('utf-8'))
            else:
                correct_metascore[searched_movie['title']] = movie_info_by_id[item_to_obtain]
        return correct_metascore, invalid_metascore


def is_metascore_correct (movie_with_correct_metascore):
    with open('rating_file', 'w') as csvfile:
        csv_header = ['Title', 'Metascore']
        writer2 = csv.DictWriter(csvfile, fieldnames=csv_header)
        writer2.writeheader()
        for k,v in movie_with_correct_metascore.items():
            row_to_write = dict(zip(csv_header, [k,v]))
            writer2.writerow(row_to_write)


if __name__ == "__main__":
    file_names = ['invalid_titles.txt', 'invalid_metascore.txt']
    movie_list = list_of_movies('movie_names')

    all_movies = {}     # dictionary with all movies info from omdb
    for movie in movie_list:
        all_movies[movie] = in_omdb(movie)
    not_found_movie = [movie for movie in all_movies.keys() if all_movies.get(movie) is None] # list of not found movies
    write_to_txt(file_names[0], not_found_movie) # write not found movies to txt

    found_movie = [all_movies[movie] for movie in all_movies.keys() if all_movies.get(movie)]
    write_to_txt('invalid_metascore.txt', get_item(found_movie, 'metascore')[1]) # write ivalid metascore to txt
is_metascore_correct(get_item(found_movie, 'metascore')[0]) #write correct metascore to csv
