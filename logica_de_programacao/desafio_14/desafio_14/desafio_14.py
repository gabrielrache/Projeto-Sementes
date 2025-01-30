"""Remove duplicidades de um vetor de nomes"""

singer = ["Dave Mustaine", "Alice Cooper", "Corey Taylor", "Dave Mustaine",
          "Marko Hietala", "Ozzy Osbourne", "Bruce Dickinson", "James Hetfield", 
          "Ozzy Osbourne", "James Hetfield", "Corey Taylor", "Tarja Turunen",
          "Amy Lee", "Bruce Dickinson", "Andre Matos","Simone Simons", 
          "Serj Tankian", "Chester Bennington", "Bruce Dickinson", "Amy Lee"]

for name in singer:

    quantity = singer.count(name)

    if quantity > 1:
        singer.pop(singer.index(name))

print (singer)
