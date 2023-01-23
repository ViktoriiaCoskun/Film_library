import random
import time
class Movies:

    def __init__(self, name, graduation_year, genre, number_of_views):
       self.name = name
       self.graduation_year = graduation_year
       self.genre = genre
       self.number_of_views = number_of_views
       
       self.content_type="movie"

    def play (self):
        self.number_of_views=self.number_of_views+1

    def __str__(self):
        return f'{self.name} ({self.graduation_year})'    

class Series(Movies):
    def __init__(self, series_number, season_number, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.series_number = series_number
       self.season_number = season_number
       self.content_type="series"

    def play (self):
        self.number_of_views=self.number_of_views+1

    def __str__(self):
        episode="S"+self.season_number+"E"+self.series_number
        return f'{self.name} {episode}'  
#To the class representing the series, add an external function that will display the number of episodes of a particular series available in the library.
    def number_of_episodes(self):
        return self.series_number
        

library=[]

def storeInLibrary(content_type,name,graduation_year, genre, number_of_views,series_number, season_number):
    if content_type=="movie":
        movie=Movies(name, graduation_year, genre, number_of_views)
        library.append(movie)
    elif content_type=="series":
        series=Series(series_number, season_number,name,graduation_year, genre, number_of_views)
        library.append(series)
#Write functions get_movies and get_series that will filter the list and return only movies and TV shows, respectively. Sort the received list alphabetically.
def get_Movies():
    movieList=[]
    for movie in library:
        if movie.content_type=="movie":
            movieList.append(movie)
    
    by_name = sorted(movieList, key=lambda movies:movies.name)

   # for item in range(len(movieList)):
   #     print(by_name[item])
    return by_name

def get_Series():
    seriesList=[]
    for series in library:
        if series.content_type=="series":
            seriesList.append(series)
    
    by_name = sorted(seriesList, key=lambda item:item.name)

    #for item in range(len(seriesList)):
    #    print(by_name[item])
    return by_name
#Write a function searchthat will search for a movie or TV series by name.
def search(type,name):
        if type=="series":
           seriesList= get_Series()
           for item in seriesList:
                if item.name==name:
                    print("Search performed!",item)
        elif type=="movie":
           movieList= get_Movies()
           for item in movieList:
                if item.name==name:
                    print("Search performed!",item)

#Write a function generate_views that randomly selects an item from the library and then adds a random (range 1 to 100) number of reproductions.
def generate_views():
    random_item = random.randint(0,len(library)-1)
    random_view= random.randint(1,100)
    library[random_item].number_of_views=random_view
    #print(library[random_item],"Number of Views:",library[random_item].number_of_views)

#Write a function that will run generate_views10 times
def run_views():
    for index in range(10):
        generate_views()

#Write a function top_titles()that will return a selected number of the most popular titles from the library.
#  For those who want: add a parameter to the function content_type, with which you can choose whether certain movies or series should be shown.

def top_titles(content_type,top_limit):
    itemList=[]
    if(content_type=="movie"):
        movieList= get_Movies()
        itemList = sorted(movieList,reverse=True, key=lambda movies:movies.number_of_views)
    elif(content_type=="series"):
        seriesList= get_Series()
        itemList = sorted(seriesList,reverse=True, key=lambda movies:movies.number_of_views)

    for item in range(top_limit):
        #print(item+1,". ",itemList[item]," viewed ",itemList[item].number_of_views ,"times")
        print(item+1,". ",itemList[item])
    print()
#Write a function that uses a loop to add complete seasons of a TV series to a library.
#  The function should accept parameters such as: series name, release year, genre, season number, number of series to add.
def add_complete_seasons(series_name,release_year, genre,series_number, season_number):
    for season in range(1,season_number+1):
        for episode in range(1,series_number+1):
            episode_no=str(episode)
            season_no=str(season)
            if episode<10:episode_no="0"+episode_no
            if season<10:season_no="0"+season_no
            storeInLibrary("series",series_name,release_year,genre,50,episode_no,season_no)

#A message 'Film Library' will appear on the console.
print("Film Library")

# Fill the library with content.
add_complete_seasons("Game Of Thrones","2011","Drama",10,8)
storeInLibrary("movie","The Shawshank Redemption","1994","Drama",95,0,0) 
storeInLibrary("movie","Pulp Fiction","1994","Sci-Fi",50,0,0)
storeInLibrary("movie","The Godfather","1972","Crime,Drama",96,0,0)
storeInLibrary("series","Simpsons","1994","Sci-Fi",50,"01","02")


# A rendering of the content using the function will be created generate_views.
run_views()

# A message will appear on the consoleНайпопулярніші фільми та серіали дня <data>``, де` is the current date in DD.MM.YYYY format.
time_string = time.strftime("%d.%m.%Y", time.localtime())




# It will show us the 3 most popular titles.
print("Top Movies of the Day ",time_string)
top_titles("movie",3)
print("Top TV Shows of the Day ",time_string)
top_titles("series",3)

#test search 
#search("series","Simpsons")

#test number_of_episodes()
#serial=get_Series()
#print(serial[0],serial[0].number_of_episodes())



