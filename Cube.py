from rubikscolorresolver.solver import resolve_colors

def resolveCube(cubeString):
    cube = {}
    for i in range(0, 54):
        cube[str(i)] = getColor(cubeString[i])

    solve = resolve_colors("cube.txt")

    movesList = solve.split(" ")

    resolution = simplifyResolution(movesList)

    print("Resolution: " + str(resolution))

    return cube

def getColor(color):
    if color == "W":
        return [255, 255, 255]
    if color == "G":
        return [0, 102, 0]
    if color == "R":
        return [204, 51, 0]
    if color == "B":
        return [0, 0, 153]
    if color == "O":
        return [255, 153, 0]
    if color == "Y":
        return [255, 255, 0]

def writeCubeToFile(cube):
    with open("cube.txt", "w") as file:
        file.write(str(cube))

def readCubeFromFile():
    with open("cube.txt", "r") as file:
        cube = file.read()
        return cube

def askForCube():
    cubeString = input("Enter the cube: ")

    data = resolveCube(cubeString)
    print(data)

def simplifyResolution(movesList):
    count = 0
    moves = []
    size = len(movesList)

    while count < size:
        item = movesList[count]
        item2 = movesList[count+1]
        item3 = "X" if count+2 >= size else movesList[count+2]

        if ((item == item2) and (item2 == item3)):
            moves.append(item+"'")
            count = count+3
        elif ((item == item2) and (item2 != item3)):
            moves.append(item+"2")
            count = count+2
        elif ((item != item2) and (item2 == item3)):
            moves.append(item)
            count = count+1
        elif ((item != item2) and (item2 != item3)):
            moves.append(item)
            count = count+1
    
    return " ".join(moves)

def main():
    askForCube()

main()

# RRRWWWWWWWOOGGGRRYBBBWOOGGGRRYBBBWOOGGGRRYBBBYYYYYYOOO