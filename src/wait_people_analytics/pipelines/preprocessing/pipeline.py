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
        outputs={"processed_survey_combined", "processed_survey_organizers", "processed_survey_participants"},
        pipe=[
            node(
                func=swap_zero_with_one,
                inputs="renamed_raw_survey",
                outputs="rescaled_survey",
                name="swap_zero_with_one",
            ),
            node(
                func=change_participation_detail_to_df,
                inputs="rescaled_survey",
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
                outputs=["processed_survey_combined", "processed_survey_organizers", "processed_survey_participants"],
                name="filter_project_participants",
            ),
        ]
    )
