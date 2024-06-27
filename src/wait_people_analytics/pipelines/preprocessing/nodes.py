from typing import Any

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def change_participation_detail_to_df(survey: pd.DataFrame) -> pd.DataFrame:
    """Decouple 'Participation Type' into 3 different categories:
    Participant, Organizer, Consumer

    Mapping:
    Chcę uczestniczyć w projekcie data - Participant
    Chcę uczestniczyć w projekcie data i organizować "życie" Community - Participant and Organizer
    Póki co chcę czerpać, obserwować, "konsumować content - Consumer

    Args:
        survey: raw dataframe.
    Returns:
        dataframe with changed columns
    """
    participation_column_name = "Participation Type"
    survey.insert(1, "Participant", "")
    survey.insert(1, "Organizer", "")
    survey.insert(1, "Consumer", "")
    survey["Participant"] = np.where(
        (
            survey[participation_column_name]
            == "Chcę uczestniczyć w projekcie data"
        )
        |
        (
            survey[participation_column_name]
            == 'Chcę uczestniczyć w projekcie data i organizować "życie" Community'
        ),
        1,
        0,
    )
    survey["Organizer"] = np.where(
        (
            survey[participation_column_name] == 'Chcę organizować "życie" Community'
        )
        |
        (
            survey[participation_column_name]
            == 'Chcę uczestniczyć w projekcie data i organizować "życie" Community'
        ),
        1,
        0,
    )
    survey["Consumer"] = np.where(
        survey[participation_column_name]
        == 'Póki co chcę czerpać, obserwować, "konsumować content"',
        1,
        0,
    )
    survey = survey.drop(
        columns=[participation_column_name]
    )
    return survey


def drop_columns(survey: pd.DataFrame) -> pd.DataFrame:
    """Drop columns with no value for model

    Args:
        survey: dataframe.
    Returns:
        dataframe without specific columns
    """
    survey = survey.drop(
        columns=[
            "Survey start time",
            "Survey end time",
            "Email",
            "Name",
            "Survey last modify time",
            "Your idea",
            "Interests",
            "Additional Tech",
            "FinTech",
            "HealthTech",
            "FashionTech",
            "ECommerce",
            "SportTech",
            "NonProfit",
            "PropTech",
            "Cybersecurity",
        ]
    )
    return survey


def filter_project_participants(df: pd.DataFrame) -> list[pd.DataFrame]:
    """
    Filters the DataFrame to include only project participants.

    Args:
        df: dataframe.
    Returns:
        dataframe containing only project participants.
    """
    combined_df = df[(df["Participant"] == 1) | (df["Organizer"] == 1)].copy()
    combined_df.drop(columns=["Participant", "Organizer", "Consumer"], inplace=True)
    organizers_df = df[df["Organizer"] == 1].copy()
    organizers_df.drop(columns=["Participant", "Organizer", "Consumer"], inplace=True)
    participants_df = df[df["Participant"] == 1].copy()
    participants_df.drop(columns=["Participant", "Organizer", "Consumer"], inplace=True)
    return [combined_df, organizers_df, participants_df]


def swap_zero_with_one(df: pd.DataFrame) -> pd.DataFrame:
    ids = df["ID"]
    df = df.drop(columns="ID")
    replaced = df.replace({0: 1, 1: 0})
    replaced.insert(0, "ID", "")
    replaced["ID"] = ids
    return replaced
