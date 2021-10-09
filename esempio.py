try:
    a = int(input("Inserisci un numero: "))
    b = int(input("Inserisci un numero: "))
    c = int(input("Inserisci un numero: "))
    
except ValueError:
    print("[ERRORE] input non valido")
    if (type(a) and type(b) and type(c)) == str:
        print(a+b+c)
    #exit()
    
if a < 0 or b < 0 or c < 0:
    print("[ERRORE] numeri non validi, prova a riavviare il programma")
elif a > 100 or b > 100 or c > 100:
    print("[ERRORE] Valori troppo grandi, riprova")
else:
    print("La somma dei numeri e`: %i" % (a+b+c))
    
