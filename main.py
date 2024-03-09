import requests as r
import time as t
import smtplib
print('Initializing' + '\n')

def Spawn_Alert(msg, to):
  user = to
  #App Password for your email
  password = ''
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()
  server.login(user, password)
  server.sendmail(user, to, msg)
  server.quit()

#Pokedex IDs of Pokemon you want alerts for
#Example [1,3,66,675,800]
pokemon = []

while True:
  spawn_url = 'https://poketwitch.bframework.de/info/events/last_spawn/'
  latest_spawn = r.get(spawn_url).json()
  latest_spawn_timestamp = latest_spawn["event_time"]
  with open('Last_Spawn.txt', 'r') as file:
    if file.read() == latest_spawn_timestamp:
      t.sleep(latest_spawn["next_spawn"])
    else:
      with open('Last_Spawn.txt', 'w') as file:
        file.write(str(latest_spawn_timestamp))
      pokemon_id = latest_spawn['order']
      if pokemon_id in pokemon:
        pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}/'
        pokemon_data = r.get(pokemon_url).json()
        name = pokemon_data['name'].title()
        #User's Email
        users_email=''
        Spawn_Alert(f'{name} Spawn', users_email)
        print(f'Sent Alert for {name} spawn')
      t.sleep(latest_spawn["next_spawn"])
