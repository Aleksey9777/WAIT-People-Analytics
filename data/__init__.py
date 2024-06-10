from pathlib import Path

DATA_DIR = Path(__file__).parent


def get_path(dir_name, file_name: str) -> Path:
    return DATA_DIR / dir_name / file_name

def test():
    return 'dzila'
