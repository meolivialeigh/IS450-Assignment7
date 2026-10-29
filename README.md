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
