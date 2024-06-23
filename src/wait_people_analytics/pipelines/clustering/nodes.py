from typing import Any

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.cluster.hierarchy as sch


def generate_hierarchical_clustering_visual(df: pd.DataFrame) -> Any:
    filtered_df = df.drop(columns= "ID")
    filtered_df = filtered_df.replace( {0: 1, 1:0})
    clustering = sch.linkage(filtered_df, method="ward")
    plt.figure(figsize=(10, 4))
    sch.dendrogram(clustering)
    plt.xticks(rotation=90)
    plt.title("Dendrogram")
    plt.xlabel("UserId")
    plt.ylabel("Distance")
    return plt
