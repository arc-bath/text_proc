import web_text as wt

def test_rjg20():
    link = "https://people.bath.ac.uk/rjg20/index.html"
    filename = "../data/rjg20-index.html"

    with open(filename) as file:
        expect = file.read().splitlines()

    link_str = wt.open_page(link)
    link_lines = link_str.splitlines()

    assert link_lines == expect
