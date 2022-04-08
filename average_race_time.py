# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians

import re
import datetime


def get_data():
    """Return content from the 10k_racetimes.txt file"""
    with open("10k_racetimes.txt", "rt") as file:
        content = file.read()
    return content


def get_rhines_times():
    """Return a list of Jennifer Rhines' race times"""
    time_pattern = r"\d+:\d+(\.\d+)?"
    _, *races = get_data().split("\n")
    return [
        re.search(time_pattern, race).group()
        for race in races
        if "Jennifer Rhines" in race
    ]


def get_average():
    """Return Jennifer Rhines' average race time in the format:
    mm:ss:M where :
    m corresponds to a minutes digit
    s corresponds to a seconds digit
    M corresponds to a milliseconds digit (no rounding, just the single digit)"""
    sum_time = datetime.timedelta()
    rhines_times = get_rhines_times()
    for time in rhines_times:
        m, s, *ms = re.split(r"[\.:]+", time)

        sum_time += datetime.timedelta(
            minutes=int(m), seconds=int(s), milliseconds=int(ms[0]) if ms else 0
        )
    _, m, s, *ms = re.split(r"[\.:]+", str(sum_time / len(rhines_times)))

    return f"{m}:{s}.{ms[0][0] if ms else 0}"
