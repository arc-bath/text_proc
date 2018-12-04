import web_text as wt

def test_licence():
    link = "https://people.bath.ac.uk/rjg20/index.html"
    filename = "../data/rjg20-index.html"

    with open(filename) as file:
        expect = file.read().splitlines()

    link_str = wt.open_page(link)
    link_lines = link_str.splitlines()
