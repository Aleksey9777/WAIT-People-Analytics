from typing import Any

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def filter_project_participants(df: pd.DataFrame) -> Any:
    df = df[df["Participant"] == 1]
    df = df.drop(columns = ["Participant", "Organizer", "Consumer"])
    return df

def generate_corr_matrix_visual(df: pd.DataFrame) -> Any:
    df = df.copy()
    df = df.drop(columns = ["ID"])
    numeric_df = df.select_dtypes(include=[np.number])
    corr_matrix = numeric_df.corr(method='spearman')

    plt.figure(figsize=(17, 14))
    mask = np.triu(np.ones_like(corr_matrix, dtype=bool))

    sns.heatmap(
        corr_matrix,
        mask=mask,
        annot=corr_matrix,
        fmt="0.2f",
        cmap="coolwarm",
        vmin=-1,
        vmax=1,
        center=0,
    )
    return plt
