
import omdb
import csv


path_to_input_file = 'movie_names'
path_to_good_movies_file = 'rating1.csv'
path_to_invalid_titles_file = 'invalid_titles1.txt'
path_to_invalid_metascore_file = 'invalid_metascore1.txt'


def readDataFromFileIntoList(pathToFile):
    movieList = []
    with open(pathToFile) as inputFile:
        for line in inputFile:
            movieList.append(line)
    inputFile.close()
    return movieList


def getMovieData(movieList):
    movieData = {}
    i=0
    for item in movieList:
        i=i+1
        print i,":  "+item
        dataItem = omdb.search(str(item).rstrip())
        movieData.update({str(item).rstrip(): dataItem or ''})
    return movieData


def getMovieScore(movieData):
    print '###################'
    print 'Now we are calculating the score'
    invalid_metascore = []
    good_movies = []
    i=0

    for key, value in movieData.iteritems():
        movieFound = False
        i = i + 1
        print i
        if value == '':
            continue
        else:
            for movieMetaData in value:
                if movieMetaData['title'].encode('utf-8') == key and (movieMetaData['type'] == 'movie' or movieMetaData['type'] == 'series'):
                    movieFound = True
                    imdb_metascore = omdb.imdbid(movieMetaData['imdb_id'])['metascore'] or ''
                    if imdb_metascore == 'N/A' or not imdb_metascore.isdigit():
                        invalid_metascore.append(key)
                    else:
                        good_movies.append({key : imdb_metascore})
                    break
            if movieFound == False:
                invalid_metascore.append(key)
    return invalid_metascore, good_movies


def getInvalidTitles(movieData):
    list_of_invalid_titles = []
    for key, value in movieData.iteritems():
        if value == '':
            list_of_invalid_titles.append(key)
    return list_of_invalid_titles


if __name__ == '__main__':

    movieList = readDataFromFileIntoList(path_to_input_file)
    movieData = getMovieData(movieList)  # get dict of movie_title with metadata from input file
    invalid_titles = getInvalidTitles(movieData)
    differentMovies = getMovieScore(movieData)
    invalid_metascore = differentMovies[0]   #getMovieScore(movieData)[0]
    good_movies = differentMovies[1]       #getMovieScore(movieData)[1]

    with open(path_to_invalid_metascore_file,'w') as invalid_m:
        for item in invalid_metascore:
            invalid_m.write(item+'\n')
    invalid_m.close()

    with open(path_to_invalid_titles_file,'w') as invalid_t:
        for item in invalid_titles:
            invalid_t.write(item+'\n')
    invalid_t.close()

    with open(path_to_good_movies_file,'wb') as good_m:
        writer = csv.writer(good_m, delimiter=',')
        writer.writerow(('Title', 'Metascore'))
        for item in good_movies:
            for key in item:
                writer.writerow((key, ' ' + item[key]))
    good_m.close()
