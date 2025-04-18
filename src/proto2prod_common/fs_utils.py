import os

def list_files(directory: str) -> list:
    """Return a list of file paths in the given directory."""
    files = []
    for root, _, filenames in os.walk(directory):
        for fname in filenames:
            files.append(os.path.join(root, fname))
    return files


def read_file(path: str) -> str:
    """Read and return the contents of a file."""
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()
