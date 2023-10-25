import sys
import urllib.request as request
import urllib.error
from bs4 import BeautifulSoup as bs


def print_stats(stats):
    """
    Prints player names, positions, teams, and touchdowns in a table.

    Parameters:
        stats (tuple): A tuple of stats to be printed
    """

    print("\nNFL Top 20 Players' Stats\n")
    # Print header border
    print("+-{:<40}-+-{:<15}-+-{:<15}-+-{:>10}-+".format("-" * 40, "-" * 15, "-" * 15, "-" * 10))
    # Print the header
    print("| {:<40} | {:<15} | {:<15} | {:>10} |".format(
        'Player', 'Position', 'Team', 'Touchdowns'))

    # Print the players' stats
    for stat in stats:
        # Print the cell separators
        print("|-{:<40}-+-{:<15}-+-{:<15}-+-{:>10}-|".format("-" * 40, "-" * 15, "-" * 15, "-" * 10))
        # Print the player's stats
        print("| {:<40} | {:<15} | {:<15} | {:>10} |".format(
            stat[0], stat[1], stat[2], stat[3]))

    # Print footer border
    print("+-{:<40}-+-{:<15}-+-{:<15}-+-{:>10}-+".format("-" * 40, "-" * 15, "-" * 15, "-" * 10))


def get_html(url):
    """Accepts a URL as a string and opens it.

    Parameters:
        url (string): the url to be opened
    """

    response = request.urlopen(url).read()
    html = bs(response, 'lxml')

    return html


def get_top_20_stats(html):
    """Accepts a BeautifulSoup object and parses it.

    Parameters:
        html (BeautifulSoup): the content to be parsed
    """

    rows = html.select('tr.row1, tr.row2')

    stats = ((rows[i].contents[0].text, rows[i].contents[1].text, rows[i].contents[2].text, rows[i].contents[6].text)
             for i in range(0, 20))

    return stats


def main():
    """The method that runs when the program is executed."""

    # Set the URL
    url = 'https://www.cbssports.com/nfl/stats/playersort/nfl/year-2019-season-regular-category-touchdowns'

    # Get the HTML
    html = get_html(url)
    # Parse the top 20 players' stats from the HTML
    stats = get_top_20_stats(html)
    # Print the stats
    print_stats(stats)

    # Exit the program after the stats are printed
    sys.exit()


if __name__ == '__main__':
    main()