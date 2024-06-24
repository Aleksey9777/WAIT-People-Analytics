from kedro.pipeline import Pipeline, node, pipeline

from .nodes import (
    generate_overall_stackedbar_visual,
    generate_top_interested_stackedbar_visual,
    generate_top_not_interested_stackedbar_visual,
    generate_top_unconscious_stackedbar_visual
)


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        namespace="data_insights",
        inputs={"processed_survey"},
        parameters={"analytics_legend_mapping"},
        outputs={
            "overall_stackedbar_visual",
            "top_interested_stackedbar_visual",
            "top_not_interested_stackedbar_visual",
            "top_unconscious_stackedbar_visual",
        },
        pipe=[
            node(
                func=generate_overall_stackedbar_visual,
                inputs=["processed_survey", "params:analytics_legend_mapping"],
                outputs="overall_stackedbar_visual",
                name="generate_overall_stackedbar_visual",
            ),
            node(
                func=generate_top_interested_stackedbar_visual,
                inputs=["processed_survey", "params:analytics_legend_mapping"],
                outputs="top_interested_stackedbar_visual",
                name="generate_top_interested_stackedbar_visual",
            ),
            node(
                func=generate_top_not_interested_stackedbar_visual,
                inputs=["processed_survey", "params:analytics_legend_mapping"],
                outputs="top_not_interested_stackedbar_visual",
                name="generate_top_not_interested_stackedbar_visual",
            ),
            node(
                func=generate_top_unconscious_stackedbar_visual,
                inputs=["processed_survey", "params:analytics_legend_mapping"],
                outputs="top_unconscious_stackedbar_visual",
                name="generate_top_unconscious_stackedbar_visual",
            )
        ]
    )
