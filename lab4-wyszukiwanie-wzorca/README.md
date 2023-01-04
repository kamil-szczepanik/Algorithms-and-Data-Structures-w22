Wyszukiwanie wzorca - sprawozdanie

Podział zadań:
•Kamil Szczepanik - algorytm Naiwny i algorytm KMP
•Mateusz Roszkowski - algorytm KR


Testy poprawności implementacji:
Testy znajdują się w tests_pytests.py, w którym widać testy jednostkowe na wszystkich przypadkach brzegowych, tzn:
• pusty jeden lub oba napisy wejściowe,
• napis string równy napisowi text,
• napis string dłuższy od napisu text,
• napis string nie występuje w text.


Wyniki eksperymentów:

Algorytm KR radzi sobie najgorzej przy krótkich słowach (pierwsze słowo: "tylko"), ale jest lepszy w dłuższych słowach (drugie słowo: "podkomorzy"), więc przy zastosowaniu dłuższych zdań bądź powtarzajacych się słów, które są podobne do innych, KR wypadnie o wiele lepiej. 
Algorytm KMP radzi sobie najlepiej ze względu na pomijanie sprawdzonych już wcześniej części tekstu.
