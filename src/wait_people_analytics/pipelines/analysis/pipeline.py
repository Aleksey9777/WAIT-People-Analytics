from kedro.pipeline import Pipeline, node, pipeline

from .nodes import (
    generate_corr_matrix_visual,
    generate_overall_stackedbar_visual,
    generate_top_interested_stackedbar_visual,
    generate_top_not_interested_stackedbar_visual,
    generate_top_unconscious_stackedbar_visual
)


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        namespace="data_analysis",
        inputs={"filter_project_participants_data"},
        parameters={"analytics_legend_mapping"},
        outputs={
            "corr_matrix_visual",
            "overall_stackedbar_visual",
            "top_interested_stackedbar_visual",
            "top_not_interested_stackedbar_visual",
            "top_unconscious_stackedbar_visual",
        },
        pipe=[
            node(
                func=generate_corr_matrix_visual,
                inputs="filter_project_participants_data",
                outputs="corr_matrix_visual",
                name="generate_corr_matrix_visual",
            ),
            node(
                func=generate_overall_stackedbar_visual,
                inputs=["filter_project_participants_data", "params:analytics_legend_mapping"],
                outputs="overall_stackedbar_visual",
                name="generate_overall_stackedbar_visual",
            ),
            node(
                func=generate_top_interested_stackedbar_visual,
                inputs=["filter_project_participants_data", "params:analytics_legend_mapping"],
                outputs="top_interested_stackedbar_visual",
                name="generate_top_interested_stackedbar_visual",
            ),
            node(
                func=generate_top_not_interested_stackedbar_visual,
                inputs=["filter_project_participants_data", "params:analytics_legend_mapping"],
                outputs="top_not_interested_stackedbar_visual",
                name="generate_top_not_interested_stackedbar_visual",
            ),
            node(
                func=generate_top_unconscious_stackedbar_visual,
                inputs=["filter_project_participants_data", "params:analytics_legend_mapping"],
                outputs="top_unconscious_stackedbar_visual",
                name="generate_top_unconscious_stackedbar_visual",
            )
        ]
    )
