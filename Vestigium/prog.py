count = int(input())
for i in range(1, count + 1):
    N = int(input())
    grid = []
    for j in range(N):
        grid.append(str(input()).split(" "))

    output = [0, 0, 0]
    trace = 0
    for k in range(len(grid)):
        trace += int(grid[k][k])
    output[0] = trace
    for row in range(len(grid)):
        if len(set(grid[row])) != len(grid[0]):
            output[1] += 1

    for c in range(len(grid[0])):
        current = []
        for row in range(len(grid)):
            current.append(grid[row][c])

        if len(current) != len(set(current)):
            output[2] += 1
    print("Case #{}: {}".format(i, ' '.join(str(out) for out in output)))
