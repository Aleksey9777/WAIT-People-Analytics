from kedro.pipeline import Pipeline, node, pipeline

from .nodes import (
    generate_missing_value_heatmap,
    rename_columns,
    change_participation_detail_to_df,
    drop_columns,
)


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
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
            node(
                func=change_participation_detail_to_df,
                inputs="renamed_raw_survey",
                outputs="changed_participation_detail",
                name="add_participation_detail_to_df",
            ),
            node(
                func=drop_columns,
                inputs="changed_participation_detail",
                outputs="processed_survey",
                name="drop_columns",
            ),
        ]
    )
