# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians
# Assume a year has 365.25 days
import re
import datetime

DATE = re.compile(r"\d{2} \w{3} \w{4}")
TIME = re.compile(r"\d+:\d+(\.\d+)?")


def get_data():
    with open("10k_racetimes.txt", "rt") as file:
        content = file.read()
    return content


def get_event_time(line):
    """Given a line with Jennifer Rhines' race times from 10k_racetimes.txt,
    parse it and return a tuple of (age at event, race time).
    Assume a year has 365.25 days"""
    time = TIME.search(line).group()
    race_date, birth_date = [
        datetime.datetime.strptime(date, "%d %b %Y") for date in DATE.findall(line)
    ]
    diff = race_date - birth_date
    years = int(diff.days // 365.25)
    days = int(diff.days - years * 365.25)
    return f"{years}y{days}d", time


def get_age_slowest_times():
    """Return a tuple (age, race_time) where:
    age: AyBd is in this format where A and B are integers"""
    races = get_data()
    rhines_races = [
        get_event_time(race) for race in races.splitlines() if "Jennifer Rhines" in race
    ]
    print(rhines_races)
    return max(
        rhines_races,
        key=lambda r: [
            int(a.split(".")[0]) if "." in a else int(a) for a in r[1].split(":")
        ],
    )


get_age_slowest_times()
