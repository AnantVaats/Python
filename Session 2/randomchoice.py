import random

print('Rock','paper','Scissors!')

while True:
    user_choice=input("enter: ").strip().lower()
    if user_choice in ['rock','paper','scissors']:
        break
    else:
        print('Invalid')

computer_choice = random.choice(['rock','paper','scissors'])
print('you chose: ',user_choice)
print('computer choice',computer_choice)

#Determine the winner
if user_choice== computer_choice:
    print('tie')
elif (computer_choice=='scissors' and user_choice=='rock') or (computer_choice=='rock' and user_choice=='paper') or (computer_choice=='paper' and user_choice=='scissors'):
    print('You win')
else:
    print('Computer wins')