def kr_search(pat, txt, q):
  M = len(pat)
  N = len(txt)
  p = 0    # hash of pat
  t = 0    # hash of txt
  h = 1
  d = 256
  matched = []
  if(N>0 and M>0 and N>=M):
    #"pow(d, M-1)% q"
    for i in range(M-1):
        h = (h * d)% q

    for i in range(M):
        p = (d * p + ord(pat[i]))% q
        t = (d * t + ord(txt[i]))% q

    for i in range(N-M + 1):
      #checking hash
      if p == t:
        # checking pattern in text
        for j in range(M):
            if txt[i + j] != pat[j]:
                break

        j+= 1
        if j == M:
          matched.append(i)
      # new hash
      if i < N-M:
        t = (d*(t-ord(txt[i])*h) + ord(txt[i + M]))% q

        if t < 0:
          t = t + q
  return matched