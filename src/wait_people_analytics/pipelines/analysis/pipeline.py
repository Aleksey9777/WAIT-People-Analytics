from kedro.pipeline import Pipeline, node, pipeline

from .nodes import (
    generate_corr_matrix_visual,
)


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=generate_corr_matrix_visual,
                inputs="processed_survey_combined",
                outputs="corr_matrix_visual_combined",
                name="generate_corr_matrix_visual_combined",
            ),
            node(
                func=generate_corr_matrix_visual,
                inputs="processed_survey_organizers",
                outputs="corr_matrix_visual_organizers",
                name="generate_corr_matrix_visual_organizers",
            ),
            node(
                func=generate_corr_matrix_visual,
                inputs="processed_survey_participants",
                outputs="corr_matrix_visual_participants",
                name="generate_corr_matrix_visual_participants",
            ),
        ]
    )
