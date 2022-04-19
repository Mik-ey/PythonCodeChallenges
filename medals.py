from collections import namedtuple
import pandas as pd


olympics = pd.read_csv("olympics.txt", sep=";")
olympics = olympics.astype(str)

medal = namedtuple(
    "medal",
    [
        "City",
        "Edition",
        "Sport",
        "Discipline",
        "Athlete",
        "NOC",
        "Gender",
        "Event",
        "Event_gender",
        "Medal",
    ],
)


def get_medals(**kwargs):
    """Return a list of medal namedtuples"""
    pass
