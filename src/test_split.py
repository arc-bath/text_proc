import web_text as wt

def test_split_macbeth():
    '''
    Test split macbeth on 'Actus'
    '''
    link = "http://www.gutenberg.org/cache/epub/2264/pg2264.txt"

    expect = 6

    text = wt.open_page(link)

    key_word = 'Actus'

    split = wt.split_strip_text(text, key_word)

    assert len(split) == expect

def test_strip_macbeth_start():
    '''
    Test split and strip macbeth on 'Actus' using start values
    '''
    link = "http://www.gutenberg.org/cache/epub/2264/pg2264.txt"

    text = wt.open_page(link)

    key_word = 'Actus'

    for i in range(6):
        expect = 6 - i
        split = wt.split_strip_text(text, key_word, start = i)

        assert len(split) == expect

def test_strip_macbeth_stop():
    '''
    Test split and strip macbeth on 'Actus' using stop values
    '''
    link = "http://www.gutenberg.org/cache/epub/2264/pg2264.txt"

    text = wt.open_page(link)

    key_word = 'Actus'

    for i in range(1,6):
        expect = i
        split = wt.split_strip_text(text, key_word, stop = i)

        assert len(split) == expect

def test_strip_macbeth_both():
    '''
    Test split and strip macbeth on 'Actus' using stop values
    '''
    link = "http://www.gutenberg.org/cache/epub/2264/pg2264.txt"

    text = wt.open_page(link)

    key_word = 'Actus'

    for i in range(0,6):
        for j in range(i+1,6):
            expect = j - i
            split = wt.split_strip_text(text, key_word, start = i, stop = j)

            assert len(split) == expect, str(i)+'is i and j is '+str(j)
