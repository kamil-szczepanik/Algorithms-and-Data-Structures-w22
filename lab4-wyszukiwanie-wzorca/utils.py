def transform_polish(letter):
  letter_dict = {
    "ą": "a",
    "ć": "c",
    "ę": "e",
    "ł": "l",
    "ń": "n",
    "ó": "o",
    "ś": "s",
    "ź": "z",
    "ż": "z",
  }
  if letter in letter_dict:
      return letter_dict[letter]
  else:
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


def get_text_from_file(filename):
    text = ""
    with open(filename,'r', encoding='utf8', errors='ignore') as file:
        
        while True:
            
            # Read from file
            c = file.read(1)
            if not c:
                break
            
            if c.isalpha():
                c = transform_polish(c)
            text+=c

    return text


if __name__=="__main__":
    # print(get_text_from_file('pan-tadeusz.txt'))
    pass


