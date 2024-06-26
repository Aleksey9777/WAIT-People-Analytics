from kedro.pipeline import Pipeline, node, pipeline

from .nodes import (
    generate_hierarchical_clustering_visual,
    generate_hierarchical_table,
    generate_k_means_sse_plot,
    generate_k_means_clusters,
    prepare_data_for_clustering,
    generate_heatmap,
)


def create_pipeline(**kwargs) -> Pipeline:
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
                name="prepare_data_for_clustering",
            ),
            node(
                func=generate_hierarchical_clustering_visual,
                inputs=[
                    "scaled_skills_table",
                    "params:hierarchical_params",
                ],
                outputs="hierarchical_clustering_visual",
                name="generate_hierarchical_clustering_visual",
            ),
            node(
                func=generate_hierarchical_table,
                inputs=[
                    "scaled_skills_table",
                    "params:hierarchical_params",
                ],
                outputs="hierarchical_clustered_table",
                name="generate_hierarchical_table",
            ),
            node(
                func=generate_heatmap,
                inputs=[
                    "hierarchical_clustered_table",
                    "params:clustering_skill_scaling",
                ],
                outputs="hierarchical_cluster_heatmap",
                name="generate_hierarchical_heatmap",
            ),
            node(
                func=generate_k_means_sse_plot,
                inputs=[
                    "scaled_skills_table",
                    "params:k_means_params",
                ],
                outputs="k_means_sse_plot",
                name="generate_k_means_sse_plot",
            ),
            node(
                func=generate_k_means_clusters,
                inputs=[
                    "scaled_skills_table",
                    "params:k_means_params",
                ],
                outputs="k_means_clustered_table",
                name="generate_k_means_clusters",
            ),
        ]
    )
