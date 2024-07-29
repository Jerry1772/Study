import argparse
from importlib.abc import TraversableResources
import os
from turtle import back

import mlflow

def main():
    parser = argparse.ArgumentParser(
        description="Entry Point",
        formatter_class=argparse.RawTextHelpFormatter
    )
#region arguments
## preprocess arguments
    parser.add_argument(
        "--preprocess_data",
        type=str,
        default="mnist",
        help="dataset name"
    )
    # parser.add_argument(
    #     "--preprocess_output_path",
    #     type=str,
    #     default="/opt/data/preprocess/",
    #     help="dataset output path after preprocessing"
    # )
    parser.add_argument(
        "--preprocess_cached_data_id",
        type=str,
        default="",
        help="dataset cache id"
    )

## train arguments
    parser.add_argument(
        "--train_output_path",
        type=str,
        default="/opt/data/train/",
        help="model path after training"
    )
    parser.add_argument(
        "--train_tensorboard",
        type=str,
        default="/opt/data/tensorboard/",
        help="tensorboard path"
    )
    parser.add_argument(
        "--train_epochs",
        type=int,
        default=1,
        help="train epochs"
    )
    parser.add_argument(
        "--train_batch_size",
        type=str,
        default=32,
        help="train batch size"
    )
    parser.add_argument(
        "--train_learning_rate",
        type=float,
        default=0.001,
        help="train learning rate"
    )
    parser.add_argument(
        "--train_model_name",
        type=str,
        default="dense",
        help="model class name"
    )

## building arguments
    parser.add_argument(
        "--building_dockerfile_path",
        type=str,
        default="./Dockerfile",
        help="docker file path"
    )
    parser.add_argument(
        "--building_model_filename",
        type=str,
        default="dense_0.onnx",
        help="model filel name"
    )
    parser.add_argument(
        "--building_entrypoint_path",
        type=str,
        default="./onnx_runtime_server_entrypoint.sh",
        help="building process entry point"
    )

## evaluate arguments
    parser.add_argument(
        "--evaluate_output_path",
        type=str,
        default="./evaluate/",
        help="evaluate output path"
    )
#endregion

    args = parser.parse_args()
    mlflow_experiment_id = int(os.getenv("MLFLOW_EXPERIMENT_ID", 0))

    mlflow.set_tracking_uri("http://172.17.0.1:5000")
    with mlflow.start_run(run_name="test_run_preprocess") as run:
        preprocess_run = mlflow.run(
            uri="./preprocess",
            entry_point="preprocess",
            backend="local",
            parameters={
                "data": args.preprocess_data,
                "cached_data_id": args.preprocess_cached_data_id
            }
        )
        preprocess_run = mlflow.tracking.MlflowClient().get_run(preprocess_run.run_id)

if __name__ == "__main__":
    main()