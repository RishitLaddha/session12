import csv
import requests
import io
from collections import namedtuple, defaultdict
from datetime import datetime

# Define NamedTuple
Ticket = namedtuple("Ticket", ["summons_number", "plate_id", "registration_state", 
                               "plate_type", "issue_date", "violation_code", 
                               "vehicle_body_type", "vehicle_make", "violation_description"])

# GitHub raw file link
CSV_URL = "https://raw.githubusercontent.com/RishitLaddha/session12/main/nyc_parking_tickets_extract-1.csv"

def lazy_ticket_reader(url):
    """Read CSV lazily from a URL."""
    response = requests.get(url)
    response.raise_for_status()  # Raise error if request fails
    file = io.StringIO(response.text)

    reader = csv.reader(file)
    headers = next(reader)  # Skip headers

    for row in reader:
        try:
            yield Ticket(
                summons_number=int(row[0]),
                plate_id=row[1],
                registration_state=row[2],
                plate_type=row[3],
                issue_date=datetime.strptime(row[4], "%m/%d/%Y").date(),
                violation_code=int(row[5]),
                vehicle_body_type=row[6],
                vehicle_make=row[7],
                violation_description=row[8],
            )
        except ValueError as e:
            print(f"Skipping row due to error: {e}")

def count_violations_by_make(url):
    """Count violations lazily from the CSV URL."""
    violation_counts = defaultdict(int)
    for ticket in lazy_ticket_reader(url):
        violation_counts[ticket.vehicle_make] += 1
    return dict(violation_counts)

if __name__ == "__main__":
    violations_by_make = count_violations_by_make(CSV_URL)
    print(violations_by_make)
