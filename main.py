player = {'name': 'Lili', 'attack': 10, 'heal': 12, 'health': 100}
monster = {'name': 'Bug', 'attack': 12, 'health': 100}

print('Welcome to 21sw_Coding class Monster Game!!')
print('What do you want to do?')
print('1) Attack')
print('2) Heal')

player_choice = input()

if player_choice == '1':
  print('Attack! No mercy!')
  
elif player_choice == '2':
  print('Healing player...')

else:

  print('Something went wrong. I did not understand you. Do you want to try again?'
