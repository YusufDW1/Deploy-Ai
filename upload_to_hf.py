from huggingface_hub import create_repo, upload_folder

repo_id = "YusufDW1/IndoBERT-Spam-Model"

# Buat repo jika belum ada
create_repo(repo_id, repo_type="model", exist_ok=True, private=False)

# Upload model
upload_folder(
    repo_id=repo_id,
    folder_path="indobert_spam_model",
    path_in_repo="model",
    repo_type="model"
)

# Upload tokenizer
upload_folder(
    repo_id=repo_id,
    folder_path="indobert_spam_tokenizer",
    path_in_repo="tokenizer",
    repo_type="model"
)
