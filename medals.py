from collections import namedtuple
import pandas as pd


olympics = pd.read_csv("olympics.txt", sep=";")

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

medals = []  # Complete this - medals is a list of medal namedtuples


def get_medals(**kwargs):
    """Return a list of medal namedtuples"""
    pass
