from kedro.pipeline import Pipeline, node, pipeline

from .nodes import preprocess_survey, generate_missing_value_heatmap


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=preprocess_survey,
                inputs="raw_survey",
                outputs="processed_survey",
            ),
            node(
                func=generate_missing_value_heatmap,
                inputs="raw_survey",
                outputs="missing_value_heatmap_plot",
            ),
        ]
    )
