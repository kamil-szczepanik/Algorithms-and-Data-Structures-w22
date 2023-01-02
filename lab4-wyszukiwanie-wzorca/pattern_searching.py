

def naive_search(pat, txt):
    m = len(pat)
    n = len(txt)

    for i in range(n-m):
        for j in range(m):
            if txt[i+j] != pat[j]:
                break
        if j==m-1:
            return i
    return -1



if __name__=="__main__":

    pat = "igla"
    txt = "gdziejestiglawstogusiana"

    
    print(naive_search(pat, txt))