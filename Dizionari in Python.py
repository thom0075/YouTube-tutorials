user_input_1=input("Inserisci il nome dell`azienda >  ")
user_input_2=input("Inserisci il nome della seconda azienda > ")

#si riceve l`input dall`utente

user_input_3=int(input("Inserisci numero di dipendenti della prima azienda (solo int)> "))
user_input_4=int(input("Inserisci numero di dipendenti della seconda azienda (solo int) > "))

d={user_input_1:user_input_3, user_input_2:user_input_4}

#tutto quello inserito dall`utente viene aggiunto al dizionario

user_input_5=input("Inserisci nome azienda > ")

#chiediamo all`utente di inserire un nome per avere delle informazioni che verranno prese dal dizionario

if user_input_5==user_input_1:  #se il nome inserito corrisponde al primo nome, si stampano le info riguardanti la prima azienda
    print("Numero di dipendenti dell`azienda selezionata: ",d[user_input_1])
if user_input_5==user_input_2:  #se il nome inserito corrisponde al secondo nome, si stampano le info riguardanti la seconda azienda
    print("Numero di dipendenti dell`azienda selezionata: ",d[user_input_2])
if user_input_5!=user_input_1 and user_input_5!=user_input_2:
    print("Errore")
#se il nome inserito non corrisponde ne` al primo nome ne`al secondo, si stampa un messaggio di errore
