INPUT = 'input.txt'
TEST_INPUT = [0,3,0,1,-3]


def input_to_int(input):
    return [int(num) for num in input]

def run(maze, offset_limit=None):
    #print(len(maze), maze)
    step = 0
    pos = 0
    while True:
        #print(step, pos, maze)
        try:
            jump = maze[pos]
            if offset_limit and jump >= offset_limit:
                maze[pos] -= 1
            else:
                maze[pos] += 1
            pos += jump
        except:
            #print(step)
            return step
        else:
            step += 1

def test(input, offset_limit, answer):
    test_input = input_to_int(input)
    assert run(test_input, offset_limit) == answer

def escape(offset=None):
    with open(INPUT) as file:
        input = file.readlines()
    maze = input_to_int(input)
    return run(maze, offset)


test(TEST_INPUT, None, 5)
test(TEST_INPUT, 3, 10)

print(escape())
print(escape(3))