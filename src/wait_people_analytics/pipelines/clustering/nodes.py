from typing import Any

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.cluster.hierarchy as sch


def generate_hierarchical_clustering_visual(df: pd.DataFrame) -> Any:
    clustering = sch.linkage(df, method="ward")
    plt.figure(figsize=(10, 4))
    sch.dendrogram(clustering, labels=df.index)
    plt.xticks(rotation=90)
    plt.title("Dendrogram")
    plt.xlabel("UserId")
    plt.ylabel("Distance")
    return plt
