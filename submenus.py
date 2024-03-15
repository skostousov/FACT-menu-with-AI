from menu import Menu
import requests
import sqlite3

# Function to authenticate the user based on the provided credentials
def authenticate(username, password):
  # Connect to the SQLite database
  conn = sqlite3.connect('path/to/database.db')
  cursor = conn.cursor()

  # Query the database to check if the user exists and the password is correct
  cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
  user = cursor.fetchone()

  # Close the database connection
  conn.close()

  # Return True if the user exists and the password is correct, otherwise return False
  return user is not None
print("Hello")
print("Hi")
print("Banana")  
class MainMenu(Menu):
  def __init__(self, q, classname):
    self.choices = {"1": ("Sign In", self.signin), "2": ("Create Account", self.signup)}
    super().__init__(self.choices, q, classname)

  def signin(self):
    # Prompt the user for their username and password
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    # Authenticate the user
    if authenticate(username, password):
      self.signedinmenu = SignedinMenu(self.que, "Signed In Menu", username)
      self.signedinmenu.run()
    else:
      print("Invalid username or password. Access denied.")

  def signup(self):
    # Prompt the user for their username and password
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    repeat_password = input("Repeat your password: ")

    # Check if the passwords match
    if password != repeat_password:
      print("Passwords do not match. Please try again.")
      return

    # Check if the password meets the criteria for a good password
    if not is_good_password(password):
      print("Password does not meet the criteria. Please try again.")
      return

    # Connect to the SQLite database
    conn = sqlite3.connect('path/to/database.db')
    cursor = conn.cursor()

    # Check if the username already exists in the database
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    existing_user = cursor.fetchone()
    if existing_user:
      print("Username already exists. Please choose a different username.")
      conn.close()
      return

    # Insert the new user into the database
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()

    # Close the database connection
    conn.close()

    print("User created successfully. You can now sign in.")

def is_good_password(password):
  # Add your password criteria here
  # For example, you can check the length, presence of special characters, etc.
  return len(password) >= 8