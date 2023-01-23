import random
class Movies:

    def __init__(self, name, graduation_year, genre, number_of_views):
       self.name = name
       self.graduation_year = graduation_year
       self.genre = genre
       self.number_of_views = number_of_views
       
       self.content_type="movie"

#Movies and TV shows have a method play that increments the number of views of a given title by 1.
    def play (self):
        self.number_of_views=self.number_of_views+1

#After displaying the movie as a string, the name and year of release are displayed, for example, "Pulp Fiction (1994)".
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

#After viewing the series, information about a certain series is displayed in the form of a string, 
# for example: "Simpsons S01E05" (where S is the season number in two-digit form, and E is the series number, also in two-digit format).
    def __str__(self):
        episode="S"+self.season_number+"E"+self.series_number
        return f'{self.name} {episode}'  

library=[]
#Stores movies and series in one list.
def storeInLibrary(content_type,name,graduation_year, genre, number_of_views,series_number, season_number):
    if content_type=="movie":
        movie=Movies(name, graduation_year, genre, number_of_views)
        library.append(movie)
        print(movie)
    elif content_type=="series":
        series=Series(series_number, season_number,name,graduation_year, genre, number_of_views)
        library.append(series)
        print(series)
#Write functions get_movies and get_series that will filter the list and return only movies and TV shows, respectively. Sort the received list alphabetically.
def get_Movies():
    movieList=[]
    for movie in library:
        if movie.content_type=="movie":
            movieList.append(movie)
    
    by_name = sorted(movieList, key=lambda movies:movies.name)
    return by_name

def get_Series():
    seriesList=[]
    for series in library:
        if series.content_type=="series":
            seriesList.append(series)
    
    by_name = sorted(seriesList, key=lambda item:item.name)
    return by_name

#Write a function search that will search for a movie or TV series by name.
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

#Write a function that will run generate_views 10 times
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


storeInLibrary("series","Game Of Thrones","2011","Sci-Fi",50,"01","01")
storeInLibrary("series","Game Of Thrones","2011","Sci-Fi",60,"02","01")
storeInLibrary("series","Game Of Thrones","2011","Sci-Fi",80,"03","01")

for index in range(1,2):
    for episode in range(1,5):
        episode_no=str(episode)
        season_no=str(index)
        if episode<10:episode_no="0"+episode_no
        if index<10:season_no="0"+season_no
        storeInLibrary("series","Simpsons","1994","Animation",90,episode_no,season_no)

storeInLibrary("movie","The Shawshank Redemption","1994","Drama",95,0,0) 
storeInLibrary("movie","Pulp Fiction","1994","Crime",50,0,0)
storeInLibrary("movie","The Godfather","1972","Crime,Drama",96,0,0)
storeInLibrary("movie","The Godfather 2","1982","Crime,Drama",86,0,0)
 # test play       
library[0].play()
#print(library[0].name,library[0].number_of_views)

#test run fuction
run_views()
print()
#test top_titles
print("Top Movies of the Day ")
top_titles("movie",3)
print("Top TV Shows of the Day ")
top_titles("series",3)

#test search series
search("movie","Pulp Fiction")

