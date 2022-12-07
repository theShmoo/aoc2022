"""day 07 of aoc2022"""


def calc_dir_size(dir, sizes):
    for k, v in dir.items():
        if k == '..':
            pass
        elif type(v) is dict:
            dir['.'] += calc_dir_size(v, sizes)
        else:
            dir['.'] += v

    sizes.append(dir['.'])

    return dir['.']


def day_07(part, data):
    """solve day 07 for the given part and data."""

    filesystem = {'/': {'.': 0}}

    current = filesystem['/']

    for d in data[1:]:
        if d.startswith('$'):
            if d.startswith('$ cd'):
                current = current[d[5:]]
        else:
            if d.startswith('dir'):
                current[d[4:]] = {'..': current, '.': 0}
            else:
                file = d.split(' ')
                current[file[1]] = int(file[0])

    current = filesystem['/']
    result = []
    calc_dir_size(current, result)

    if part == 1:
        return sum(filter(lambda r: r <= 100000, result))
    else:
        total_space = 70000000
        free_space = total_space - filesystem['/']['.']
        needed_space = 30000000
        to_free = needed_space - free_space
        return min(filter(lambda r: r > to_free, result))
