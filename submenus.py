from menu import Menu
import requests


class MainMenu(Menu):

  def __init__(self, q, classname):
    self.choices = {"1": ("Cake", self.cake), "2": ("Strawberry", self.straw)}
    super().__init__(self.choices, q, classname)

  def cake(self):
    self.output("Hello cake")

  def straw(self):
    self.name = input("please enter your name: ")
    self.output(f"Hello {self.name}")
    self.strawb = Strawberry(self.que, "Strawberry")
    self.strawb.run()


class Strawberry(Menu):

  def __init__(self, q, classname):
    self.choices = {"1": ("Hat", self.hat), "2": ("Cap", self.cap)}
    super().__init__(self.choices, q, classname)

  def getcat(self):
    self.output(requests.get('https://w3schools.com/python/demopage.htm').text)

  def hat(self):
    self.output("Hellooo hat!")
    self.addfunctoq(self.getcat)

  def cap(self):
    self.output("I like caps")
