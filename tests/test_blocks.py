from tetris.blocks import blocks, rotate_block

def test_block_0():
    block = blocks[0]
    assert block == [[1, 1, 1, 1]]

def test_block_1():
    block = blocks[1]
    assert block == [[0, 1, 0], [1, 1, 1]]

def test_block_2():
    block = blocks[2]
    assert block == [[0, 0, 1], [1, 1, 1]]

def test_block_3():
    block = blocks[3]
    assert block == [[1, 0, 0], [1, 1, 1]]

def test_block_4():
    block = blocks[4]
    assert block == [[1, 1], [1, 1]]

def test_block_5():
    block = blocks[5]
    assert block == [[1, 1, 0], [0, 1, 1]]

def test_block_6():
    block = blocks[6]
    assert block == [[0, 1, 1], [1, 1, 0]]


def test_rotate_block_0():
    block = rotate_block(blocks[0])
    assert block == [[1], [1], [1], [1]]

def test_rotate_block_1():
    block = rotate_block(blocks[1])
    assert block == [[1, 0], [1, 1], [1, 0]]
