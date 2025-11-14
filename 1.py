class IOString:
    def __init__(self):
        self.str1 = "default value"   # default value for string

    def get_string(self):
        self.str1 = input("Enter a string: ")

    def print_uppercase(self):
        print("String in Uppercase:", self.str1.upper())


# Creating object and calling methods
obj = IOString()
obj.get_string()
obj.print_uppercase()
