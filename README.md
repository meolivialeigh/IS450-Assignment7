# IS450-Assignment7 — Trail Weather Log

**Student name:** Olivia Leigh
**GitHub username:** meolivialeigh
**Course:** BAN 701 — Assignment 7

## Description

`myProgram.py` is a trail weather reporting program. It generates five days of
simulated weather readings for three hiking trails, saves those readings to a
text file, reads them back in from that file, and reports the condition of each
trail day by day along with a summary for each trail.

Each day is classified using the trail's high temperature and rainfall:

| Status | Condition |
| --- | --- |
| Closed | rainfall of 0.75 in or more |
| Caution | high of 85F or above, or 55F or below |
| Open | anything else |

## Input

The program takes no keyboard input. The trail names and the number of days are
set as variables at the top of `main()`, and the daily high temperature and
rainfall are generated randomly, so the readings differ on every run.

The program also reads its own data file, `trail_log.txt`, back in after writing
it, so the report is produced from the saved file rather than from the values
held in memory.

## Output

Printed to the screen:

- A confirmation that the readings were written to `trail_log.txt`, and a count
  of the readings read back in.
- A daily conditions table — one line per trail per day, showing the high
  temperature, the rainfall, and the status.
- A season summary for each trail: average high, warmest day, total rainfall,
  and the number of days the trail was open.

Written to disk:

- `trail_log.txt`, one comma-separated reading per line in the form
  `trail,day,high,rain`.

Sample output:

```
TRAIL WEATHER LOG
==========================================
Generating 5 days of readings for 3 trails.

Readings written to trail_log.txt

Readings read back from file: 15

DAILY TRAIL CONDITIONS
------------------------------------------
Day 1 | Redwood Loop | High: 65F | Rain: 0.12in | Open
Day 2 | Redwood Loop | High: 71F | Rain: 0.81in | Closed
Day 3 | Redwood Loop | High: 52F | Rain: 0.28in | Caution
...

SEASON SUMMARY
------------------------------------------
Trail: Redwood Loop
  Average High: 71.8F
  Warmest Day: 87F
  Total Rainfall: 2.18in
  Days Open: 3 of 5
```

## How to run

Python 3.9 or later is required.

```
python myProgram.py
```

From Visual Studio Code, open the project folder, open `myProgram.py`, and press
the Run button, or run the command above in the integrated terminal.

## Concepts demonstrated

- **Variables** — trail names, day count, and the log file name.
- **Functions** — seven functions, each with type hints and a single job.
- **Lists** — the readings list, and list comprehensions that pull the highs and
  rainfall for one trail.
- **Dictionaries** — each reading and each trail summary is a dictionary.
- **Loops** — nested loops to generate readings, and loops over the readings to
  report and summarize them.
- **Conditionals** — `classify_day()` decides Closed, Caution, or Open.
- **Random values** — `random.randint()` and `random.uniform()` generate the
  daily weather.
- **File input/output** — the readings are written to `trail_log.txt` and read
  back in before any reporting is done.
