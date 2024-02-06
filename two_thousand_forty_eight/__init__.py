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
        data, changed = __merge_left(data)
        if changed:
            data, changed = __move_left(data)
        return data
    elif Direction(data[-1] == Direction.UP):
        changed = True
        while changed:
            data, changed = __move_up(data)
        data, changed = __merge_up(data)
        if changed:
            data, changed = __move_up(data)
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
                else:
                    result[y][x] = data[y][x]
    return result, changed

def __merge_left(data):
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
                if previous == data[y][x]:
                    result[y][x-1] = previous + data[y][x]
                    result[y][x] = 0
                    changed = True
                else:
                    result[y][x] = data[y][x]
    return result, changed

def __move_up(data):
    result = []
    changed = False
    for y in range(len(data[0:4])):
        result.append([])
        for x in range(len(data[y])):
            result[y].append(0)
            if y == 0 or data[y][x] == 0:
                result[y][x] = data[y][x]
                pass
            else:
                previous = data[y-1][x]
                if previous == 0:
                    result[y-1][x] = data[y][x]
                    result[y][x] = 0
                    changed = True
                else:
                    result[y][x] = data[y][x]
    return result, changed

def __merge_up(data):
    result = []
    changed = False
    for y in range(len(data[0:4])):
        result.append([])
        for x in range(len(data[y])):
            result[y].append(0)
            if y == 0 or data[y][x] == 0:
                result[y][x] = data[y][x]
                pass
            else:
                previous = data[y-1][x]
                if previous == data[y][x]:
                    result[y-1][x] = previous + data[y][x]
                    result[y][x] = 0
                    changed = True
                else:
                    result[y][x] = data[y][x]
    return result, changed