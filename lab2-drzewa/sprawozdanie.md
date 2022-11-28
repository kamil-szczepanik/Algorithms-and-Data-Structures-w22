# Drzewa - sprawozdanie

Podział zadań:
- Mateusz Roszkowski - BST
- Kamil Szczepanik - AVL

## Wyniki eksperymentów

### Tworzenie drzew
![plot](wykresy/tworzenie.png "Tworzenie drzew")

### Szuaknie w drzewie
![plot](wykresy/szukanie.png "Szuaknie w drzewie")

### Usuwanie elementów w drzewie
![plot](wykresy/usuwanie.png "Usuwanie elementów w drzewie")


### Wnioski:
- Tworzenie drzew jest szybsze dla BST, ponieważ nie wykonywane są żadne rotacje. 
- Wyszukiwanie w drzewie jest szybsze w AVL, ponieważ te drzewa nie są aż tak wysokie jak BST.
-  Usuwanie jest szybsze dla BST. Wydawałoby się, że tutaj również AVL ma szanse być szybszym algorytmem, ponieważ w usuwaniu wykonywana jest operacja szukania. Widocznie częste rotacje są powodem do wolniejszego działania.