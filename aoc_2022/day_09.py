"""day 09 of aoc2022"""


def sign(x):
    return bool(x > 0) - bool(x < 0)


def update_tail(head, tail):
    t_x, t_y = tail

    diff_x = head[0] - t_x
    diff_y = head[1] - t_y

    if abs(diff_x) == 2 or abs(diff_y) == 2:
        t_x += sign(diff_x)
        t_y += sign(diff_y)

    return (t_x, t_y)


def day_09(part, data):
    """solve day 09 for the given part and data."""

    directions = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}

    num_tails = 2 if part == 1 else 10
    tails = [(0, 0)] * num_tails
    visited = set()
    visited.add(tails[-1])

    for d in data:
        s = d.split(' ')
        direction = directions[s[0]]
        moves = int(s[1])

        for m in range(moves):
            tails[0] = (tails[0][0] + direction[0], tails[0][1] + direction[1])
            for t in range(1, num_tails):
                tails[t] = update_tail(tails[t-1], tails[t])
            visited.add(tails[-1])

    return len(visited)
