'''afiseaza primele n numere prime '''
cateNumere=6
def primele_zece_prime(cateNumere):
    numere_prime = []
    numar = 2
    while len(numere_prime) < cateNumere:
        if este_prim(numar):
            numere_prime.append(numar)
        numar += 1
    print(numere_prime)
    return numere_prime

def este_prim(numar):
    if numar < 2:
        return False
    for i in range(2, int(numar**0.5) + 1):
        if numar % i == 0:
            return False
    return True