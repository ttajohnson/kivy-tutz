# Kivy Basics

### Creating an Application <create_app.py>
    - Subclass the App class.
    - Use the build() method to return a Widget instance.
    - Instantiate the subclass and call the run() method.

### Customizing an Application <customize_app.py>
    - You can set the title and icon of your application in the build() method; icons must be in main file directory.

### A Note on calling super().
    - super() provides a way to access parent class methods that is more maintainable and flexible, especially when dealing with multiple inheritance. It allows you to avoid hard-coding parent class names in your methods and ensures that, in complex inheritance scenarios, each method is called exactly once.