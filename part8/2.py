if __name__ == "__main__":
    n = 7
    dx = [0] * (n+2)
    dx[1] = 1
    dx[2] = 2

    for i in range(3, n+2):
        dx[i] = dx[i-1] + dx[i-2]

    print(dx[n+1])