import itertools

INPUT = 265149

class Taxi:
    def __init__(self):
        # Order is important here, for a counter-clockwise spiral starting to the right
        self.dirs = itertools.cycle([
            (1,0),   # cartesian right
            (0,1),   # up
            (-1,0),  # left
            (0,-1),  # down
        ])
        self.facing = next(self.dirs)
        self.position = (0,0)
        self.values = {self.position: 1}
        self.history = [self.position]

    def left(self):
        self.facing = next(self.dirs)

    def right(self):
        # 2 wrongs don't make a right, but 3 lefts do
        # More seriously, can't go backwards with an iterator
        # Turns out this is never used in a counter-clockwise spiral...
        self.right()
        self.right()
        self.right()

    def step(self):
        new_position = tuple([self.facing[i] + self.position[i] for i in range(len(self.position))])
        value = sum([self.get_value(adj) for adj in self.get_adjacent(new_position)])
        self.values[new_position] = value
        self.position = new_position
        self.history.append(new_position)

    def build_sequence(self, input):
        seq = [0]
        a = 1
        b = 1
        for i in range(input):
            value = a*b
            #print(value)
            seq.append(value)
            if value > input:
                break
            if i % 2 == 0:
                a += 1
            else:
                b += 1
        return seq

    def spiral(self, input):
        seq = self.build_sequence(input)
        for i in range(input-1):
            self.step()
            if i+1 in seq:
                self.left()
        return self.position

    def get_distance(self):
        return sum([abs(axis) for axis in self.position])

    def get_adjacent(self, position):
        adj = []
        for x in range(-1,2):
            for y in range(-1,2):
                adj.append((position[0]+x, position[1]+y))
        return adj

    def get_value(self, position):
        return self.values.get(position, 0)

def get_spiral_distance(input):
    taxi = Taxi()
    taxi.spiral(input)
    #print(taxi.build_sequence(input))
    #print(taxi.history)
    return taxi.get_distance()

def calc_value(square):
    taxi = Taxi()
    taxi.spiral(square)
    #print(taxi.values)
    return max(taxi.values.values())

def test(input, answer):
    dist = get_spiral_distance(input)
    #print(dist, answer)
    assert dist == answer

def test_values():
    assert calc_value(1) == 1
    assert calc_value(2) == 1
    assert calc_value(4) == 4
    assert calc_value(6) == 10
    assert calc_value(7) == 11
    assert calc_value(23) == 806

def find_value(input):
    for i in range(input):
        value = calc_value(i)
        #print(value)
        if value > input:
            return value

test(1, 0)
test(12, 3)
test(23, 2)
test(1024, 31)

print(get_spiral_distance(INPUT))

test_values()
print(find_value(INPUT))

