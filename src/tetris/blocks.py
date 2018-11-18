

blocks = [
    [[1, 1, 1, 1]],

    [[0, 1, 0],
     [1, 1, 1]],

    [[0, 0, 1],
     [1, 1, 1]],

    [[1, 0, 0], 
     [1, 1, 1]],

    [[1, 1], 
     [1, 1]],

    [[1, 1, 0],
     [0, 1, 1]],

    [[0, 1, 1],
     [1, 1, 0]]
]

def rotate_block(block):
    return [
        [block[i][j] for i in range(len(block)-1, -1, -1)]
        for j in range(0, len(block[0]))
    ]