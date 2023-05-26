import random
import tkinter as tk

#time, @param currentTime
class time:
    destination=3000
    def __init__(self,player):
        initial=random.randrange(-3000,1000000,100)
        self.currentTime=self.destination+initial
        if(initial>0):
            print(f"{player.name} travels {initial} years forwards. Now it's year {self.currentTime}")
        else:
            print(f"{player.name} travels {initial} years back. Now it's year {self.currentTime}")

#protagonist, @param name,energy,experience,memory        
class protagonist:
    trueName="Philip J. Fry"
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
        self.energy=100
        self.memory=0
        self.experience=0
    def getEnergy(self):
        return self.energy
    def getMemory(self):
        return self.memory
    def getExperience(self):
        return self.experience
    def setEnergy(self,energy):
        self.energy=energy
    def setMemory(self,memory):
        self.memory=memory
    def setExperience(self,experience):
        self.experience=experience

#time machine, @param level, takes in time and player data
class timeMachine():
    def __init__(self,player):
        self.level=1
        self.machine_label = tk.Label(window,text=f"{player.name}'s machine is level {self.level}")
        self.machine_label.pack()
        self.use_button = tk.Button(window,text="Use",command=self.use)
        self.use_button.pack()
        
    def getLevel(self):
        return self.level
    def upgrade(self):
        if(self.level<4):
            self.level+=1
    def use(self,player,time_new):
        if self.getLevel()==1:
           change=random.randrange(-100,100,10)
           while change==0:
               change=random.randrange(-100,100,10)
        elif self.getLevel()==2:
            change=random.randrange(-10,10,1)
            while change==0:
               change=random.randrange(-10,10,10)
        elif self.getLevel()==3:
            change=int(input("How many years do you want to travel?"))
            while change==0:
               change=int(input("How many years do you want to travel?"))
        time_new.currentTime+=change
        if self.getLevel()==4:
            time_new.currentTime=time_new.destination
        if(change>0):
            print(f"{player.name} travels {abs(change)} years forwards. Now it's year {time_new.currentTime}")
        else:
            print(f"{player.name} travels {abs(change)} years back. Now it's year {time_new.currentTime}")
        player.setEnergy(player.getEnergy()-5)
        player.setExperience(player.getExperience()+5)

class event():
    pass

#main
def start():
    
    def exit():
       global command
       command = "exit"
    greeting.config(text=name_box.get().strip())
    name_label.pack_forget()
    name_box.pack_forget()
    gender_label.pack_forget()
    gender_box.pack_forget()
    go_button.pack_forget()
    
    exit_button = tk.Button(window,text="Exit",command=exit)
    exit_button.pack()
    event = tk.Label(window,text="")
    event.pack()

    player=protagonist(name_box.get().strip(),gender_box.get().strip())
    time_new=time(player)
    machine=timeMachine(player)

    while(time_new.currentTime!=time_new.destination and player.getEnergy()!=0):
      if(command=="use"):
         machine.use(player,time_new)
      if(command=="exit"):
           break
      event.config(text=f"Exprience: {player.getExperience()}")
      print(f"Energy: {player.getEnergy()}")
    if command=="exit":
       event.config(text=f"Bye,{player.name}")
    if player.energy==0 and player.memory<50:
      event.config(text=f"{player.name} is tired. {player.gender} no longer wants to return. What to do now? Just opens a six pack and waits to watch the end of the universe.")
    elif time_new.currentTime==time_new.destination and player.getMemory()==100:
       event.config(text=f"{player.name} is back. {player.gender} stands at the entrance of Planet Express and realizes that {player.gender} has a date with Leela")

window = tk.Tk()
name_label = tk.Label(window,text="What's your name?")
name_label.pack()
name_box = tk.Entry(window)
name_box.pack()
gender_label = tk.Label(window,text="What's you pronoun?")
gender_label.pack()
gender_box = tk.Entry(window)
gender_box.pack()
go_button = tk.Button(window,text="Go",command=start)
go_button.pack()
greeting = tk.Label(window,text="")
greeting.pack()

window.mainloop()


