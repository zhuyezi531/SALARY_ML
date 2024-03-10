import os
from absl import logging
from tfx.orchestration.kubeflow import kubeflow_dag_runner
from pipeline import create_pipeline

PIPELINE_NAME = 'salary_prediction'
PIPELINE_ROOT = 'gs://sunlit-charge-pipeline/metadata'
DATA_PATH = 'gs://sunlit-charge-pipeline/data'
SERVING_DIR = 'gs://sunlit-charge-pipeline/models'

def run():
    metadata_config = kubeflow_dag_runner.get_default_kubeflow_metadata_config()
    tfx_image = ''

    runner_config = kubeflow_dag_runner.KubeflowDagRunnerConfig(
        kubeflow_metadata_config=metadata_config, tfx_image=tfx_image
    )

    # Constructs a pipeline definition YAML file based on the TFX logical pipeline.
    kubeflow_dag_runner.KubeflowDagRunner(config=runner_config).run(
        create_pipeline(
            pipeline_name=PIPELINE_NAME,
            pipeline_root=PIPELINE_ROOT,
            serving_dir=SERVING_DIR,
            data_path=DATA_PATH
        )
    )