from huggingface_hub import snapshot_download
import os

repo_id = "Sp1786/multiclass-sentiment-analysis-dataset"
local_dir = os.path.join(os.getcwd(), "dataset")

print(f"Downloading {repo_id} to {local_dir}...")
snapshot_download(repo_id=repo_id, repo_type="dataset", local_dir=local_dir)
print(f"Download complete. Files are located in {local_dir}")
