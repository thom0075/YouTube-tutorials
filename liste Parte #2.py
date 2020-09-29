#By thom0075
#YouTube channel link: https://www.youtube.com/channel/UCDSmCUDI_hx09nOqKcakmKQ
import time

l=[]

user_input_1=input("Inserisci il tuo nome: ")   #
l.append(user_input_1)
print(l[0])

#-------------------------------

user_input_2=input("Inserisci il tuo cognome: ")
l.append(user_input_2)
print(l[1])

#-------------------------------

del(user_input_1)
print("Var 1 cancellata...")
time.sleep(1)
del(user_input_2)
print("Var 2 cancellata...")
time.sleep(1)

