"""day 09 of aoc2022"""


directions = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}


def update_head(head, direction):
    dir = directions[direction]
    return (head[0] + dir[0], head[1] + dir[1])


def sign(x):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    return 0


def update_tail(head, tail):
    h_x, h_y = head
    t_x, t_y = tail

    diff_x = h_x - t_x
    diff_y = h_y - t_y

    if abs(diff_x) == 2 or abs(diff_y) == 2:
        t_x += sign(diff_x)
        t_y += sign(diff_y)

    return (t_x, t_y)


def day_09(part, data):
    """solve day 09 for the given part and data."""

    input = []

    for d in data:
        s = d.split(' ')
        input.append((s[0], int(s[1])))

    num_tails = 2 if part == 1 else 10
    tails = [(0, 0)] * num_tails
    visited = set()
    visited.add(tails[-1])

    for i in input:
        direction, moves = i

        for m in range(moves):
            tails[0] = update_head(tails[0], direction)
            for t in range(1, num_tails):
                tails[t] = update_tail(tails[t-1], tails[t])
            visited.add(tails[-1])

    return len(visited)
