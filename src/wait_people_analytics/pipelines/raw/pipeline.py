from kedro.pipeline import Pipeline, node, pipeline

from .nodes import (
    generate_missing_value_heatmap,
    rename_columns,
)


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        namespace="raw_analysis",
        inputs={"raw_survey"},
        outputs={"renamed_raw_survey", "missing_value_heatmap_plot"},
        pipe=[
            node(
                func=rename_columns,
                inputs="raw_survey",
                outputs="renamed_raw_survey",
                name="rename_columns",
            ),
            node(
                func=generate_missing_value_heatmap,
                inputs="renamed_raw_survey",
                outputs="missing_value_heatmap_plot",
                name="generate_missing_value_heatmap",
            ),
        ]
    )
