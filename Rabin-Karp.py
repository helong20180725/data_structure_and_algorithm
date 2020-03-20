# Rabin-Karp Algorithm for pattern searching
# pattern  : ABAB
# text     : AABAABCCDEAA
# Return all the indices whose pattern are same as the given pattern in the given text.
# hash( txt[s+1 .. s+m] ) = ( d ( hash( txt[s .. s+m-1]) – txt[s]*h ) + txt[s + m] ) mod q
# hash( txt[s .. s+m-1] ) : Hash value at shift s.
# hash( txt[s+1 .. s+m] ) : Hash value at next shift (or shift s+1)
# d: Number of characters in the alphabet
# q: A prime number
# h: d^(m-1)


def search(txt, pattern, prime, digit):
    # d : the number of charactors in the ascii table.
    d = digit
    q = prime
    h = 1
    m = len(pattern)
    n = len(txt)
    indices = []
    # ( ( (1*256)%101 )*256 )%101 = ( 1*256*256 )%101
    for i in range(m-1):
        h = ( h * d ) % q 
    
    # p : the hash value of pattern
    # t : the hash value of substring in txt
    p = 0
    t = 0
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q 
        t = (d * t + ord(txt[i])) % q 
    
    for i in range(n - m + 1):
        if p == t: 
            # If the hash values are equal, compare the charactors one by one
            for j in range(m):
                if txt[i+j] != pattern[j]:
                    break 
            j += 1 
            if j == m :
                
                indices.append(i)
        # Calculate the new value of next t
        if i < n - m:
            t = (d * (t - (ord(txt[i]) * h) ) + ord(txt[i+m])) % q
            print(t)

            if t < 0:
                print(i)
                t = t + q 
    return indices

if __name__ == "__main__":
    txt = "666666666666"
    pattern = "234"
    print(search(txt, pattern, 53, 10))









    


    

