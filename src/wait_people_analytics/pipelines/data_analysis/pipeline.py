from kedro.pipeline import Pipeline, node, pipeline

from .nodes import (
    generate_corr_matrix_visual
)


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=generate_corr_matrix_visual,
                inputs="processed_survey",
                outputs="corr_matrix_visual",
                name="generate_corr_matrix_visual",
            )
        ]
    )
