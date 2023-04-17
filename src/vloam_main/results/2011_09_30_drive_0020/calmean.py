with open("TO1.txt", "r") as f:

    lines = f.readlines()

columns = [line.strip().split() for line in lines]

columns = [[float(cell) for cell in col] for col in columns]

means = [sum(col)/len(col) for col in zip(*columns)]

print("Mean values:", means)