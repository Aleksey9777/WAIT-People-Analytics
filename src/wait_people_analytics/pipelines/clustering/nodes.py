from typing import Any

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering


def prepare_data_for_clustering(
    df: pd.DataFrame,
    clustering_skill_scaling: dict[int, int],
    selected_columns: list[str],
) -> pd.DataFrame:
    df = df[[*selected_columns]]
    ids = df["ID"]
    df = df.drop(columns="ID")
    replaced = df.replace(clustering_skill_scaling)
    replaced.insert(0, "ID", "")
    replaced["ID"] = ids
    return replaced


def generate_hierarchical_clustering_visual(
    df: pd.DataFrame,
    hierarchical_params: dict[str, Any],
) -> Any:
    df = df.drop(columns="ID")

    ac = AgglomerativeClustering(
        **{
            **hierarchical_params,
            "distance_threshold": 0,
            "n_clusters": None,
        }
    )
    model = ac.fit(df)

    counts = np.zeros(model.children_.shape[0])
    n_samples = len(model.labels_)
    for i, merge in enumerate(model.children_):
        current_count = 0
        for child_idx in merge:
            if child_idx < n_samples:
                current_count += 1  # leaf node
            else:
                current_count += counts[child_idx - n_samples]
        counts[i] = current_count

    linkage_matrix = np.column_stack(
        [model.children_, model.distances_, counts]
    ).astype(float)

    # Plot the corresponding dendrogram
    sch.dendrogram(linkage_matrix)

    # plt.figure(figsize=(10, 4))
    # plt.xticks(rotation=90)
    # plt.title("Dendrogram")
    # plt.xlabel("UserId")
    # plt.ylabel("Distance")
    return plt


def generate_hierarchical_table(
    df: pd.DataFrame,
    hierarchical_params: dict[str, Any],
) -> Any:
    df_copy = df.copy()
    df = df.drop(columns="ID")

    ac = AgglomerativeClustering(**hierarchical_params)
    clustering = ac.fit(df)

    df_copy.insert(1, "group", "")
    df_copy["group"] = clustering.labels_
    return df_copy


def generate_k_means_sse_plot(df: pd.DataFrame, k_means_params: dict[str, Any]) -> Any:
    df = df.drop(columns="ID")
    k = range(1, 20)
    tries = 10
    sum_squared_errors: list[float] = []

    for i in k:
        errors = []
        for t in range(tries):
            model = KMeans(
                **{
                    **k_means_params,
                    "n_clusters": i,
                    "max_iter": 300000,
                }
            )
            model.fit_predict(df)
            errors.append(model.inertia_)
        sum_squared_errors.append(sum(errors)/len(errors))

    plt.plot(k, sum_squared_errors)
    plt.xlabel('K-Value')
    plt.ylabel('Sum of Squared Errors')
    plt.tight_layout()
    return plt


def generate_k_means_clusters(df: pd.DataFrame, k_means_params: dict[str, Any]) -> Any:
    df_copy = df.copy()
    df = df.drop(columns="ID")

    model = KMeans(**k_means_params)
    model.fit_predict(df)

    df_copy.insert(1, "group", "")
    df_copy["group"] = model.labels_
    return df_copy


def generate_heatmap(
    df: pd.DataFrame,
    clustering_skill_scaling: dict[int, int],
) -> Any:
    """Generate heatmap

    Args:
        df: dataframe.
    Returns:
        Matplotlib plit
    """
    df.drop(columns=["ID"], inplace=True)
    reverse_clustering_skill_scaling = {
        value: key
        for key, value in clustering_skill_scaling.items()
    }
    df.replace(reverse_clustering_skill_scaling)
    df = df.sort_values(by="group", ascending=False)
    plt.figure(figsize=(18, 13))
    sns.heatmap(df, cbar=False, cmap="YlGnBu")
    plt.title("Heatmap")
    plt.tight_layout()
    return plt
