peso = int(input("Inserisci peso: "))  # l`utente inserisce il peso del frutto


def e_pari(num):  # verifica se il numero e` pari
    if num % 2 == 0:
        return 1
    else:
        return 0


def Solve():  # Verifichiamo se la suddivisione secondo i criteri indicati e` possibile
    for x in range(1, 101):
        if x <= (peso / 2):
            if e_pari(x):
                if e_pari(peso):
                    return 1
        else:
            return 0


if peso < 1 or peso > 100:  # verifica se il numero inserito e` valido
    print("Numero non valido, riprova")
    exit()
elif Solve():  # se la funzione restituisce 1 (True) stampa "YES"
    print("YES")
else:  # se la funzione restituisce 0 (False) stampa "NO"
    print("NO")
