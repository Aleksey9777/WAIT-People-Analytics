from kedro.pipeline import Pipeline, node, pipeline

from .nodes import (
    change_participation_detail_to_df,
    drop_columns,
    filter_project_participants,
)


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        namespace="data_preprocessing",
        inputs={"renamed_raw_survey"},
        outputs={"processed_survey"},
        pipe=[
            node(
                func=change_participation_detail_to_df,
                inputs="renamed_raw_survey",
                outputs="changed_participation_detail",
                name="add_participation_detail_to_df",
            ),
            node(
                func=drop_columns,
                inputs="changed_participation_detail",
                outputs="numeric_df",
                name="drop_columns",
            ),
            node(
                func=filter_project_participants,
                inputs="numeric_df",
                outputs="processed_survey",
                name="filter_project_participants",
            ),
        ]
    )
