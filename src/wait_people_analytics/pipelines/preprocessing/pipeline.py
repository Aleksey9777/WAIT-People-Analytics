from kedro.pipeline import Pipeline, node, pipeline

from .nodes import (
    change_participation_detail_to_df,
    drop_columns,
    filter_project_participants,
    swap_zero_with_one,
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
                outputs="filtered_survey",
                name="filter_project_participants",
            ),
            node(
                func=swap_zero_with_one,
                inputs="filtered_survey",
                outputs="processed_survey",
                name="swap_zero_with_one",
            ),
        ]
    )
