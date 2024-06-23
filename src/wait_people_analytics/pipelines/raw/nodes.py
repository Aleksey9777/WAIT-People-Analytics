from typing import Any

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


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


def generate_missing_value_heatmap(df: pd.DataFrame) -> Any:
    """Generate missing value heatmap

    Args:
        df: dataframe.
    Returns:
        Matplotlib plit
    """
    plt.figure(figsize=(18, 13))
    sns.heatmap(df.isnull(), cbar=False, cmap="YlGnBu")
    plt.title("Heatmap of Missing Values")
    return plt
