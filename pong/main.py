from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector


class PongBall(Widget):

    # Velocity of the ball on x and y axis.
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    # ReferenceListProperty allows use of ball.velocity as shorthand.
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

class PongGame(Widget):
    pass

class PongApp(App):
    def build(self):
        return PongGame()
    
if __name__ == '__main__':
    PongApp().run()