class dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print (f"{self.name} is {self.age} years old.")
        
    def __str__(self):
        return f"{self.name} is {self.age} years."
        
def main():
     my_dog = dog("Kavin", 3)
     my_dog.info()
     your_dog = dog("jame", 0.5)
     your_dog.info()
     
if __name__ == "__main__":
    main()
        
