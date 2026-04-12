with open("niveau_info.txt","r") as f:
    list = f.read().splitlines()
    f.close()

character = {"position": (0,0), "velocity": (0,0)}
lst_blocks = []
print(list)

position = list[0].split(", ",)
character["position"] = (int(position[0]),int(position[1]))
print(character)

# testing for tg