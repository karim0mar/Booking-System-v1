from Classes.ClientData import readData


def getFilmData():
    return readData("Films")


def getFilmPrice(filmName):
    for film in getFilmData()["films"]:
        if filmName == film["filmName"]:
            return film["filmPrice"]
    return 0


def getFilmDate(filmName):
    for film in getFilmData()["films"]:
        if filmName == film["filmName"]:
            return film["filmDate"]
    return 0


class FilmsControl:

    def __init__(self, _filmList):
        self.filmList = _filmList

    def printFilmsData(self):
        for film in self.filmList:
            print(f"\033[95mFilm Name : {film}")
            print(f"Film Price : {getFilmPrice(film)}$")
            print(f"Film Date : {getFilmDate(film)}")
            print('\n')
    # self.getFilmDate()

    # def getFilmDate(self):
    #   return self.filmDate
