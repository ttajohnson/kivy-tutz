# Import Kivy and set version requirement.
import kivy
kivy.require('2.2.1') # Will raise exception if version requirements unmet.

# Import the App class.
from kivy.app import App
# Import the Label class.
from kivy.uix.label import Label # Label class is a widget used for displaying text.

# Subclass the App class.
class MyApp(App):

    # Use the build() method to return a Widget, in this case Label for text-display.
    def build(self):
        self.title = 'Hello Kivy' # Set the title of your application.
        self.icon = 'TTAJPixelated.png' # Set the icon for your application; must be in same directory as your main file.
        return Label(text='Hello world')

# Instantiate the subclass and call the run() method.
if __name__ == '__main__':
    MyApp().run()