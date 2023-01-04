def find_lps(pattern):
    # lps - longest proper prefix that is suffix

    # lista lps ma dlugość taką samą co pattern
    lps = [0]*len(pattern)

    prefix_idx = 0
    for i in range(1, len(pattern)):

        # zmniejszanie prefixa jesli znaki rozne
        while prefix_idx and pattern[i] != pattern[prefix_idx]:
            prefix_idx = lps[prefix_idx - 1]
        
        # zwiekszanie prefixa jesli znaki te same
        if pattern[prefix_idx] == pattern[i]:
            prefix_idx += 1
            lps[i] = prefix_idx

    return lps

def kmp_search(pattern, text):
    matched = []
    if(len(pattern)>0 and len(text)>0 and len(text)>=len(pattern)):
      lps = find_lps(pattern)

      pattern_idx = 0
      for i in range(len(text)):
          
          # jesli jest niezgodność znaków to korzystamy z lps zeby zaktualizowac pattern_idx
          while pattern_idx and pattern[pattern_idx] != text[i]:
              pattern_idx = lps[pattern_idx - 1]

          # zgodność
          if pattern[pattern_idx] == text[i]:
              # koniec wzorca = dopasowanie, zapis i aktualizacja pattern_idx używając lps
              if pattern_idx == len(pattern) - 1:
                  matched.append(i - pattern_idx)
                  pattern_idx = lps[pattern_idx]
              
              else:
                  # zgodność ale jeszcze nie koniec wzorca
                  pattern_idx += 1
    return matched
