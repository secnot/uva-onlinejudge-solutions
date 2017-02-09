from sys import stdin

PORT = "port"
STARBOARD = "starboard"


def loadcase():

    # Discard empty line
    _ = stdin.readline()
    
    # Ferry length in cm
    length = int(stdin.readline())*100

    # Read car dimmensions until 0 is reached
    cars = []

    car = int(stdin.readline())
    while car>0:
        cars.append(car)
        car = int(stdin.readline())

    return length, cars 



def best_dist(ferry_length, cars):

    csum =[0]
    for c in cars:
        csum.append(c+csum[-1])

    # Using dicts instead of lists because they're faster for sparse matrices
    dp = [dict() for _ in range(len(cars)+1)]
    dp[0][0] = True 
    side = [dict() for _ in range(len(cars)+1)]

    last_car = 0
    for i, car in enumerate(cars, 1):
        for j in dp[i-1].keys():
            # Load car into port side if there is enough space
            if ferry_length-(csum[i-1]-j) >= car:
                dp[i][j] = True
                side[i][j] = PORT
                last_car = i

            # Load car starboard side if there is enough space
            if ferry_length-j>=car:
                dp[i][j+car] = True
                side[i][j+car] = STARBOARD
                last_car = i

    # Select one of the valid combinations (any will do)
    last_length = list(dp[last_car].keys())[0]

    # Recostruct selected combination from last to first
    sides_chosen = []
    while (last_length in side[last_car]):
        s = side[last_car][last_length]
        sides_chosen.append(s)
        if s == STARBOARD:
            last_length -= cars[last_car-1]
        last_car -= 1
    
    return list(reversed(sides_chosen))



if __name__ == '__main__':
    ncases = int(stdin.readline())

    for c in range(ncases):
        flength, cars = loadcase()
        sides = best_dist(flength, cars)
        print(len(sides))
        [print(s) for s in sides]
        if c+1!= ncases:
            print()

