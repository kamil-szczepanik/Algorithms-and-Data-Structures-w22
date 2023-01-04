def naive_search(pattern, text):
    m = len(pattern)
    n = len(text)
    matched = []
    if(n>0 and m>0 and n>=m):
      for i in range(n-m+1):
          for j in range(m):
              if text[i+j] != pattern[j]:
                  break
          if j==m-1:
            if text[i+j] == pattern[j]:
              matched.append(i)
    return matched
