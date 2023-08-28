from kivy.app import App # Import the App class.
from kivy.uix.gridlayout import GridLayout # Import GridLayout class, used as base for Root Widget.
from kivy.uix.label import Label # Import Label class for displaying text.
from kivy.uix.textinput import TextInput # Import the TextInput class for...text input.

class LoginScreen(GridLayout): # Our Root Widget

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs) # Overriding the __init__() method to add widgets and define their behaviors.
        self.cols = 2 # Creating 2 columns.
        self.add_widget(Label(text='User Name')) # Creating one widget for a User Name input in Column 1.
        self.username = TextInput(multiline=False) # Creating a one-line text input.
        self.add_widget(self.username)
        self.add_widget(Label(text='Password'))
        self.password = TextInput(password = True, multiline=False)
        self.add_widget(self.password)

class MyApp(App):

    def build(self):
        return LoginScreen()
    
if __name__ == '__main__':
    MyApp().run()