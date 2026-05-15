"""opening file to read it"""
def open_file(filename):
    with open(filename,"r") as f:
        list_info = f.read().splitlines()
        f.close()

    """creating dict structure for info keeping"""
    character = {"position": (0,0), "velocity": (0,0)}
    lst_blocks = []
    # print(list)

    """logging barashka's position"""
    position = list_info[0].split(", ",)
    character["position"] = (int(position[0]),int(position[1]))
    # print(character)

    """logging the goal for our barashek"""
    goal_l = list_info[1].split(", ",)
    goal = (int(goal_l[0]),int(goal_l[1]),int(goal_l[2]),int(goal_l[3]))
    #print(goal)

    """logging the blocks in our database for usage later"""
    for i in range(2,len(list_info)):
        block_l = list_info[i].split(", ", )
        block = (int(block_l[0]), int(block_l[1]), int(block_l[2]), int(block_l[3]))
        lst_blocks.append(block)
    return character, lst_blocks, goal

character, lst_blocks, goal = open_file("niveau_info.txt")