from lista import data
import random

print("Benvenuto in higer or lower")
contatore=0
personaggi={}
followers=[]
followers1=0
followers2=0
g=True
cont_vittorie=0
vinto=False
scelta=""
while g==True:
    n=random.sample(range(0,len(data)),2)
    vs=0
    
    for idx in n:
        if vs==0:
            print("Inizio Confronto")
            print("""
     __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/        
                    """)
            print(f"Indovinati {cont_vittorie}")
        elif vs>1:
            print("""
                     _    __    
                    | |  / /____
                    | | / / ___/
                    | |/ (__  ) 
                    |___/____(_)
                    """)
        print("\n-------------------------------------------------\n")
        cont=0
        for chiave,valore in data[idx].items():
            vs+=1
            if chiave=="follower_count" :
                followers.append(valore)
            else:
                print(f"{chiave}:{valore}")
                personaggi.update({chiave:valore})#vado a creare il dizionario personaggi in modo tale che abbia i 2 personaggi scelti
            
                #cont+=1
            #elif chiave=="follower_count" and cont==1:
                #followers2=valore
    scelta=int(input("Chi ha più followers il numero 1 o il numero 2?"))
    if(scelta==1 and followers[0]>followers[1])or (scelta==2 and followers[1]>followers[0]):
        cont_vittorie+=1
        print("\n"*100)
    else:
        g=False
        print("\n"*100)
        print(f"Hai perso sei riuscito a indovinare :{cont_vittorie}")
        cont_vittorie=0
        continuare=input("Vuoi rigiocare ? y o n").lower()
        if(continuare=="y"):
            g=True
            print("\n"*100)
        else:
            g=False
    followers.clear()
        
                
    #print(personaggi)    



    
        #print(r)
    '''for i in range(len(data)):
        personaggio1=data[i]

    for i in range(2):  # i è l'indice
        personaggio = data[i]  # Otteniamo il dizionario corrispondente
        
        #print(f"Personaggio {i}:")
        
        for chiave, valore in personaggio.items():
            print(f"{chiave}: {valore}")
        
        print()  # Riga vuota per separare i personaggi'''
