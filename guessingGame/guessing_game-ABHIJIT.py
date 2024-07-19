import random
def main():
 number_to_guess=random.randint(1,100)
 attempts=0
 correct_guess=False
 print("Enter a number between 1 to 100")
 print("Guess it!!!")

 while True:
   try:
      number_you_guessed=int(input("Enter the guess: "))
      attempts += 1
      if number_to_guess > number_you_guessed:
       print("Too Small! try again")
      elif number_to_guess < number_you_guessed:
       print("Too High guess! try again")
      else:
       print(f"WOAH! YOU GUESSED IT RIGHT,Correct number is {number_to_guess} in {attempts} attempts")
       correct_guess=True
       break
   except ValueError:
    print("Invallid input!!, please enter a number between 1 to 100")
   

if __name__=="__main__":
   main()

    