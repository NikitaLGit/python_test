a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 4]

def lens(chis):
    i = 0
    for N in a:
        if N<chis:
            print(N)
            i +=1
        else:
            continue

c = int(input("Vvedite chislo: "))
lens(c)