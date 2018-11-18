from tetris.blocks import blocks

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
    assert block == [[0, 1, 0], [1, 1, 1]]

def test_block_4():
    block = blocks[5]
    assert block == [[1, 1], [1, 1]]