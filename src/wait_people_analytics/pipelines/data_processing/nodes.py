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


def rename_columns(survey: pd.DataFrame) -> pd.DataFrame:
    """Rename all columns in survey dataframe columns to shorter english equivalents.

    Args:
        survey: raw dataframe.
    Returns:
        dataframe with renamed columns
    """
    survey = survey.rename(
        columns={
            "Godzina rozpoczęcia": "Survey start time",
            "Godzina ukończenia": "Survey end time",
            "Adres e-mail": "Email",
            "Nazwa": "Name",
            "Czas ostatniej modyfikacji": "Survey last modify time",
            "Masz jakiś pomysł na projekt data? Napisz nam o tym. Jeżeli to nie ten moment, pozostaw puste pole.": "Your idea",
            "W jaki sposób chcesz uczestniczyć w Community?": "Participation Type",
            "Programming: R": "R",
            "Programming: Python": "Python",
            "Programming: Bash": "Bash",
            "Version Control: GIT": "GIT",
            "Containers: Docker": "Docker",
            "CLI: (np. Bash, PowerShell, CMD)": "CLI",
            "Front End: (HTML, JavaScript, CSS)": "Frontend",
            "Databases: SQL": "SQL",
            "Databases: NoSQL": "NoSQL",
            "Cloud: Azure": "Azure",
            "Cloud: AWS": "AWS",
            "Cloud: GPC": "GPC",
            "BI: PowerBI": "PowerBI",
            "BI: Tableau": "Tableau",
            "Area: Time Series": "Area: Time Series",
            "Area: Classical ML (Clustering, Regression, Classification)": "Area: Classical ML",
            "Area: NLP": "Area: NLP",
            "Area: Computer Vision": "Computer Vision",
            "Project Management": "Project Management",
            "Promocja w Social Media": "Prom. Social Media",
            "Ux/Ui": "UxUi",
            "Projektowanie graficzne": "Projekt. graf.",
            "Nawiązywanie Relacji z Biznesem": "Naw. Rel. z Biz.",
            "Nawiązywanie Relacji z naukowcami": "Naw. Rel. z nauk.",
            "Pozyskiwanie finansowania": "Pozysk. Finans.",
            "Współpraca z administracją UEW": "Wsp. z adm. UEW",
            "Jeżeli jest obszar, na którym się znasz i chcesz go wykorzystać, dopisz go:": "Interests",
            "FinTech": "FinTech",
            "HealthTech": "HealthTech",
            "FashionTech": "FashionTech",
            "E-commerce": "ECommerce",
            "SportTech": "SportTech",
            "Non-profit": "NonProfit",
            "PropTech (nieruchomości)": "PropTech",
            "Cybersecurity": "Cybersecurity",
            "HR": "HR",
            "Jeżeli pominięto branżę, na której się znasz dopisz ją:": "Additional Tech",
        }
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
        ]
    )
    return survey


def generate_missing_value_heatmap(df: pd.DataFrame) -> Any:
    """Generate missing value heatmap

    Args:
        df: dataframe.
    Returns:
        Matplotlib plit
    """
    plt.figure(figsize=(10, 4))
    sns.heatmap(df.isnull(), cbar=False, cmap="YlGnBu")
    plt.title("Heatmap of Missing Values")
    return plt
