from kedro.pipeline import Pipeline, node, pipeline

from .nodes import (
    generate_corr_matrix_visual,
    filter_project_participants
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
            )
        ]
    )
