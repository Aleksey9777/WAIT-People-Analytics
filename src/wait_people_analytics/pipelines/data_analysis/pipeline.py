from kedro.pipeline import Pipeline, node, pipeline

from .nodes import (
    filter_project_participants,
    generate_corr_matrix_visual,
    generate_overall_stackedbar_visual,
    generate_top_interested_stackedbar_visual,
    generate_top_not_interested_stackedbar_visual,
    generate_top_unconscious_stackedbar_visual
)


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=filter_project_participants,
                inputs="processed_survey",
                outputs="filter_project_participants_data",
                name="filter_project_participants",
            ),
            node(
                func=generate_corr_matrix_visual,
                inputs="filter_project_participants_data",
                outputs="corr_matrix_visual",
                name="generate_corr_matrix_visual",
            ),
            node(
                func=generate_overall_stackedbar_visual,
                inputs="filter_project_participants_data",
                outputs="overall_stackedbar_visual",
                name="generate_overall_stackedbar_visual",
            ),
            node(
                func=generate_top_interested_stackedbar_visual,
                inputs="filter_project_participants_data",
                outputs="top_interested_stackedbar_visual",
                name="generate_top_interested_stackedbar_visual",
            ),
            node(
                func=generate_top_not_interested_stackedbar_visual,
                inputs="filter_project_participants_data",
                outputs="top_not_interested_stackedbar_visual",
                name="generate_top_not_interested_stackedbar_visual",
            ),
            node(
                func=generate_top_unconscious_stackedbar_visual,
                inputs="filter_project_participants_data",
                outputs="top_unconscious_stackedbar_visual",
                name="generate_top_unconscious_stackedbar_visual",
            )
        ]
    )
