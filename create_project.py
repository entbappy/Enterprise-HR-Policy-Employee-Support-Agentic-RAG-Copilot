from pathlib import Path

root = Path(".")

# All folders list

folders = [
    "app/api",
    "app/core",
    "app/rag",
    "app/services",
    "data",
    "templates",
    "static",
    "uploads",
    "tests",
]


# All files list

# Files to create
files = [
    "app/main.py",
    "ingest_sample_kb.py",
    "requirements.txt",
    "run.py",
    ".env",
]


# Create folders
for folder in folders:
    (root / folder).mkdir(parents=True, exist_ok=True)


# Create files
for file in files:
    (root / file).touch(exist_ok=True)


print("Project structure created successfully.")
