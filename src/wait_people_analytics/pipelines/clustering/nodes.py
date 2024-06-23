from typing import Any

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.cluster.hierarchy as sch


def generate_hierarchical_clustering_visual(df: pd.DataFrame) -> Any:
    df_without_id = df.drop(columns= "ID")
    clustering = sch.linkage(df_without_id, method="ward")
    plt.figure(figsize=(10, 4))
    sch.dendrogram(clustering)
    plt.xticks(rotation=90)
    plt.title("Dendrogram")
    plt.xlabel("UserId")
    plt.ylabel("Distance")
    return plt
