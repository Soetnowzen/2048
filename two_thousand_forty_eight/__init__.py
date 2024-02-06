from enum import Enum


class Direction(Enum):
    LEFT = 0
    UP = 1
    RIGHT = 2
    DOWN = 3

def execute(data):
    if Direction(data[-1]) == Direction.LEFT:
        changed = True
        while changed:
            data, changed = __move_left(data)
        return data
    return None

def __move_left(data):
    result = []
    changed = False
    for y in range(len(data[0:4])):
        result.append([])
        for x in range(len(data[y])):
            result[y].append(0)
            if x == 0 or data[y][x] == 0:
                result[y][x] = data[y][x]
                pass
            else:
                previous = data[y][x-1]
                if previous == 0:
                    result[y][x-1] = data[y][x]
                    result[y][x] = 0
                    changed = True
                elif previous == data[y][x]:
                    result[y][x-1] = previous + data[y][x]
                    result[y][x] = 0
                    changed = True
                else:
                    result[y][x] = data[y][x]
    return result, changed