from kedro.pipeline import Pipeline, node, pipeline

from .nodes import (
    generate_overall_stacked_bar_visual,
    generate_top_interested_stacked_bar_visual,
    generate_top_not_interested_stacked_bar_visual,
    generate_top_unaware_stacked_bar_visual
)


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        namespace="data_insights",
        inputs={"processed_survey_combined"},
        parameters={"analytics_legend_mapping"},
        outputs={
            "overall_stacked_bar_visual",
            "top_interested_stacked_bar_visual",
            "top_not_interested_stacked_bar_visual",
            "top_unaware_stacked_bar_visual",
        },
        pipe=[
            node(
                func=generate_overall_stacked_bar_visual,
                inputs=["processed_survey_combined", "params:analytics_legend_mapping"],
                outputs="overall_stacked_bar_visual",
                name="generate_overall_stacked_bar_visual",
            ),
            node(
                func=generate_top_interested_stacked_bar_visual,
                inputs=["processed_survey_combined", "params:analytics_legend_mapping"],
                outputs="top_interested_stacked_bar_visual",
                name="generate_top_interested_stacked_bar_visual",
            ),
            node(
                func=generate_top_not_interested_stacked_bar_visual,
                inputs=["processed_survey_combined", "params:analytics_legend_mapping"],
                outputs="top_not_interested_stacked_bar_visual",
                name="generate_top_not_interested_stacked_bar_visual",
            ),
            node(
                func=generate_top_unaware_stacked_bar_visual,
                inputs=["processed_survey_combined", "params:analytics_legend_mapping"],
                outputs="top_unaware_stacked_bar_visual",
                name="generate_top_unaware_stacked_bar_visual",
            )
        ]
    )
