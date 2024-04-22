import os
from load_dataset import LoadDataset
from load_model import LoadModel
from process_logs import store_logs
import uuid

run_id = "run_id"
global_model_name = "model_name"

def train_model(user_id, repo_name, run_id, model_file_id, data_file_id):
    # copy the dataset directory
    print("[In train_model] ")
    LoadDataset(user_id, repo_name, run_id, data_file_id)
    LoadModel(user_id, repo_name, run_id, model_file_id)

    print("Dataset and model loaded")

    # # check if there is a run.py file in the model directory
    if not os.path.exists(f"repos/{repo_name}/model/train.py"):
        print("Error: No train.py file in the model directory")
        return "Error: No train.py file in the model directory"
    

    os.makedirs(f"results/{run_id}", exist_ok=True)
    results_path = f'results/{run_id}/results.txt'
    
    print("Running model")
    # # run the model and store the results in a file
    os.system(f"python repos/{repo_name}/model/train.py > {results_path}")
    print("Model run complete")

    results = ""
    # return the results as a string
    with open(results_path, "r") as file:
        results = file.read()

    print("Results: ", results)

    # TODO 
    # store_logs(user_id, repo_name, run_id, results_path)

    return results