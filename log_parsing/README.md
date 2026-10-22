# Log Parsing

A Python script that reads lines from standard input, parses server log entries, and prints a summary of HTTP status codes and total file size.

## Log Format

Each input line must follow this format:

```text
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
```

Lines that do not match the expected format are ignored.

## Usage

```bash
./0-stats.py
```

Enter log entries through standard input. Statistics are printed after every 10 valid lines and when the program receives a keyboard interrupt.

## Output

The script prints the total file size and status code counts in ascending order:

```text
File size: <total>
200: <count>
301: <count>
400: <count>
401: <count>
403: <count>
404: <count>
405: <count>
500: <count>
```
