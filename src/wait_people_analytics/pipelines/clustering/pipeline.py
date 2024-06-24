from kedro.pipeline import Pipeline, node, pipeline

from .nodes import (
    generate_hierarchical_clustering_visual
)


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=generate_hierarchical_clustering_visual,
                inputs="processed_survey",
                outputs="hierarchical_clustering_visual",
                name="generate_hierarchical_clustering_visual",
            )
        ]
    )
