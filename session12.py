import csv
from collections import namedtuple, defaultdict
from datetime import datetime

# Defineng namedTuples based on given csv headers
Ticket = namedtuple("Ticket", ["summons_number", "plate_id", "registration_state", 
                               "plate_type", "issue_date", "violation_code", 
                               "vehicle_body_type", "vehicle_make", "violation_description"])

# Lazy iterator function
def lazy_ticket_reader(file_path):
    with open(file_path, "r", encoding="latin-1") as f:
        reader = csv.reader(f)
        headers = next(reader)  # Skips the header row

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

# Count violations by car make lazily
def count_violations_by_make(file_path):
    violation_counts = defaultdict(int)
    for ticket in lazy_ticket_reader(file_path):
        violation_counts[ticket.vehicle_make] += 1
    return dict(violation_counts)


if __name__ == "__main__":
    file_path = "/Users/rishitladdha/Desktop/EPAI/S12/nyc_parking_tickets_extract-1.csv"  
    violations_by_make = count_violations_by_make(file_path)
    print(violations_by_make)
    