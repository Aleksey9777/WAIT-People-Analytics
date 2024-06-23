from typing import Any

import pandas as pd
import matplotlib.pyplot as plt


def generate_overall_stackedbar_visual(
    df: pd.DataFrame,
    analytics_legend_mapping: dict[int, str],
) -> Any:
    df = _get_skill_count(df, analytics_legend_mapping)
    df = df.sort_values(by=4, ascending=False)
    return _get_bar_plot(df, analytics_legend_mapping, "Count of People with Each Skill Value")


def generate_top_interested_stackedbar_visual(
    df: pd.DataFrame,
    analytics_legend_mapping: dict[int, str],
) -> Any:
    df = _get_skill_count(df, analytics_legend_mapping)
    df = df.sort_values(by=2, ascending=False)
    return _get_bar_plot(df, analytics_legend_mapping, "Top by Count of Interested")


def generate_top_not_interested_stackedbar_visual(
    df: pd.DataFrame,
    analytics_legend_mapping: dict[int, str],
) -> Any:
    df = _get_skill_count(df, analytics_legend_mapping)
    df = df.sort_values(by=1, ascending=False)
    return _get_bar_plot(df, analytics_legend_mapping, "Top by Count of Not Interested")


def generate_top_unconscious_stackedbar_visual(
    df: pd.DataFrame,
    analytics_legend_mapping: dict[int, str],
) -> Any:
    df = _get_skill_count(df, analytics_legend_mapping)
    df = df.sort_values(by=0, ascending=False)
    return _get_bar_plot(df, analytics_legend_mapping, "Top by Count of Unconscious")


def _get_skill_count(df: pd.DataFrame, mapping: dict[int, str]) -> pd.DataFrame:
    skill_values = list(mapping.keys())
    skill_counts = {value: [] for value in skill_values}

    for col in df.columns[1:]:
        for value in skill_values:
            count = (df[col] == value).sum()
            skill_counts[value].append(count)

    return pd.DataFrame(skill_counts, index=df.columns[1:])


def _get_bar_plot(df: pd.DataFrame, mapping: dict[int: str], plot_title: str) -> Any:
    skill_values = list(mapping.keys())

    count_df = df.head(8)
    plt.figure(figsize=(10, 6))
    ax = count_df.plot(kind="bar", stacked=True, figsize=(10, 6))
    plt.title(plot_title)
    plt.xlabel("Skill")
    plt.ylabel("Count")
    plt.xticks(rotation=90)

    handles, labels = ax.get_legend_handles_labels()
    sort_order = sorted(range(len(skill_values)), reverse=True)

    sorted_handles = [handles[idx] for idx in sort_order]
    sorted_labels = [mapping[idx] for idx in sort_order]

    ax.legend(sorted_handles, sorted_labels, title="Skill Value", bbox_to_anchor=(1.05, 1), loc="upper left")
    return plt
