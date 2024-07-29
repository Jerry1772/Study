import argparse
import os
import shutil
import pickle

import mlflow
import mlflow.runs
import numpy as np

def main():
   
    EXPERIMENT_ID = os.environ["MLFLOW_EXPERIMENT_ID"]
    # RUN_ID = os.environ["MLFLOW_RUN_ID"]

    parser = argparse.ArgumentParser(
        description="preprocessing module",
        formatter_class=argparse.RawTextHelpFormatter
    )
#region arguments
    parser.add_argument(
        "--data",
        type=str,
        default="mnist",
        help="dataset name"
    )
    # parser.add_argument(
    #     "--output_path",
    #     type=str,
    #     default="/opt/data/_preprocess/",
    #     help="output path"
    # )
    
    parser.add_argument(
        "--cached_data_id",
        type=str,
        default="",
        help="cached id"
    )
    args = parser.parse_args()

#endregion

#region data path
    
    if args.cached_data_id:
        run_directories = set(os.listdir(f"/opt/mlruns/{EXPERIMENT_ID}"))
        if args.cached_data_id in run_directories:
            mlflow.log_artifacts(
                f"/opt/mlruns/{EXPERIMENT_ID}/{args.cached_data_id}/artifacts/preprocessed_data",
                artifact_path="preprocessed_data"
            )
            return
        else:
            raise ValueError("no matched directory found!")

    # output_path = args.output_path
    output_path = "/tmp/preprocess/"

    original_data_path = os.path.join(
        "/opt/preprocess/data",
        args.data
    )
    train_data_path = os.path.join(
        output_path,
        "train"
    )
    test_data_path = os.path.join(
        output_path,
        "test"
    )

    # os.makedirs(output_path, exist_ok=True)
    os.makedirs(train_data_path, exist_ok=True)
    os.makedirs(test_data_path, exist_ok=True)
#endregion

#region preprocessing
    with open(f'{original_data_path}/train_x.pickle', 'rb') as f:
        train_x:np.ndarray = pickle.load(f)
    with open(f'{original_data_path}/train_y.pickle', 'rb') as f:
        train_y:np.ndarray = pickle.load(f)
    with open(f'{original_data_path}/test_x.pickle', 'rb') as f:
        test_x:np.ndarray = pickle.load(f)
    with open(f'{original_data_path}/test_y.pickle', 'rb') as f:
        test_y:np.ndarray = pickle.load(f)

    train_x = train_x/255.
    test_x = test_x/255.

    with open(f'{train_data_path}/x.pickle', 'wb') as f:
        pickle.dump(train_x, f)
    with open(f'{train_data_path}/y.pickle', 'wb') as f:
        pickle.dump(train_y, f)
    with open(f'{test_data_path}/x.pickle', 'wb') as f:
        pickle.dump(test_x, f)
    with open(f'{test_data_path}/y.pickle', 'wb') as f:
        pickle.dump(test_y, f)

#endregion
    # 현재는 mount 된 volume에 artifact logging 기능을 통해 데이터를 떨구고 있음.
    # 저장된 데이터를 추후에 사용하기 위해서는 mlflow 모니터링 툴을 통해 run id를 복사해가야 함.
    # 이 방식은 좀 불편하니, rdb에 run name등을 저장해서 다양한 메타데이터를 통해
    # 데이터 위치를 불러오는 방식을 고려할 필요가 있음.
    
    mlflow.log_artifacts(
        output_path,
        artifact_path="preprocessed_data"
    )
    shutil.rmtree(output_path)

if __name__ == "__main__":

    main()