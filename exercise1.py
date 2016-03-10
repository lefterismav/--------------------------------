import random
#kataskeuh tou pinaka
DECK=["M","N"]
for i in range(98):
		DECK.append(" ")
random.shuffle(DECK)
#thesh tou paixth kai tou thisavrou
for i in range(100):
		if DECK[i]=="M":
			x1=i/10
			y1=i%10
		if DECK[i]=="N":
			x2=i/10
			y2=i%10
print "You must find the treasure.\nHow to play:\nPress W key to go Up.\nPress A key to go Left.\nPress S key to go Down.\nPress D key to go Right.\n"
while (x1!=x2 or y1!=y2):
	#kiniseis
	move=""
	while (move!="w" and move!="W" and move!="a" and move!="A" and move!="s" and move!="S" and move!="d" and move!="D"):
		print "Please try again. Press a correct character to continue."
		move=raw_input(':')		
	if (move=="w" or move=="W"):
		if  x1!=0:
			x1=x1-1	
	if (move=="a" or move=="A"):
		if y1!=0:
			y1=y1-1
	if (move=="s" or move=="S"):
		if x1!=9:
			x1=x1+1
	if (move=="d" or move=="D"):
		if y1!=9:
			y1=y1+1
	#upoloipomenh apostash
	distance=abs(x1-x2)+abs(y1-y2)
	if distance!=0:
		print "Keep trying almost done. There are ",distance," moves left to make.\n"
print "You did it! BRAVO!!!"
