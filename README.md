Link for the colab - https://colab.research.google.com/drive/1dB6yzquW_50xEO1zVtFzWQhsJtLXyIYn?usp=sharing 

# NYC Parking Ticket Data Analysis

## Overview

This program processes NYC parking ticket data stored in a CSV file and performs an analysis of violations based on vehicle make. Instead of loading the entire dataset at once, it uses a **lazy iterator** to read and process data efficiently. The CSV file is fetched from an online source using a URL.

## Key Functionalities

### 1. Lazy Iteration

Instead of reading the entire CSV into memory, the program processes one row at a time using a **generator function**. This ensures efficient memory usage, especially for large datasets, by avoiding unnecessary memory consumption and allowing processing of very large files without performance issues.

A **generator** in Python is a special type of function that returns an iterator and allows iteration over a sequence of data without storing it all in memory. This is achieved using the `yield` keyword. In this program, the `lazy_ticket_reader` function acts as a generator by yielding one row at a time as a `Ticket` named tuple.

#### Example from the Code:

- The `lazy_ticket_reader` function reads a CSV file from a URL.
- It processes each row one at a time instead of loading the whole file into memory.
- It uses `yield` to return each row as a `Ticket` named tuple.
- This ensures that even if the dataset is huge, only one row is held in memory at a time.

### 2. Data Storage Using Named Tuples

Each row of the CSV file is stored as a **namedtuple** called `Ticket`. This data structure improves readability and structured data access, making it easier to reference specific attributes. The named tuple contains fields such as:
- **Summons number**: A unique identifier for the ticket.
- **Plate ID**: The license plate of the vehicle.
- **Registration State**: The state where the vehicle is registered.
- **Issue Date**: The date when the violation occurred.
- **Vehicle Make**: The manufacturer of the vehicle.
- **Violation Description**: A brief description of the violation.

Using named tuples provides the benefits of both dictionaries and tuples—readability and immutability—while keeping memory usage low.

### 3. Error Handling

If a row contains **invalid data**, such as incorrect formatting or missing values, the program **skips the row** and prints an error message indicating the issue. This prevents the program from crashing due to corrupt or inconsistent data.

- If a value cannot be converted to the expected type (e.g., `int` for summons number or violation code), an exception is caught, and the row is skipped.
- This ensures that errors in data do not halt execution.

### 4. Counting Violations

The program iterates through the dataset and **counts the number of violations per vehicle make** using a dictionary. The dictionary structure allows for efficient aggregation of violation data. The results are then converted into a standard dictionary and returned as the final output.

- The `count_violations_by_make` function uses a `defaultdict(int)` to initialize counts at zero.
- Each ticket's vehicle make is used as a key, and the count is incremented.
- Finally, the `defaultdict` is converted into a normal dictionary for easy readability.

## Top 10 Vehicle Makes with Most Violations

Below are the top 10 vehicle makes with the highest number of parking violations, as extracted from the final output of `session12.py` when executed:

| Vehicle Make | Number of Violations |
|-------------|---------------------|
| TOYOT       | 112                 |
| HONDA       | 106                 |
| FORD        | 104                 |
| CHEVR       | 76                  |
| NISSA       | 70                  |
| DODGE       | 45                  |
| FRUEH       | 44                  |
| ME/BE       | 38                  |
| GMC         | 35                  |
| HYUND       | 35                  |

## Execution Flow

1. The script starts by defining the CSV URL.
2. The `lazy_ticket_reader` function reads and processes each row lazily.
3. The `count_violations_by_make` function aggregates violations for each car make.
4. The final results are printed as a dictionary.

## Advantages of This Approach

- **Memory Efficiency**: Reads data one row at a time, reducing memory usage.
- **Improved Data Structure**: Using `namedtuple` makes accessing attributes intuitive.
- **Resilient to Errors**: Skips problematic rows without interrupting execution.
- **Web Compatibility**: Fetches data from a URL, making it accessible without local storage.

## Possible Enhancements

- Adding a function to filter violations by year.
- Storing results in a database for further analysis.
- Visualizing the data using graphs or charts.
- Allowing users to input a custom CSV file URL instead of a hardcoded one.

## Conclusion

This script provides a **lightweight, efficient, and scalable solution** for processing NYC parking ticket data. By leveraging lazy iteration, structured data storage, and robust error handling, it ensures smooth execution even for large datasets.

