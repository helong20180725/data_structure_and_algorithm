
def generate_subset(L):

    if len(L) == 0:
        return [[]]
    smaller = generate_subset(L[:-1])
    extra = L[-1:]
    new = []
    for small in smaller:
        new.append(small + extra)
    return smaller + new

if __name__ == "__main__":
    big = [1, 2, 3, 4, 5, 8]
    print(generate_subset(big))
    print(len(generate_subset(big)))