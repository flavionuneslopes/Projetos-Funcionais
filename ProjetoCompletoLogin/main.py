from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label

from database import Database

def invalid_login():
    pop = Popup(
        title="Invalid Login",
        content=Label(text="Invalid username or password."),
        size_hint=(None, None),
        size=(400, 400)
    )
    pop.open()

class CreateAccountWindow(Screen):
    namee=ObjectProperty(None)
    email=ObjectProperty(None)
    password=ObjectProperty(None)

    def submit(self):
        if self.namee.text!= "" and self.email.text!="" and self.email.text.count("@")==1 and self.email.text.count(".")>0:
            if self.password.text!="":
                db.add_user(self.email.text,self.password.text,self.namee.text)
                self.reset()
                sm.current= "login"
            else:
                invalid_form()
        else:
            invalid_form()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.namee.text = ""
        self.email.text = ""
        self.password.text = ""

class LoginWindow(Screen):
        name=ObjectProperty(None)
        password=ObjectProperty(None)

        def loginBtn(self):
            if db.validate(self.name.text, self.password.text):
                MainWindow.current= self.email.text
                self.reset()
                sm.current = "main"
            else:
                invalid_login()

        def createBtn(self):
            self.reset()
            sm.current = "create"

        def reset(self):
            self.email.text = ""
            self.password.text = ""

class MainWindow(Screen):
    n=ObjectProperty(None)
    created=ObjectProperty(None)
    email=ObjectProperty(None)
    current=""

    def logOut(self):
        sm.current = "login"

    def on_enter(self, *args):
        password, name, created= db.get_user(self.current)
        if user_data!= -1:
            password, name, created= user_data
            self.n.text = "Account Name: "+name
            self.email.text = "Email: "+self.current
            self.created.text = "Created: "+created
        else:
            self.n.text = "Account not found"
            self.email.text = ""
            self.created.text = ""

class WindowManager(ScreenManager):
    pass

kv= Builder.load_file("mk.kv")
sm=WindowManager()
db=Database("user.txt")

screens= [
    LoginWindow(name="login"),
    CreateAccountWindow(name="create"),
    MainWindow(name="main")
]
for screen in screens:
    sm.add_widget(screen)

sm.current="login"

class MymainApp(App):
    def build(self):
        return sm
    def on_press_button(self):
        print("You pressed")

if __name__ == "__main__":
    MymainApp().run()