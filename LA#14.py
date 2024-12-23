class Spiderman:
    def __init__(self, name, age):
        self.name = name.lower()
        self.age = age
    def describe_spiderman(self):
        print(f"Name: {self.name.upper()}, Age: {self.age},")

class Tobey(Spiderman):
    def __init__(self, name, age, movie_title):
        super().__init__(name, age)
        self.movie_title = movie_title

class Andrew(Spiderman):
    def __init__(self, name, age, movie_title):
        super().__init__(name, age)
        self.movie_title = movie_title
       
class Tom(Spiderman):
    def __init__(self, name, age, movie_title):
        super().__init__(name, age)
        self.movie_title = movie_title
       
tobey = Tobey("Tobey Maguire", 46, "Spiderman (2002)")
andrew = Andrew("Andrew Garfield", 40, "The Amazing Spiderman (2012)")
tom = Tom("Tom Holland", 27, "Spiderman: Homecoming (2017)")

print(f"Name: {tobey.name.upper()}, Movie: {tobey.movie_title}")
print(f"Name: {andrew.name.upper()}, Movie: {andrew.movie_title}")
print(f"Name: {tom.name.upper()}, Movie: {tom.movie_title}")