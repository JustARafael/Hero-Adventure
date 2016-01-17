from tkinter import *
from os import system
import time
import threading
import queue
import sys
from tkinter import ttk
import os.path
import tkinter.messagebox
from random import randint

container = Tk()
container.title("Hero Adventure")
container.resizable(width=False, height=False)

low_bar=ttk.Progressbar(container,orient="horizontal",maximum=5,mode="determinate")
high_bar=ttk.Progressbar(container,orient="horizontal",maximu=10,mode="determinate")
low_bar_display=queue.Queue()
def low_bar_add():
    i=1
    while i<6:
        low_bar_display.put(i)
        i+=1
    low_bar_display.put(0)
def low_bar_display_thread():
    while True:
        time.sleep(1)
        low_bar["value"]=low_bar_display.get()
        if low_bar["value"]==5:
            p.low_potion+=1
low_bar_thread=threading.Thread(target=low_bar_display_thread)
low_bar_thread.daemon=True
low_bar_thread.start()

high_bar_display=queue.Queue()
def high_bar_add():
    i=1
    while i<11:
        high_bar_display.put(i)
        i+=1
    high_bar_display.put(0)
def high_bar_display_thread():
    while True:
        time.sleep(1)
        high_bar["value"]=high_bar_display.get()
        if high_bar["value"]==10:
            p.high_potion+=1
high_bar_thread=threading.Thread(target=high_bar_display_thread)
high_bar_thread.daemon=True
high_bar_thread.start()

class player:
    def __init__(self):
       self.health=8
       self.damage=2
       self.key=0
       self.apple=0
       self.egg=0
       self.ham=0
       self.fish=0
       self.gold=100
       self.bottle=0
       self.low_potion=0
       self.high_potion=0
class enemy:
    def __init__(self):
       self.health=6
       self.damage=2
class boss:
    def __init__(self):
       self.health=100
       self.damage=40
       
global p
p=player()

label_by=Label(container, text="""BY:
RAFAEL LI CHEN
BO HAN CHEN
JIN HUI CHEN""")
photo = PhotoImage(file="MAIN-HERO.gif")
label = Label(image=photo)
photo1 = PhotoImage(file="BONE.gif")
label1 = Label(image=photo1)
photo2 = PhotoImage(file="ORC.gif")
label2 = Label(image=photo2)
photo3 = PhotoImage(file="DRAGON.gif")
label3 = Label(image=photo3)
photo4 = PhotoImage(file="2-3.gif")
label4 = Label(image=photo4)
photo5 = PhotoImage(file="2-5.gif")
label5 = Label(image=photo5)
photo6 = PhotoImage(file="5-6.gif")
label6 = Label(image=photo6)
photo7 = PhotoImage(file="white.gif")
label7 = Label(image=photo7)
photo8 = PhotoImage(file="5-3.gif")
label8 = Label(image=photo8)
photo9 = PhotoImage(file="11.gif")
label9 = Label(image=photo9)
photo10 = PhotoImage(file="1-8.gif")
label10 = Label(image=photo10)
photo11 = PhotoImage(file="3-2.gif")
label11 = Label(image=photo11)
photo12 = PhotoImage(file="2-7.gif")
label12 = Label(image=photo12)
photo13 = PhotoImage(file="3-3.gif")
label13 = Label(image=photo13)
photo14 = PhotoImage(file="3-8.gif")
label14 = Label(image=photo14)
photo15 = PhotoImage(file="3-1.gif")
label15 = Label(image=photo15)
photo16 = PhotoImage(file="3-4.gif")
label16 = Label(image=photo16)
photo17 = PhotoImage(file="3-6.gif")
label17 = Label(image=photo17)

label_new=Label(container, text="New")
label_load=Label(container, text="Load")
label_quit=Label(container, text="Quit")
label_battle=Label(container, text="Battle")
label_info=Label(container, text="Info")
label_store=Label(container, text="Store")
label_save=Label(container, text="Save")
label_menu=Label(container, text="Menu")
damage_text="Damage: "+str(p.damage)
label_damage=Label(container, text=damage_text)
health_text="Health: "+str(p.health)
label_health=Label(container, text=health_text)
label_1=Label(container, text="1")
label_go_back=Label(container, text="Go back")
label_room1=Label(container, text="Room 1")
label_room2=Label(container, text="Room 2")
label_room3=Label(container, text="Room 3")
label_attack=Label(container, text="Attack")
label_run=Label(container, text="Run")
label_door1=Label(container, text="Door 1")
label_door2=Label(container, text="Door 2")
label_box_text=Label(container, text="There is a treasure box!")
label_nothing=Label(container, text="There is nothing here. Just a rock!")
label_gem=Label(container, text="Looks like a key to open something.")
label_damage_text=Label(container, text="Damage")
label_health_text=Label(container, text="Health")
label_player_health=Label(container, text="")
label_player_damage=Label(container, text="")
label_enemy_health=Label(container, text="")
label_enemy_damage=Label(container, text="")
label_choose=Label(container, text="""There are 2 doors,
Choose one to enter.
""")
label_weapon_44=Label(container, text="damage:+1  $200")
label_weapon_46=Label(container, text="damage:+2  $300")
label_weapon_14=Label(container, text="damage:+3  $400")
label_armor_24=Label(container, text="health:+2  $200")
label_armor_28=Label(container, text="health:+4  $350")
label_armor_22=Label(container, text="health:+6  $500")
label_armor_26=Label(container, text="health:+10  $800")
label_emp_bottle=Label(container, text="")
label_gold=Label(container, text="")
label_synthesis=Label(container, text="Synthesis")
label_low_potion=Label(container, text="Low Potion\nRecover 20 HP")
label_low_potion_number=Label(container, text="")
label_low_potion1=Label(container, text="""1 Bottle 
+ 
1 Apple 
+ 
1 Egg :""")
label_high_potion=Label(container, text="High Potion\nRecover 50 HP")
label_high_potion_number=Label(container, text="High Potion (%s)"%p.high_potion)
label_high_potion1=Label(container, text="""1 Bottle
+
1 Ham 
+ 
1 Fish :""")
label_material=Label(container, text="")
label_apple=Label(container, text="")
label_egg=Label(container, text="")
label_ham=Label(container, text="")
label_fish=Label(container, text="")
label_bottle=Label(container, text="")
label_bottle1=Label(container, text="$100 for 1 Bottle")
label_bottle2=Label(container, text="$350 for 5 Bottles")
label_onwer=Label(container, text="Store Owner")

def remove():
    low_bar.grid_remove()
    high_bar.grid_remove()
    label_enemy_damage.grid_remove()
    label_enemy_health.grid_remove()
    label_player_damage.grid_remove()
    label_player_health.grid_remove()
    button_battle.grid_remove()
    button_info.grid_remove()
    button_store.grid_remove()
    button_save.grid_remove()
    button_menu.grid_remove()
    label_battle.grid_remove()
    label_info.grid_remove()
    label_store.grid_remove()
    label_save.grid_remove()
    label_menu.grid_remove()
    label.grid_remove()
    label1.grid_remove()
    label2.grid_remove()
    label3.grid_remove()
    label4.grid_remove()
    label5.grid_remove()
    label6.grid_remove()
    label7.grid_remove()
    label_1.grid_remove()
    label_health.grid_remove()
    label_damage.grid_remove()
    button_new.grid_remove()
    button_load.grid_remove()
    button_quit.grid_remove()
    label_new.grid_remove()
    label_load.grid_remove()
    label_quit.grid_remove()
    label_by.grid_remove()
    button_info_new.grid_remove()
    label_go_back.grid_remove()
    label_room1.grid_remove()
    label_room2.grid_remove()
    label_room3.grid_remove()
    button_room1.grid_remove()
    button_room2.grid_remove()
    button_room3.grid_remove()
    button_run.grid_remove()
    button_attack.grid_remove()
    label_attack.grid_remove()
    label_run.grid_remove()
    button_room2_monster.grid_remove()
    button_room2_key.grid_remove()
    label_door2.grid_remove()
    label_door1.grid_remove()
    label_choose.grid_remove()
    button_room2_key_box.grid_remove()
    label_box_text.grid_remove()
    label_gem.grid_remove()
    label_nothing.grid_remove()
    label8.grid_remove()
    label_damage_text.grid_remove()
    label_health_text.grid_remove()
    button_weapon_14.grid_remove()
    button_weapon_44.grid_remove()
    button_weapon_46.grid_remove()
    label_weapon_14.grid_remove()
    label_weapon_44.grid_remove()
    label_weapon_46.grid_remove()
    button_armor_22.grid_remove()
    button_armor_24.grid_remove()
    button_armor_26.grid_remove()
    button_armor_28.grid_remove()
    label_armor_24.grid_remove()
    label_armor_28.grid_remove()
    label_armor_22.grid_remove()
    label_armor_26.grid_remove()
    label10.grid_remove()
    button_emp_bottle.grid_remove()
    label_emp_bottle.grid_remove()
    button_store_new.grid_remove()
    label9.grid_remove()
    label_gold.grid_remove()
    label_synthesis.grid_remove()
    button_synthesis.grid_remove()
    label_low_potion.grid_remove()
    label_low_potion1.grid_remove()
    label_high_potion.grid_remove()
    label_high_potion1.grid_remove()
    button_low_potion.grid_remove()
    button_high_potion.grid_remove()
    button_low_potion_use.grid_remove()
    button_high_potion_use.grid_remove()
    label_apple.grid_remove()
    label_egg.grid_remove()
    label_ham.grid_remove()
    label_fish.grid_remove()
    label13.grid_remove()
    label14.grid_remove()
    label15.grid_remove()
    label16.grid_remove()
    label17.grid_remove()
    label_bottle.grid_remove()
    label_bottle1.grid_remove()
    label_bottle2.grid_remove()
    label_onwer.grid_remove()
    label_material.grid_remove()
    button_emp_bottle1.grid_remove()
    label_low_potion_number.grid_remove()
    label_high_potion_number.grid_remove()
    
def update():
    global hp
    hp=p.health
    if which_room==1:
       label_player_damage.configure(text=p.damage)
       label_player_health.configure(text=p.health)
       label_enemy_damage.configure(text=enemy1.damage)
       label_enemy_health.configure(text=enemy1.health)
    elif which_room==2:
       label_player_damage.configure(text=p.damage)
       label_player_health.configure(text=p.health)
       label_enemy_damage.configure(text=enemy2.damage)
       label_enemy_health.configure(text=enemy2.health)
    elif which_room==3:
       label_player_damage.configure(text=p.damage)
       label_player_health.configure(text=p.health)
       label_enemy_damage.configure(text=boss1.damage)
       label_enemy_health.configure(text=boss1.health)
    label_player_damage.grid(row=1,column=0)
    label_player_health.grid(row=2,column=0)
    label_enemy_damage.grid(row=1,column=2)
    label_enemy_health.grid(row=2,column=2)

def battle():
    remove()
    button_room1.grid(row=0,column=0)
    button_room2.grid(row=0,column=1)
    button_room3.grid(row=0,column=2)
    label_room1.grid(row=1,column=0)
    label_room2.grid(row=1,column=1)
    label_room3.grid(row=1,column=2)
    container.update()
    window_center()
battle_b_image=PhotoImage(file="1-3.gif")
button_battle=Button(image=battle_b_image, command=battle)

def attack():
    global result
    if which_room==1:
       enemy1.health=enemy1.health-p.damage
       p.health=p.health-enemy1.damage
       label_player_health.configure(text=p.health)
       label_enemy_health.configure(text=enemy1.health)
       container.update()
       window_center()
       if enemy1.health<=0:
         result=tkinter.messagebox.showinfo("","Victory, Damage +1, Health +2, Gold +100.")
         p.damage+=1
         p.health=hp+2
         p.gold+=100
         r=randint(0,3)
         if r==0:
          result=tkinter.messagebox.showinfo("","You got a Apple!")
          p.apple=p.apple+1
         elif r==1:
          result=tkinter.messagebox.showinfo("","You got an Egg!")
          p.egg=p.egg+1
         if result:
          game()
       elif p.health<=0:
         result=tkinter.messagebox.showinfo("","Defeat...")
         run()
    elif which_room==2:
       enemy2.health=enemy2.health-p.damage
       p.health=p.health-enemy2.damage
       label_player_health.configure(text=p.health)
       label_enemy_health.configure(text=enemy2.health)
       container.update()
       window_center()
       if enemy2.health<=0:
         result=tkinter.messagebox.showinfo("","Victory, Damage +2, Health +3, Gold +200.")
         p.damage+=2
         p.health=hp+3
         p.gold+=200
         r=randint(0,3)
         if r==0:
          result=tkinter.messagebox.showinfo("","You got a Ham!")
          p.ham=p.ham+1
         elif r==1:
          result=tkinter.messagebox.showinfo("","You got a Fish!")
          p.fish=p.fish+1
         if result:
          game()
       elif p.health<=0:
         result=tkinter.messagebox.showinfo("","Defeat...")
         run()
    elif which_room==3:
       boss1.health=boss1.health-p.damage
       p.health=p.health-boss1.damage
       label_player_health.configure(text=p.health)
       label_enemy_health.configure(text=boss1.health)
       container.update()
       window_center()
       if boss1.health<=0:
         if p.key==1:
          result=tkinter.messagebox.showinfo("","Victory! You used the gem to activate the mechanism of exit door")
         else:
          tkinter.messagebox.showinfo("","There is an exit door, but you don't have a key to open it")
          result=False
          run()
         if result:
          remove()
          if os.path.isfile("stat.txt"):
              os.remove("stat.txt")
          menu()
       elif p.health<=0:
         result=tkinter.messagebox.showinfo("","Defeat...")
         run()
attack_b_image=PhotoImage(file="1-6.gif")
button_attack=Button(image=attack_b_image, command=attack)

def run():
    p.health=hp
    game()
run_b_image=PhotoImage(file="5-9.gif")
button_run=Button(image=run_b_image, command=run)

def room1():
    remove()
    global which_room
    which_room=1
    global enemy1
    enemy1=enemy()
    label_low_potion_number.configure(text="Low Potion ("+str(p.low_potion)+")")
    label_high_potion_number.configure(text="High Potion ("+str(p.high_potion)+")")
    update()
    label.grid(row=0,column=0)
    label7.grid(row=0,column=1)
    label1.grid(row=0,column=2)
    label_damage_text.grid(row=1,column=1)
    label_health_text.grid(row=2,column=1)
    button_attack.grid(row=3,column=0)
    button_run.grid(row=3,column=2)
    label_attack.grid(row=4,column=0)
    label_run.grid(row=4,column=2)
    button_low_potion_use.grid(row=5,column=0)
    button_high_potion_use.grid(row=5,column=2)
    label_low_potion_number.grid(row=6,column=0)
    label_high_potion_number.grid(row=6,column=2)
    container.update()
    window_center()
room1_b_image=PhotoImage(file="forest.gif")
button_room1=Button(image=room1_b_image, command=room1)

def room2_monster():
# door 2
    remove()
    global enemy2
    enemy2=enemy()
    enemy2.health+=50
    enemy2.damage+=40
    label_low_potion_number.configure(text="Low Potion ("+str(p.low_potion)+")")
    label_high_potion_number.configure(text="High Potion ("+str(p.high_potion)+")")
    update()
    label.grid(row=0,column=0)
    label7.grid(row=0,column=1)
    label2.grid(row=0,column=2)
    label_damage_text.grid(row=1,column=1)
    label_health_text.grid(row=2,column=1)
    button_attack.grid(row=3,column=0)
    button_run.grid(row=3,column=2)
    label_attack.grid(row=4,column=0)
    label_run.grid(row=4,column=2)
    button_low_potion_use.grid(row=5,column=0)
    button_high_potion_use.grid(row=5,column=2)
    label_low_potion_number.grid(row=6,column=0)
    label_high_potion_number.grid(row=6,column=2)
    container.update()
    window_center()
room2_monster_b_image=PhotoImage(file="1-9.gif")
button_room2_monster=Button(image=room2_monster_b_image, command=room2_monster)

def key_box():
    remove()
    label6.grid(row=0,column=0)
    label_gem.grid(row=1,column=0)
    container.update()
    window_center()
    result=tkinter.messagebox.showinfo("","You got a gem!")
    if result:
       p.key=1
       game()
room2_key_box_b_image=PhotoImage(file="20.gif")
button_room2_key_box=Button(image=room2_key_box_b_image, command=key_box)

def room2_key():
# door 1
    remove()
    if p.key==0:
       button_room2_key_box.grid(row=0,column=0)
       label_box_text.grid(row=0,column=1)
       container.update()
       window_center()
    else:
       label8.grid(row=0,column=0)
       label_nothing.grid(row=0,column=1)
       container.update()
       window_center()
       result=tkinter.messagebox.showinfo("","You took the treasure already!")
       if result:
         game()
room2_key_b_image=PhotoImage(file="1-9.gif")
button_room2_key=Button(image=room2_key_b_image, command=room2_key)

def room2():
    remove()
    global which_room
    which_room=2
    button_room2_key.grid(row=0,column=0)
    #label7.grid(row=0,column=1)
    button_room2_monster.grid(row=0,column=2)
    label_door1.grid(row=1,column=0)
    label_door2.grid(row=1,column=2)
    label_choose.grid(row=0,column=1)
    container.update()
    window_center()
room2_b_image=PhotoImage(file="winter.gif")
button_room2=Button(image=room2_b_image, command=room2)

def room3():
    remove()
    global which_room
    which_room=3
    global boss1
    boss1=boss()
    label_low_potion_number.configure(text="Low Potion ("+str(p.low_potion)+")")
    label_high_potion_number.configure(text="High Potion ("+str(p.high_potion)+")")
    update()
    label.grid(row=0,column=0)
    label7.grid(row=0,column=1)
    label3.grid(row=0,column=2)
    label_damage_text.grid(row=1,column=1)
    label_health_text.grid(row=2,column=1)
    button_attack.grid(row=3,column=0)
    button_run.grid(row=3,column=2)
    label_attack.grid(row=4,column=0)
    label_run.grid(row=4,column=2)
    button_low_potion_use.grid(row=5,column=0)
    button_high_potion_use.grid(row=5,column=2)
    label_low_potion_number.grid(row=6,column=0)
    label_high_potion_number.grid(row=6,column=2)
    container.update()
    window_center()
room3_b_image=PhotoImage(file="cave.gif")
button_room3=Button(image=room3_b_image, command=room3)

def menu():
    label.grid(row=0, column=0)
    label1.grid(row=0, column=1)
    label2.grid(row=0, column=2)
    label3.grid(row=0, column=3)
    button_new.grid(row=1,column=0)
    label_new.grid(row=2,column=0)
    button_load.grid(row=1,column=1)
    label_load.grid(row=2,column=1)
    button_quit.grid(row=1,column=2)
    label_quit.grid(row=2,column=2)
    label_by.grid(row=1,column=3)
    container.update()

def save():
    data=open("stat.txt","w")
    data.write(str(p.health))
    data.write(".")
    data.write(str(p.damage))
    data.write(".")
    data.write(str(p.key))
    data.write(".")
    data.write(str(p.gold))
    data.write(".")
    data.write(str(p.egg))
    data.write(".")
    data.write(str(p.apple))
    data.write(".")
    data.write(str(p.ham))
    data.write(".")
    data.write(str(p.fish))
    data.write(".")
    data.write(str(p.bottle))
    data.write(".")
    data.write(str(p.low_potion))
    data.write(".")
    data.write(str(p.high_potion))
    data.write(".")
    data.close()
    tkinter.messagebox.showinfo("","Game is saved.")
save_b_image=PhotoImage(file="1-5.gif")
button_save=Button(image=save_b_image, command=save)

def synthesis():
    remove()
    low_bar.grid(row=4,column=0)
    high_bar.grid(row=4,column=1)
    label_material.configure(text="""%s Bottle
%s Egg
%s Ham
%s Fish
%s Apple"""%(p.bottle,p.egg,p.ham,p.fish,p.apple))
    button_info_new.grid(row=1,column=2)
    label_go_back.grid(row=2,column=2)
    button_low_potion.grid(row=1,column=0)
    button_high_potion.grid(row=1,column=1)
    label_low_potion.grid(row=2,column=0)
    label_high_potion.grid(row=2,column=1)
    label_low_potion1.grid(row=0,column=0)
    label_high_potion1.grid(row=0, column=1)
    label_material.grid(row=0,column=2)
    container.update()
    window_center()
synthesis_b_image=PhotoImage(file="3-5.gif")
button_synthesis=Button(image=synthesis_b_image, command=synthesis)

def low_potion():
    result=tkinter.messagebox.askyesno("","Do you want to synthesize this potion?")
    if result:
        if p.apple>0 and p.egg>0 and p.bottle>0:
            p.apple-=1
            p.egg-=1
            p.bottle-=1
            label_material.configure(text="""%s Bottle
%s Egg
%s Ham
%s Fish
%s Apple"""%(p.bottle,p.egg,p.ham,p.fish,p.apple))
            low_bar_add()
        else:
            tkinter.messagebox.showinfo("","You don't have enough materials!")
button_low_potion=Button(image=photo11, command=low_potion)

def high_potion():
    result=tkinter.messagebox.askyesno("", "Do you want to synthesize this potion?")
    if result:
        if p.ham>0 and p.fish>0 and p.bottle>0:
            p.ham-=1
            p.fish-=1
            p.bottle-=1
            label_material.configure(text="""%s Bottle
%s Egg
%s Ham
%s Fish
%s Apple"""%(p.bottle,p.egg,p.ham,p.fish,p.apple))
            high_bar_add()
        else:
            tkinter.messagebox.showinfo("","You don't have enough materials!")
button_high_potion=Button(image=photo12, command=high_potion)

def low_potion_use():
    result=tkinter.messagebox.askyesno("","Do you want to use low potion?")
    if result:
        if p.low_potion>0:
            p.low_potion-=1
            if hp-p.health<20 and hp-p.health>=0:
                p.health=hp
            else:
                p.health+=20
            label_player_health.configure(text=p.health)
            label_low_potion_number.configure(text="Low Potion ("+str(p.low_potion)+")")
        else:
            tkinter.messagebox.showinfo("","No more low potions!")
button_low_potion_use=Button(image=photo11, command=low_potion_use)

def high_potion_use():
    result=tkinter.messagebox.askyesno("","Do you want to use high potion?")
    if result:
        if p.high_potion>0:
            p.high_potion-=1
            if hp-p.health<50 and hp-p.health>=0:
                p.health=hp
            else:
                p.health+=50
            label_player_health.configure(text=p.health)
            label_high_potion_number.configure(text="High Potion ("+str(p.high_potion)+")")
        else:
            tkinter.messagebox.showinfo("","No more high potions!")
button_high_potion_use=Button(image=photo12, command=high_potion_use)

def info(): 
    remove()
    damage_text="Damage: "+str(p.damage)
    label_damage.configure(text=damage_text)
    health_text="Health: "+str(p.health)
    label_health.configure(text=health_text)
    label_gold.configure(text="$ "+str(p.gold))
    label_apple.configure(text=str(p.apple)+" Apple")
    label_egg.configure(text=str(p.egg)+ " Egg")
    label_ham.configure(text=str(p.ham)+ " Ham")
    label_fish.configure(text=str(p.fish)+ " Fish")
    label_bottle.configure(text=str(p.bottle)+ " Bottle")
    label10.grid(row=0, column=0)
    label4.grid(row=0,column=1)
    label5.grid(row=0,column=2)
    label13.grid(row=3,column=0)
    label14.grid(row=3,column=1)
    label15.grid(row=3,column=2)
    label16.grid(row=3,column=3)
    label17.grid(row=3,column=4)
    label_gold.grid(row=1, column=0)
    label_damage.grid(row=1,column=1)
    label_health.grid(row=1,column=2)
    label_egg.grid(row=4,column=0)
    label_apple.grid(row=4,column=1)
    label_ham.grid(row=4,column=2)
    label_fish.grid(row=4,column=3)
    label_bottle.grid(row=4, column=4)
    if p.key==1:
       label6.grid(row=0,column=3)
       label_1.grid(row=1,column=3)
       button_info_new.grid(row=0,column=4)
       label_go_back.grid(row=1,column=4)
    else:
       button_info_new.grid(row=0,column=3)
       label_go_back.grid(row=1,column=3)
    container.update()
    window_center()
info_b_image=PhotoImage(file="1-1.gif")
button_info=Button(image=info_b_image, command=info)

def store():
    remove()
    label9.grid(row=4, column=1)
    button_weapon_44.grid(row=0, column=0)
    label_weapon_44.grid(row=1, column=0)
    button_weapon_46.grid(row=0, column=1)
    label_weapon_46.grid(row=1, column=1)
    button_weapon_14.grid(row=0, column=2)
    label_weapon_14.grid(row=1, column=2)
    button_armor_24.grid(row=2, column=0)
    label_armor_24.grid(row=3, column=0)
    button_armor_28.grid(row=2, column=1)
    label_armor_28.grid(row=3, column=1)
    button_armor_22.grid(row=2, column=2)
    label_armor_22.grid(row=3, column=2)
    button_armor_26.grid(row=2, column=3)
    label_armor_26.grid(row=3, column=3)
    label10.grid(row=4,column=0)
    button_emp_bottle.grid(row=4, column=3)
    label_bottle1.grid(row=5, column=3)
    button_emp_bottle1.grid(row=4, column=2)
    label_bottle2.grid(row=5, column=2)
    label_onwer.grid(row=5,column=1)
    button_store_new.grid(row=0, column=3)
    label_go_back.grid(row=1, column=3)
    label_gold.configure(text="$ "+str(p.gold))
    label_gold.grid(row=5, column=0)
    window_center()
store_b_image = PhotoImage(file="4-8.gif")
button_store = Button(image=store_b_image, command=store)

def store_purchase_damage(in_damage,in_gold):
    result=tkinter.messagebox.askyesno("", "Do you really want to buy?")
    if result:
        if p.gold-in_gold>=0:
            p.damage+=in_damage
            p.gold-=in_gold
            label_gold.configure(text="$ "+str(p.gold))
        else:
            tkinter.messagebox.showinfo("","Not enough gold!")

def store_purchase_armor(in_health,in_gold):
    result=tkinter.messagebox.askyesno("", "Do you really want to buy?")
    if result:
        if p.gold-in_gold>=0:
            p.health+=in_health
            p.gold-=in_gold
            label_gold.configure(text="$ "+str(p.gold))
        else:
            tkinter.messagebox.showinfo("","Not enough gold!")

def weapon_44():
    store_purchase_damage(1,200)
weapon_44_image=PhotoImage(file="4-4.gif")
button_weapon_44 = Button(image=weapon_44_image, command=weapon_44)

def weapon_46():
    store_purchase_damage(2,300)
weapon_46_image=PhotoImage(file="4-6.gif")
button_weapon_46 = Button(image=weapon_46_image, command=weapon_46)

def weapon_14():
    store_purchase_damage(3,400)
weapon_14_image=PhotoImage(file="1-4.gif")
button_weapon_14 = Button(image=weapon_14_image, command=weapon_14)

def armor_24():
    store_purchase_armor(2,200)
armor_24_image=PhotoImage(file="2-4.gif")
button_armor_24 = Button(image=armor_24_image, command=armor_24)

def armor_28():
    store_purchase_armor(4,350)

armor_28_image=PhotoImage(file="2-8.gif")
button_armor_28 = Button(image=armor_28_image, command=armor_28)

def armor_22():
    store_purchase_armor(6,500)
armor_22_image=PhotoImage(file="2-2.gif")
button_armor_22 = Button(image=armor_22_image, command=armor_22)

def armor_26():
    store_purchase_armor(10,800)
armor_26_image=PhotoImage(file="2-6.gif")
button_armor_26 = Button(image=armor_26_image, command=armor_26)

def store_purchase_bottle(amount,in_gold):
    result=tkinter.messagebox.askyesno("", "Do you really want to buy?")
    if result:
        if p.gold-in_gold>=0:
            p.gold -= in_gold
            label_gold.configure(text="$ "+str(p.gold))
            p.bottle+=amount
        else:
            tkinter.messagebox.showinfo("","Not enough gold!")

def emp_bottle():
    store_purchase_bottle(1,100)
emp_bottle_image=PhotoImage(file="3-6.gif")
button_emp_bottle = Button(image=emp_bottle_image, command=emp_bottle)

def emp_bottle1():
    store_purchase_bottle(5,350)
emp_bottle_image1=PhotoImage(file="3-6.gif")
button_emp_bottle1 = Button(image=emp_bottle_image1, command=emp_bottle1)

def go_back_store():
    remove()
    game()
    container.update()
    window_center()
store_new_b_image=PhotoImage(file="1-7.gif")
button_store_new=Button(image=store_new_b_image, command=go_back_store)

def info_new():
    remove()
    game()
    container.update()
    window_center()
info_new_b_image=PhotoImage(file="1-7.gif")
button_info_new=Button(image=info_new_b_image, command=info_new)

def backmenu():
    remove()
    menu()
    container.update()
    window_center()
menu_b_image=PhotoImage(file="1-2.gif")
button_menu=Button(image=menu_b_image, command=backmenu)

def new():
    remove()
    p.health=8
    p.damage=2
    p.key=0
    p.gold=100
    p.fish=0
    p.egg=0
    p.ham=0
    p.bottle=0
    p.apple=0
    p.low_potion=0
    p.high_potion=0
    health_text="Health: "+str(p.health)
    label_health.configure(text=health_text)
    damage_text="Damage: "+str(p.damage)
    label_damage.configure(text=damage_text)
    label_gold.configure(text="$ "+str(p.gold))
    game()
new_b_image=PhotoImage(file="1-7.gif")
button_new=Button(image=new_b_image, command=new)

def game():
    remove()
    button_battle.grid(row=0,column=0)
    button_info.grid(row=0,column=1)
    button_store.grid(row=0,column=2)
    button_synthesis.grid(row=2,column=0)
    button_save.grid(row=2,column=1)
    button_menu.grid(row=2,column=2)
    label_battle.grid(row=1,column=0)
    label_info.grid(row=1,column=1)
    label_store.grid(row=1,column=2)
    label_synthesis.grid(row=3,column=0)
    label_save.grid(row=3,column=1)
    label_menu.grid(row=3,column=2)
    container.update()
    window_center()

def load():
    if os.path.isfile("stat.txt"):
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
        p.gold=int(code_list[3])
        p.egg=int(code_list[4])
        p.apple=int(code_list[5])
        p.ham=int(code_list[6])
        p.fish=int(code_list[7])
        p.bottle=int(code_list[8])
        p.low_potion=int(code_list[9])
        p.high_potion=int(code_list[10])
        data.close()
        label_bottle.configure(text=str(p.bottle))
        label_gold.configure(text="$ "+str(p.gold))
        health_text="Health: "+str(p.health)
        label_health.configure(text=health_text)
        damage_text="Damage: "+str(p.damage)
        label_damage.configure(text=damage_text)
        game()
    else:
        tkinter.messagebox.showinfo("","No saved game found!")
load_b_image=PhotoImage(file="2-9.gif")
button_load=Button(image=load_b_image, command=load)

def quit():
    result=tkinter.messagebox.askyesno("", "Do you really want to quit?")
    if result==True:
        sys.exit(0)
quit_b_image=PhotoImage(file="5-4.gif")
button_quit=Button(image=quit_b_image, command=quit)

def window_center():
    container.update()
    # lines below this:
    x = container.winfo_screenwidth()/2 - container.winfo_width()/2
    y = container.winfo_screenheight()/2 - container.winfo_height()/2
    container.geometry("+%d+%d" % (x, y))
    # referenced from: https://bbs.archlinux.org/viewtopic.php?id=149559
    # author: vadmium
    # modified

menu()
window_center()
container.mainloop()
