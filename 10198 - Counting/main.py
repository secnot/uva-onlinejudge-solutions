from sys import stdin


def generate_table(num):
    # t[n] = 2*t[n-1]+t[n-2]+t[n-3]
    t = [0, 2, 5, 13]
    for n in range(4, num):
        t.append(2*t[n-1]+t[n-2]+t[n-3])
    return t


if __name__ == '__main__':

    TABLE = generate_table(1001)
    
    while True:
        line = stdin.readline()
        if not line:
            break

        print(TABLE[int(line)])

