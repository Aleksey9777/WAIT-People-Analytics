from kedro.pipeline import Pipeline, node
from kedro.pipeline.modular_pipeline import pipeline

from .nodes import (
    generate_hierarchical_clustering_visual,
    generate_hierarchical_table,
    generate_k_means_sse_plot,
    generate_k_means_clusters,
    prepare_data_for_clustering,
    generate_heatmap,
)


def create_pipeline(**kwargs) -> Pipeline:
    hard_skill_grouping_pipeline = pipeline(
        pipe=_get_pipeline_template(),
        namespace="hard_skills_grouping",
        inputs={"processed_survey": "processed_survey_participants"},
    )
    soft_skill_grouping_pipeline = pipeline(
        pipe=_get_pipeline_template(),
        namespace="soft_skills_grouping",
        inputs={"processed_survey": "processed_survey_organizers"},
    )
    return hard_skill_grouping_pipeline + soft_skill_grouping_pipeline


def _get_pipeline_template() -> Pipeline:
    return pipeline(
        [
            node(
                func=prepare_data_for_clustering,
                inputs=[
                    "processed_survey",
                    "params:clustering_skill_scaling",
                    "params:selected_columns",
                ],
                outputs="scaled_skills_table",
            ),
            node(
                func=generate_hierarchical_clustering_visual,
                inputs=[
                    "scaled_skills_table",
                    "params:hierarchical_params",
                ],
                outputs="hierarchical_clustering_visual",
            ),
            node(
                func=generate_hierarchical_table,
                inputs=[
                    "scaled_skills_table",
                    "params:hierarchical_params",
                ],
                outputs="hierarchical_clustered_table",
            ),
            node(
                func=generate_heatmap,
                inputs=[
                    "hierarchical_clustered_table",
                    "params:clustering_skill_scaling",
                ],
                outputs="hierarchical_cluster_heatmap",
            ),
            node(
                func=generate_k_means_sse_plot,
                inputs=[
                    "scaled_skills_table",
                    "params:k_means_params",
                ],
                outputs="k_means_sse_plot",
            ),
            node(
                func=generate_k_means_clusters,
                inputs=[
                    "scaled_skills_table",
                    "params:k_means_params",
                ],
                outputs="k_means_clustered_table",
            ),
        ]
    )
