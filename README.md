# IS450-Assignment7 — Trail Weather Log

- **Student name:** Olivia Leigh
- **GitHub username:** meolivialeigh

## Description

`myProgram.py` generates five days of simulated weather readings for three
hiking trails, saves them to a text file, reads them back in, and reports the
condition of each trail day by day along with a summary for each trail. A day is
Closed when rainfall reaches 0.75 in, Caution when the high is 85F or above or
55F or below, and Open otherwise.

## Input

The program takes no keyboard input. Trail names and the number of days are set
as variables in `main()`, and each day's high temperature and rainfall are
generated randomly, so the readings differ on every run. The program reads its
own data file, `trail_log.txt`, back in after writing it, and builds the report
from the saved file.

## Output

Printed to the screen:

- A daily conditions table — one line per trail per day, showing the high
  temperature, the rainfall, and the status.
- A summary for each trail: average high, warmest day, total rainfall, and the
  number of days the trail was open.

Written to disk:

- `trail_log.txt`, one comma-separated reading per line as `trail,day,high,rain`.

## How to run

Python 3.9 or later is required.

```
python myProgram.py
```

From Visual Studio Code, open the project folder, open `myProgram.py`, and press
the Run button.

## Feature Development Comparison

I added two features to this program, one on each branch.

On manual-feature I wrote a CSV export manually. It takes the season summary the program already builds and writes it to trail_conditions.csv. I reused the csv.DictWriter pattern from my Assignment 6 program and formatted each row so the file matches what prints on screen.

On ai-feature I defined a season condition breakdown and had Claude implement it. It counts every reading as Open, Caution, or Closed and prints the split with percentages. I chose the feature and wrote the spec; the AI wrote the functions and wired them into main().

The AI version ran correctly the first time, and I didn't reject any of it. Two things did change during testing. I had planned to check that the percentages add up to 100, and they didn't... each one rounds on its own, so they land anywhere from 99.9 to 100.1. The test was the issue moreso than the code. The other change was a guard so an empty list of readings doesn't crash the division.

The AI feature gives me greater confidence because this language isn't something I'm using on a regular basis like SQL, so having more robust testing and the ability to ask questions as I go is helpful.