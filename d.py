import turtle
from turtle_chat_client import Client
from turtle_chat_widgets import Button, TextInput
class TextBox(TextInput):
    def draw_box(self):
        print("a")

w=TextBox()
w.draw_box()
