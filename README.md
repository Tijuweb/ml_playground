# ml_playground
## Setup

Install uv and Git, then run these commands from the repository root on Windows
or Linux:

```sh
uv sync
uv run pre-commit install
```

uv installs Python 3.12 if needed and creates `.venv` with the ML libraries and
development tools.

## Run

```sh
uv run python main.py
uv run python -m main
```

Both commands run the same small scikit-learn example using the built-in Iris
dataset, without downloading data. Replace it with your own experiments.

Black formats Python on save; Ruff checks code and sorts imports.

## Dependencies and notebooks

Included: NumPy, pandas, SciPy, scikit-learn, Matplotlib, Seaborn, JupyterLab,
and ipykernel. Add other libraries as needed:

```sh
uv add some-package
uv add --dev some-dev-tool
uv run jupyter lab
```

For VS Code notebooks, select `.venv` as the Python kernel. Large datasets and
experiment outputs can go in `data/` and `outputs/`, which Git ignores. These
folders are created only when you need them.

## Code quality

```sh
uv run ruff check .
uv run black --check .
uv run pre-commit run --all-files
```

Pre-commit runs Ruff (common Python errors, import sorting, bug risks, and Python
syntax modernization), Black, and checks for invalid JSON/YAML/TOML, merge
conflicts, large files, trailing whitespace, and missing final newlines.
Ruff and Black use the versions locked by uv. Hooks that fix files require you
to review and stage those changes before committing again. Git hooks need to be
installed once per clone; uv must be available on your PATH when committing.
