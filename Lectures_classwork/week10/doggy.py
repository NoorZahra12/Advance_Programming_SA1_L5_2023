import tkinter as tk
app=tk.Tk()

class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def bark(self):
        return self.name, ", says: Woof!"

dog1=Dog("German Shepard",10)
dog2=Dog("Husky",8)
olderDog=dog1 if dog1.age>dog2.age else dog2

class DogGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My Dogs")
        self.geometry('450x300')
        self.display_dog_info()

    def display_dog_info(self):
        label1=tk.Label(self,"Dog1:{dog1.name},{dog1.age}years old")
        label1.pack()
        label2=tk.Label(self,"Dog1:{dog1.name},{dog1.age}years old")
        label2.pack()
        olderDog=tk.Label(self,text="The older dog{olderDog}")
        olderDog.pack()

def woof(self):
    result=olderDog.woof()
    woof_label=tk.Label(self,text=result)
    woof_label.pack()

if __name__=="__main__":
    app=DogGUI()
app.mainloop()