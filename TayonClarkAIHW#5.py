def MiniMax(leaves, Maximizing):
    if len(leaves) == 1:
        return leaves[0]

    mid = len(leaves) // 2
    left_half = leaves[:mid]
    right_half = leaves[mid:]


    if Maximizing:
        Maxleft_value = MiniMax(left_half, False)
        Maxright_value = MiniMax(right_half, False)

        return max(Maxleft_value, Maxright_value)

    else:
        Minleft_value = MiniMax(left_half, True)
        Minright_value = MiniMax(right_half, True)

        return min(Minleft_value, Minright_value)

Game_leaves = [3, 5, 17, 8, -2, 5, -1, 7]
Root_value = MiniMax(Game_leaves, Maximizing=True)
print(f"Root Value is: {Root_value}")



