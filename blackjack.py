import random
def somma(a,b):
    return a+b

def check_Banco(carta1,carta2):
	"""Chiama fino a somma>=15, e gestisce l'asso"""
	s=somma(carta1,carta2)
	if(s>=15):
		return s
	else:
		while s<15:
			Banco_carte.append(random.choice(cards))
			s+=Banco_carte[-1]
			if(carta1 or carta2 or Banco_carte[-1])==11 and s>21:
				s-=10
				a=Banco_carte.index(11)
				Banco_carte[a]=1
                
	return s

def check_Player(carta1,carta2):
	"""Fa la somma delle carte e gestisce l'eventualità di un asso"""
	s=somma(carta1,carta2)
	if(carta1 or carta2)==11 and s>21:
		s-=10
		a=Player_carte.index(11)
		Player_carte[a]=1
		
	return s

def sballato_ceck(s):
	if(s>21):
		return True
	else:
		return False


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

print("--------------------------BLACK JACK--------------------------")
logo ="""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)


carte_Banco=random.sample(cards,2)
Banco_carta1=carte_Banco[0]
Banco_carta2=carte_Banco[1]
Banco_carte=[Banco_carta1,Banco_carta2]
somma_Banco=somma(Banco_carta1,Banco_carta2)
print(f"Il banco ha {Banco_carta1}")
carte_Player=random.sample(cards,2)
Player_carta1=carte_Player[0]
Player_carta2=carte_Player[1]
Player_carte=[Player_carta1,Player_carta2]
somma_Player=somma(Player_carta1,Player_carta2)
print(f"Tu hai {carte_Player} la somma è {somma_Player}")

scelta=True
sballato=False
if somma_Player==21:
	scelta=False
chiamata=""

while scelta==True:
	chiamata=input("Se vuoi chiamare carta digita y altrimenti n")
	if(chiamata=="y"):
		Player_carte.append(random.choice(cards))
		print(f"QUESTE SONO LE CARTE CHE HAI ADESSO {Player_carte}")
		somma_Player=check_Player(somma_Player,Player_carte[-1])
		sballato=sballato_ceck(somma_Player)
	else:
		scelta=False

	if(sballato==True):
		scelta=False

if somma_Player<=21:
	somma_Banco=check_Banco(Banco_carta1,Banco_carta2)
	if(somma_Banco>21):
		print(f"Il banco ha {Banco_carte}")
		print("Hai vinto complimenti")
	elif(somma_Banco>=somma_Player):
		print(f"Mi dispiace hai perso con {Player_carte}")
		print(f"Il banco ha {Banco_carte}")
	else:
		print(f"Hai vinto con {Player_carte}")
		print(f"Il banco ha {Banco_carte}")

else:
	print(f"Hai sballato il banco ha vinto con{Banco_carte}")	
