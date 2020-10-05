from .utils import get_project_root  # pathlib is seriously awesome!

data_dir = get_project_root() / "data"
accidents_data_path = data_dir / "raw" / "collisions.csv"