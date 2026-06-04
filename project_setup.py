from pathlib import Path

folders = [
    "data/raw",
    "data/cleaned",
    "data/feature_store",
    "data/graph_data",

    "notebooks",

    "src",

    "models",

    "reports/figures",
    "reports/final",

    "dashboard",

    "presentations"
]

for folder in folders:
    Path(folder).mkdir(parents=True, exist_ok=True)

print("Project Structure Created")