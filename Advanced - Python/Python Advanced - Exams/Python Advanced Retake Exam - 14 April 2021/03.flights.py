def flights(*args):
    plane = {}
    for flight in range(0, len(args), 2):
        town = args[flight]
        if town == "Finish":
            break
        passengers = args[flight + 1]
        plane[town] = plane.get(town, 0) + passengers
    return plane
