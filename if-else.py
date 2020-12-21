user_input=int(input("Inserisci il dividendo: "))
user_input_1=int(input("Inserisci il divisore: "))

if user_input_1==0:
    print("Operazione impossibile!")    #stampa questo messaggio se il divisore e`0
elif user_input_1>=100000:
    print("Numero troppo grande") #stampa questo messaggio se il divisore e`maggiore di 100000
else:
    print(user_input/user_input_1)  #stampa questo messaggio se nessuna delle due condizioni precedenti e` vera
