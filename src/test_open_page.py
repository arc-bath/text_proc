import web_test as wt

def test_licence():
    link = "https://creativecommons.org/licenses/by/4.0/legalcode.txt"
    filename = "../data/cc-by-4.0.txt"

    with open(filename) as file:
        expect = file.readlines()

    link_str = wt.open_page(link)
    link_lines = link_str.splitlines()

    
