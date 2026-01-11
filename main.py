"""
Elections Scraper 2017
Scrapes election results for a selected district.
"""

import csv
import sys
from typing import Dict, List, Tuple
import requests
from bs4 import BeautifulSoup


def get_soup(url: str) -> BeautifulSoup:
    """Downloads page content and returns BeautifulSoup object."""
    response = requests.get(url)
    response.raise_for_status()
    return BeautifulSoup(response.text, "html.parser")


def get_municipalities(url: str) -> List[Tuple[str, str, str]]:
    """
    Returns list of municipalities:
    (code, name, detail_url)
    """
    soup = get_soup(url)
    rows = soup.find_all("tr")[2:]
    municipalities = []

    for row in rows:
        cells = row.find_all("td")
        if len(cells) >= 2:
            code = cells[0].text.strip()
            name = cells[1].text.strip()
            link = cells[0].find("a")
            if link:
                detail_url = "https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ" + link["href"]
                municipalities.append((code, name, detail_url))

    return municipalities


def get_results(detail_url: str) -> Tuple[Dict[str, int], Dict[str, int]]:
    """
    Returns:
    - summary data
    - party results
    """
    soup = get_soup(detail_url)

    summary = {}
    tables = soup.find_all("table")

    summary_cells = tables[0].find_all("td")
    summary["registered"] = int(summary_cells[3].text.replace("\xa0", ""))
    summary["envelopes"] = int(summary_cells[4].text.replace("\xa0", ""))
    summary["valid"] = int(summary_cells[7].text.replace("\xa0", ""))

    parties = {}
    for table in tables[1:3]:
        for row in table.find_all("tr")[2:]:
            cells = row.find_all("td")
            if len(cells) >= 3:
                party = cells[1].text.strip()
                votes = int(cells[2].text.replace("\xa0", ""))
                parties[party] = votes

    return summary, parties


def save_csv(
    filename: str,
    municipalities: List[Tuple[str, str, str]]
) -> None:
    """Saves scraped data into CSV file."""
    all_data = []
    party_names = set()

    for code, name, url in municipalities:
        summary, parties = get_results(url)
        party_names.update(parties.keys())
        all_data.append((code, name, summary, parties))

    header = [
        "code", "location", "registered", "envelopes", "valid"
    ] + sorted(party_names)

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(header)

        for code, name, summary, parties in all_data:
            row = [
                code,
                name,
                summary["registered"],
                summary["envelopes"],
                summary["valid"],
            ]
            for party in sorted(party_names):
                row.append(parties.get(party, 0))
            writer.writerow(row)


def main() -> None:
    """Main program entry point."""
    if len(sys.argv) != 3:
        print("Použití: python main.py <URL> <vystup.csv>")
        sys.exit(1)

    url, filename = sys.argv[1], sys.argv[2]

    try:
        municipalities = get_municipalities(url)
        save_csv(filename, municipalities)
        print(f"Data byla uložena do souboru {filename}")
    except Exception as error:
        print(f"Chyba: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
