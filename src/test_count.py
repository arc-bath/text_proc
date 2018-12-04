import web_text as wt

def test_count_rjg20():
    '''
    Test count words in page
    '''
    link = "https://people.bath.ac.uk/rjg20/index.html"

    expect = 679

    text = wt.open_page(link)

    assert wt.count_words(text) == expect

def test_count_macbeth():
    '''
    Test count words in the Scottish play
    '''
    link = "http://www.gutenberg.org/cache/epub/2264/pg2264.txt"

    expect = 20347

    text = wt.open_page(link)

    assert wt.count_words(text) == expect

def test_count_hamlet():
    '''
    Test count words in the Hamlet
    '''
    link = "http://www.gutenberg.org/cache/epub/2265/pg2265.txt"

    expect = 32211

    text = wt.open_page(link)

    assert wt.count_words(text) == expect

def test_occs_macbeth1():
    '''
    Test count occs in the Scottish play
    '''
    link = "http://www.gutenberg.org/cache/epub/2264/pg2264.txt"

    words = [ "Macbeth" ]
    expect = [ 70 ]

    text = wt.open_page(link)

    assert wt.count_occs(text, words) == expect

def test_occs_macbeth2():
    '''
    Test count occs in the Scottish play
    '''
    link = "http://www.gutenberg.org/cache/epub/2264/pg2264.txt"

    words = [ "Macduff" ]
    expect = [ 28 ]

    text = wt.open_page(link)

    assert wt.count_occs(text, words) == expect

def test_occs_macbeth3():
    '''
    Test count occs in the Scottish play
    '''
    link = "http://www.gutenberg.org/cache/epub/2264/pg2264.txt"

    words = [ "Macbeth", "Macduff" ]
    expect = [ 70, 28 ]

    text = wt.open_page(link)

    assert wt.count_occs(text, words) == expect

def test_occs_macbeth4():
    '''
    Test count occs in the Scottish play
    '''
    link = "http://www.gutenberg.org/cache/epub/2264/pg2264.txt"

    words = [ "Macb.", "Macd.", "Lady." ]
    expect = [ 137, 58, 41 ]

    text = wt.open_page(link)

    assert wt.count_occs(text, words) == expect
