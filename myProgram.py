# Name: Olivia Leigh
# Description: Assignment 7 - Trail Weather Log

import random

LOG_FILE = "trail_log.txt"


def generate_readings(trails: list[str], days: int) -> list[dict]:
    readings = []
    for trail in trails:
        for day in range(1, days + 1):
            reading = {
                "trail": trail,
                "day": day,
                "high": random.randint(48, 92),
                "rain": round(random.uniform(0.0, 1.0), 2)
            }
            readings.append(reading)
    return readings


def write_log(readings: list[dict], filename: str) -> None:
    log = open(filename, "w")
    for reading in readings:
        log.write(reading["trail"] + "," + str(reading["day"]) + ","
                  + str(reading["high"]) + "," + str(reading["rain"]) + "\n")
    log.close()


def read_log(filename: str) -> list[dict]:
    readings = []
    log = open(filename, "r")
    for line in log:
        parts = line.strip().split(",")
        if len(parts) == 4:
            readings.append({
                "trail": parts[0],
                "day": int(parts[1]),
                "high": int(parts[2]),
                "rain": float(parts[3])
            })
    log.close()
    return readings


def classify_day(high: int, rain: float) -> str:
    if rain >= 0.75:
        return "Closed"
    elif high >= 85 or high <= 55:
        return "Caution"
    else:
        return "Open"


def summarize_trail(readings: list[dict], trail: str) -> dict:
    highs = [r["high"] for r in readings if r["trail"] == trail]
    rainfall = [r["rain"] for r in readings if r["trail"] == trail]

    open_days = 0
    for reading in readings:
        if reading["trail"] == trail:
            if classify_day(reading["high"], reading["rain"]) == "Open":
                open_days = open_days + 1

    return {
        "trail": trail,
        "average_high": sum(highs) / len(highs),
        "warmest": max(highs),
        "total_rain": sum(rainfall),
        "open_days": open_days,
        "recorded_days": len(highs)
    }


def print_daily_report(readings: list[dict]) -> None:
    print("DAILY TRAIL CONDITIONS")
    print("------------------------------------------")
    for reading in readings:
        status = classify_day(reading["high"], reading["rain"])
        print("Day", reading["day"], "|", reading["trail"],
              "| High:", str(reading["high"]) + "F",
              "| Rain:", format(reading["rain"], ".2f") + "in",
              "|", status)
    print()


def print_summary(summary: dict) -> None:
    print("Trail:", summary["trail"])
    print("  Average High:", format(summary["average_high"], ".1f") + "F")
    print("  Warmest Day:", str(summary["warmest"]) + "F")
    print("  Total Rainfall:", format(summary["total_rain"], ".2f") + "in")
    print("  Days Open:", summary["open_days"], "of", summary["recorded_days"])


def main() -> None:
    trails = ["Redwood Loop", "Eagle Ridge", "Desert Wash"]
    days = 5

    print("TRAIL WEATHER LOG")
    print("==========================================")
    print("Generating", days, "days of readings for", len(trails), "trails.")
    print()

    readings = generate_readings(trails, days)
    write_log(readings, LOG_FILE)
    print("Readings written to", LOG_FILE)
    print()

    saved_readings = read_log(LOG_FILE)
    print("Readings read back from file:", len(saved_readings))
    print()

    print_daily_report(saved_readings)

    print("SEASON SUMMARY")
    print("------------------------------------------")
    for trail in trails:
        summary = summarize_trail(saved_readings, trail)
        print_summary(summary)
        print()


if __name__ == "__main__":
    main()
