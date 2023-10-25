import sys
import urllib.request as request
import urllib.error
from bs4 import BeautifulSoup as bs


def print_spreads(spreads):
    """
    Prints game dates, favorites, underdogs, and spread in a table.

    Parameters:
        spreads (tuple): A tuple of spreads to be printed
    """

    print("\nNFL Point Spreads\n")
    # Print header border
    print("+-{:<14}-+-{:<30}-+-{:<30}-+-{:>6}-+".format("-" * 14, "-" * 30, "-" * 30, "-" * 6))
    # Print the header
    print("| {:<14} | {:<30} | {:<30} | {:>6} |".format(
        'Game Date', 'Favorite', 'Underdog', 'Spread'))

    # Print the spreads
    for spread in spreads:
        # Print the cell separators
        print("|-{:<14}-+-{:<30}-+-{:<30}-+-{:>6}-|".format("-" * 14, "-" * 30, "-" * 30, "-" * 6))
        # Print the spread details
        print("| {:<14} | {:<30} | {:<30} | {:>6} |".format(
            spread[0], spread[1], spread[3], spread[2]))

    # Print footer border
    print("+-{:<14}-+-{:<30}-+-{:<30}-+-{:>6}-+".format("-" * 14, "-" * 30, "-" * 30, "-" * 6))


def get_html(url):
    """Accepts a URL as a string and opens it.

    Parameters:
        url (string): the url to be opened
    """

    response = request.urlopen(url).read()
    html = bs(response, 'lxml')

    return html


def get_spreads(html):
    """Accepts a BeautifulSoup object and parses it.

    Parameters:
        html (BeautifulSoup): the content to be parsed
    """

    # Get the tables containing the spreads in the HTML
    tables = html.find_all('table',
                           attrs={
                               'cols': '4',
                               'width': '580',
                               'border': '0',
                               'cellspacing': '6',
                               'cellpadding': '3'
                           }
                           )

    # Get the rows from each table and merge into one-dimensional list
    rows = [row for rows in [table.select('tr') for table in tables] for row in rows]

    # Get the spread cells from the rows
    spreads = ((cell[0].text, cell[1].text.replace("\n", " "), cell[2].text, cell[3].text.replace("\n", " ")) for cell
               in [row.select('td:not([width])') for row in rows if row.select('td:not([width])')])

    # Return the spreads
    return spreads


def main():
    """The method that runs when the program is executed."""

    # Set the URL
    url = 'http://www.footballlocks.com/nfl_point_spreads.shtml'
    # Get the HTML
    html = get_html(url)
    # Parse the spreads from the HTML
    spreads = get_spreads(html)
    # Print the spreads
    print_spreads(spreads)

    # Exit the program after the spreads are printed
    sys.exit()


if __name__ == '__main__':
    main()