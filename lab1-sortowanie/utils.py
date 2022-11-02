def transform_polish(letter):
  match letter:
    case "ą":
      return "a"
    case "ę":
      return "e"
    case "ó":
      return "o"
    case "ć":
      return "c"
    case "ł":
      return "l"
    case "ś":
      return "s"
    case "ź":
      return "z"
    case "ż":
      return "z"
    case _:
      return letter

def get_N_words_from_file(filename, N):

    with open(filename,'r', encoding='utf8', errors='ignore') as file:
        
        array = [None] * N

        index = 0
        for line in file:
            for word in line.split():
                array[index] = ''.join([transform_polish(i) for i in word.lower() if i.isalpha()])
                if array[index] != '':
                    index += 1
                if index == N:
                    return array

