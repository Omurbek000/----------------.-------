import json
import pickle

# Задание 1
# К уже реализованному классу «Автомобиль» добавьте 
# возможность упаковки и распаковки данных с использованием json и pickle.

class Auto:
    def __init__(self, brand: str, model: str, year: int,color: str):
       self.brand:str = brand
       self.model:str = model
       self.year:int = year 
       self.color:str = color
       
    def to_json(self):
     return json.dumps(self.__dict__)

@classmethod
    def from_json(cls,json_data):
     data = json.loads(json_data)
     return cls(**data)

    def to_pickle(self):
     return pickle.dumps(self)

@classmethod
    def from_pickle(cls,pickle_data):
     return pickle.loads(pickle_data)

    def __str__(self):
      return f'{self.year} {self.color} {self.brand} {self.model}'

 if __name__ == '__main__':
    my_car = Auto('Audi', 'A7',2021, 'black')
    
json_data = my_car.to_json()
print('JSON:',json_data) 
 
new_car_from_json = Auto.from_json(json_data)
print('From JSON:',new_car_from_json)

pickle_data = my_car.to_pickle()
print('Pickle data:',pickle_data)

new_car_from_pickle = Auto.from_pickle(pickle_data)
print("From Pickle:", new_car_from_pickle)


# Задание 2
# К уже реализованному классу «Книга» добавьте возможность упаковки и распаковки данных с использованием json и pickle.


    
    
class Book:
    def __init__(self, title: str, author: str, year: int, isbn: str):
        self.title:str = title
        self.author:str = author
        self.year: int = year
        self. isbn:str = isbn    
        
    def to_json(self):
     return json.dumps(self.__dict__)
 
@classmethod
    def from__json(cls,json_data):
     data = json.loads(json_data)
     return cls(**data)    

    def to_pickle(self):
     return pickle.loads(pickle_data)

    def __str__(self):
     return f'{self.title} {self.author} {self.year} {self.isbn}'

 if __name__ =='__main__':
  my_book ('название', 'автор', 'год', 'издательство')
    
json_data = my_book.to_json()
print("JSON:", json_data)

new_book_from_json = Book.from_json(json_data)
print("From JSON:", new_book_from_json)

pickle_data = my_book.to_pickle()
print("Pickle data:", pickle_data)


new_book_from_pickle = Book.from_pickle(pickle_data)
print("From Pickle:", new_book_from_pickle)    


# Задание 3
# К уже реализованному классу «Стадион» добавьте 
# возможность упаковки и распаковки данных с использованием json и pickle.


class Stadium:
    def __init__(self, name, location, capacity, built_year):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.built_year = built_year

    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_data):
        data = json.loads(json_data)
        return cls(**data)

    def to_pickle(self):
        return pickle.dumps(self)

    @classmethod
    def from_pickle(cls, pickle_data):
        return pickle.loads(pickle_data)

    def __str__(self):
        return f"{self.name} located in {self.location}, Capacity: {self.capacity}, Built in: {self.built_year}"



if __name__ == "__main__":
    stadium = Stadium("Camp Nou", "Barcelona", 99354, 1957)
    
json_data = stadium.to_json()
print("JSON:", json_data)


new_stadium_from_json = Stadium.from_json(json_data)
print("From JSON:", new_stadium_from_json)


pickle_data = stadium.to_pickle()
print("Pickle data:", pickle_data)

new_stadium_from_pickle = Stadium.from_pickle(pickle_data)
print("From Pickle:", new_stadium_from_pickle)    