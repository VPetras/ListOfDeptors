#!/usr/bin/python3
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class SigninWindow(BoxLayout):


    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def validate_user(self):
        user = self.ids.username_field
        pwd = self.ids.pwd_field
        info = self.ids.info

        uname = user.text
        passw = pwd.text

        if uname == '' or passw == '':
            info.text = '[color=#FF0000]username and/ or password required[/color]'
        else:
            if uname == 'admin' and passw == 'admin':
                info.text = '[color=#00FF00]Logged In successfully!!![/color]'
                self.ids.username_field.text = ""
                self.ids.pwd_field.text = ""

            else:
                info.text = '[color=#FF0000]Invalid Username and/or Password[/color]'
                self.ids.pwd_field.text = ""

class ListOfDeptors(App):
    def build(self):
        return SigninWindow()

if __name__ == '__main__':
    sa = ListOfDeptors()
    sa.run()