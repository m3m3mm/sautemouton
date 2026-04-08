with open("niveau_info.txt","r") as f:
    list = f.read().splitlines()
    f.close()

personnage = {"position": (0,0), "speed": (0,0)}
lst_blocks = []
print(list)

position = list[0].split(", ",)
personnage["position"] = (int(position[0]),int(position[1]))
print(personnage)