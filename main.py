import requests as r
import time as t
import smtplib
print("Initializing" + '\n')

def Spawn_Alert(msg, to):
  user = 'brickuser24@gmail.com'
  password = 'algr nhzi phpe wimx'
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()
  server.login(user, password)
  server.sendmail(user, to, msg)
  server.quit()

pokemon = [26, 31, 34, 45, 58, 59, 62, 64, 65, 68, 71, 72, 73, 76, 82, 91, 93, 94, 95, 112, 121, 129, 130, 131, 133, 134, 135, 136, 142, 143, 149, 169, 176, 186, 195, 196, 197, 199, 207, 208, 212, 213, 215, 217, 221, 226, 227, 229, 230, 242, 247, 248, 272, 275, 281, 282, 289, 306, 321, 323, 330, 334, 349, 350, 364, 365, 373, 375, 376, 405, 407, 408, 409, 411, 416, 418, 419, 423, 426, 429, 430, 442, 443, 444, 445, 446, 447, 448, 450, 454, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 477, 478, 479, 525, 526, 529, 530, 533, 534, 536, 537, 542, 545, 552, 553, 554, 555, 563, 566, 567, 571, 576, 579, 584, 589, 596, 597, 598, 601, 604, 607, 608, 609, 611, 612, 621, 623, 624, 625, 629, 630, 632, 635, 636, 637, 662, 663, 668, 670, 671, 675, 680, 681, 691, 697, 700, 701, 703, 706, 712, 713, 715, 733, 738, 745, 747, 748, 757, 758, 760, 763, 764, 767, 768, 774, 776, 778, 784, 823, 826, 836, 838, 839, 841, 842, 846, 847, 849, 851, 855, 858, 860, 861, 862, 864, 866, 867, 868, 869, 879, 884, 885, 886, 887]

while True:
  spawn_url = "https://poketwitch.bframework.de/info/events/last_spawn/"
  latest_spawn = r.get(spawn_url).json()
  latest_spawn_timestamp = latest_spawn["event_time"]
  with open("Last_Spawn.txt", "r") as file:
    if file.read() == latest_spawn_timestamp:
      t.sleep(latest_spawn["next_spawn"])
    else:
      with open("Last_Spawn.txt", "w") as file:
        file.write(str(latest_spawn_timestamp))
      pokemon_id = latest_spawn["order"]
      if pokemon_id in pokemon:
        pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}/'
        pokemon_data = r.get(pokemon_url).json()
        name = pokemon_data['name'].title()
        Spawn_Alert(f'{name} Spawn', 'brickuser24@gmail.com')
        print(f"Sent Alert for {name} spawn")
      t.sleep(latest_spawn["next_spawn"])
