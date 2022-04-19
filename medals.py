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

    if not set(kwargs.keys()).issubset(medal._fields):
        raise Exception("Invalid key word arguments")

    temp_df = olympics.copy()
    for k, v in kwargs.items():
        temp_df = temp_df[temp_df[k] == v]

    results = []
    for _, row in temp_df.iterrows():
        results.append(
            medal(
                City=row.City,
                Edition=row.Edition,
                Sport=row.Sport,
                Discipline=row.Discipline,
                Athlete=row.Athlete,
                NOC=row.NOC,
                Gender=row.Gender,
                Event=row.Event,
                Event_gender=row.Event_gender,
                Medal=row.Medal,
            )
        )

    return results
