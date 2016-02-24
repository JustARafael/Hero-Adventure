# RAFAEL LI CHEN
import os
import time
import sys
import os.path
# requirement 1: a class for the player
# holding information for damage and health
class player:
	def __init__(self):
		self.health=8
		self.damage=2
		self.key=0
# requirement 1: a class for an enemy
# holding information for damage and health
class enemy:
	def __init__(self):
		self.health=4
		self.damage=2
class boss:
	def __init__(self):
		self.health=50
		self.damage=10
def end():
	os.system("clear")
	print("you have defeated the boss")
	print("game ended")
	sys.exit(0)
def game():
	os.system("clear")
	print("<b> battle")
	print("<i> info")
	print("<s> save")
	print("<m> menu")
	p_input=input("what to do?").lower()
	if p_input=="b" or p_input=="battle":
		battle()
	elif p_input=="i" or p_input=="info":
		info()
	elif p_input=="s" or p_input=="save":
		save()
	elif p_input=="m" or p_input=="menu":
		menu()
	else:
		game()
# requirement 2: included at least 2 save points
# player can save game at anytime except during battle
def save():
	data=open("stat.txt","w")
	data.write(str(p.health))
	data.write(".")
	data.write(str(p.damage))
	data.write(".")
	data.write(str(p.key))
	data.write(".")
	data.close()
	os.system("clear")
	print("game saved")
	time.sleep(1)
	data.close()
	menu()
def menu():
	os.system("clear")
	print("<n> new")
	print("<l> load")
	print("<q> quit")
	p_input=input("what to do?").lower()
	if p_input=="n" or p_input=="new":
		p.health=8
		p.damage=2
		p.key=0
		game()
	elif p_input=="l" or p_input=="load":
		if os.path.isfile("stat.txt"):
			load()
		else:
			os.system("clear")
			print("no saved game found")
			time.sleep(1)
			menu()
	elif p_input=="q" or p_input=="quit":
		os.system("clear")
		print("terminating game...")
		time.sleep(0.5)
		sys.exit(0)
	else:
		menu()
# requirement 2: saved game will be loaded
# player can load saved game to continue playing		
def load():
	data=open("stat.txt","r")
	code=""
	code_list=[]
	while True:
		character=data.read(1)
		if not character.isnumeric():
			code_list.append(code)
			code=""
		if character.isnumeric():
			code+=character
		if not character:
			break
	p.health=int(code_list[0])
	p.damage=int(code_list[1])
	p.key=int(code_list[2])
	os.system("clear")
	print("information has been loaded")
	time.sleep(1)
	data.close()
	game()
def info():
	os.system("clear")
	print("health:",p.health)
	print("damage:",p.damage)
	if p.key==1:
		print("inventory: key")
	p_input=input("go back? yes?").lower()
	if p_input=="y" or p_input=="yes":
		game()
	else:
		info()
def battle():
	os.system("clear")
	print("room 1")
	print("room 2")
	print("room 3")
	p_input=input("which room?")
	if p_input=="1":
		room_1()
	elif p_input=="2":
		room_2()
	elif p_input=="3":
		room_3()
	else:
		battle()
# requirement 3: multiple turn-based battle sequences included (while true loop)
# player can choose between attack and run during their turn in the battle
# same for all 3 rooms
def room_1():
	os.system("clear")
	enemy1=enemy()
	hp=p.health
	print("enemy encountered")
	print("enemy damage:",enemy1.damage)
	print("enemy health:",enemy1.health)
	while True:
		if enemy1.health<=0:
			time.sleep(1)
			os.system("clear")
			print("victory")
			print("damage +1")
			print("health +2")
			p.damage+=1
			p.health=hp+2
			time.sleep(1)
			break
		elif p.health<=0:
			time.sleep(1)
			os.system("clear")
			print("defeat")
			p.health=hp
			time.sleep(1)
			break
		print("<a> attack")
		print("<r> run")
		p_input=input("what to do?").lower()
		if p_input=="a" or p_input=="attack":
			enemy1.health=enemy1.health-p.damage
			print("enemy health:",enemy1.health)
			p.health=p.health-enemy1.damage
			print("your health:",p.health)
		elif p_input=="r" or p_input=="run":
			os.system("clear")
			print("escaping...")
			time.sleep(1)
			p.health=hp
			break
	game()
# requirement 4: player can choose from at least two different paths
# in room 2: door 1 has the key and door 2 has an enemy
# player can't finish the game without the key
def room_2():
	os.system("clear")
	enemy2=enemy()
	enemy2.health+=10
	enemy2.damage+=2
	print("there are 2 doors")
	print("door 1: nothing special, but looks dangerous")
	print("door 2: has a stick figure on it")
	p_input=input("which door?")
	if p_input=="1":
		if p.key==0:
			p.key=1
			os.system("clear")
			print("you found a key")
			print("going back...")
			time.sleep(2)
			game()
		else:
			os.system("clear")
			print("nothing in this room")
			print("going back...")
			time.sleep(2)
			game()
	elif p_input=="2":
		hp=p.health
		os.system("clear")
		print("enemy encountered")
		print("enemy damage:",enemy2.damage)
		print("enemy health:",enemy2.health)
		while True:
			if enemy2.health<=0:
				time.sleep(1)
				os.system("clear")
				print("victory")
				print("damage +2")
				print("health +3")
				p.damage+=2
				p.health=hp+3
				time.sleep(1)
				break
			elif p.health<=0:
				time.sleep(1)
				os.system("clear")
				print("defeat")
				p.health=hp
				time.sleep(1)
				break
			print("<a> attack")
			print("<r> run")
			p_input=input("what to do?").lower()
			if p_input=="a" or p_input=="attack":
				enemy2.health=enemy2.health-p.damage
				print("enemy health:",enemy2.health)
				p.health=p.health-enemy2.damage
				print("your health:",p.health)
			elif p_input=="r" or p_input=="run":
				os.system("clear")
				print("escaping...")
				time.sleep(1)
				p.health=hp
				break
	else:
		room_2()		
	game()
# requirement 5: player's inventory: key will be checked after defeating the boss
# the inventory: key is part of the player class (self.key=0 / self.key=1)
# player can't finish the game without the key
def room_3():
	os.system("clear")
	boss1=boss()
	hp=p.health
	print("final boss has appeared!")
	print("enemy damage:",boss1.damage)
	print("enemy health:",boss1.health)
	while True:
			if boss1.health<=0:
				time.sleep(1)
				os.system("clear")
				print("victory")
				p.health=hp
				time.sleep(1)
				if p.key==1:
					os.system("clear")
					print("using key to open the exit door...")
					time.sleep(2)
					end()
				else:
					os.system("clear")
					print("there is a exit door")
					print("but you don't have a key to open it")
					time.sleep(2)
					break
			elif p.health<=0:
				time.sleep(1)
				os.system("clear")
				print("defeat")
				p.health=hp
				time.sleep(1)
				break
			print("<a> attack")
			print("<r> run")
			p_input=input("what to do?").lower()
			if p_input=="a" or p_input=="attack":
				boss1.health=boss1.health-p.damage
				print("enemy health:",boss1.health)
				p.health=p.health-boss1.damage
				print("your health:",p.health)
			elif p_input=="r" or p_input=="run":
				os.system("clear")
				print("escaping...")
				time.sleep(1)
				p.health=hp
				break
	game()
p=player()
menu()