from typing import Any

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def _add_participation_detail_to_df(survey: pd.DataFrame) -> pd.DataFrame:
    survey.insert(1, "Participant", "")
    survey.insert(1, "Organizer", "")
    survey.insert(1, "Consumer", "")
    survey["Participant"] = np.where(
        (
            survey["W jaki sposób chcesz uczestniczyć w Community?"]
            == "Chcę uczestniczyć w projekcie data"
        )
        |
        (
            survey["W jaki sposób chcesz uczestniczyć w Community?"]
            == 'Chcę uczestniczyć w projekcie data i organizować "życie" Community'
        ),
        1,
        0,
    )
    survey["Organizer"] = np.where(
        (
            survey["W jaki sposób chcesz uczestniczyć w Community?"]
            == 'Chcę organizować "życie" Community'
        )
        |
        (
            survey["W jaki sposób chcesz uczestniczyć w Community?"]
            == 'Chcę uczestniczyć w projekcie data i organizować "życie" Community'
        ),
        1,
        0,
    )
    survey["Consumer"] = np.where(
        survey["W jaki sposób chcesz uczestniczyć w Community?"]
        == 'Póki co chcę czerpać, obserwować, "konsumować content"',
        1,
        0,
    )
    survey = survey.drop(
        columns=["W jaki sposób chcesz uczestniczyć w Community?"]
    )
    return survey


def _rename_columns(survey: pd.DataFrame) -> pd.DataFrame:
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
            "Jeżeli jest obszar, na którym się znasz i chcesz go wykorzystać, dopisz go:": "Dodatkowy obszar",
            "FinTech": "FinTech",
            "HealthTech": "HealthTech",
            "FashionTech": "FashionTech",
            "E-commerce": "ECommerce",
            "SportTech": "SportTech",
            "Non-profit": "NonProfit",
            "PropTech (nieruchomości)": "PropTech",
            "Cybersecurity": "Cybersecurity",
            "HR": "HR",
            "Jeżeli pominięto branżę, na której się znasz dopisz ją:": "Dodatkowe Branży",
        }
    )
    return survey


def _drop_columns(survey: pd.DataFrame) -> pd.DataFrame:
    survey = survey.drop(
        columns=[
            "Twój pomysł",
            "Zainteresowania",
            "Dodatkowe Branży",
            "Godzina rozpoczęcia",
            "Godzina ukończenia",
            "Adres e-mail",
            "Nazwa",
            "Czas ostatniej modyfikacji",
        ]
    )
    return survey


def preprocess_survey(survey: pd.DataFrame) -> pd.DataFrame:
    survey = _add_participation_detail_to_df(survey)
    survey = _rename_columns(survey)
    # survey = _drop_columns(survey)
    return survey


def generate_missing_value_heatmap(df: pd.DataFrame) -> Any:
    plt.figure(figsize=(10, 4))
    sns.heatmap(df.isnull(), cbar=False, cmap="YlGnBu")
    plt.title("Heatmap of Missing Values")
    return plt
