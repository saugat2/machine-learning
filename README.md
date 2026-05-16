# Energy Consumption Analysis

This project contains a Jupyter Notebook for analyzing an energy consumption dataset using Python. The notebook includes data loading, cleaning, preprocessing, visualization, and regression model training/evaluation.

## Files

- `Energy_Analysis.ipynb` - Main notebook containing the analysis.
- `energy_consumption_dataset.csv` - Dataset used by the notebook.

## Prerequisites

- Python 3.8 or newer
- A terminal or command prompt
- A virtual environment is recommended

## Recommended Python packages

The notebook uses the following Python libraries:

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `scikit-learn`
- `jupyter` (or `jupyterlab`)

## Install dependencies

Open PowerShell in the project folder and run:

```powershell
python -m venv venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

If you want JupyterLab instead of classic Jupyter Notebook, run:

```powershell
python -m pip install jupyterlab
```

## Run the notebook

Once dependencies are installed and the virtual environment is active, start the notebook server:

```powershell
jupyter notebook Energy_Analysis.ipynb
```

Or open `Energy_Analysis.ipynb` directly in VS Code.

## How to use

1. Make sure `Energy_Analysis.ipynb` and `energy_consumption_dataset.csv` are in the same folder.
2. Open the notebook in Jupyter or VS Code.
3. Run the cells from top to bottom.
4. Review the visualizations, model output, and evaluation metrics.

## Notes

- If the notebook cannot find the dataset, confirm the CSV file name and location.
- If you see any errors, verify that the required packages are installed in the active environment.
- You can also export the notebook results as HTML or PDF from Jupyter.

## Optional

To save the installed packages to a file:

```powershell
pip freeze > requirements.txt
```

This creates a `requirements.txt` file you can use to reinstall the same environment later.
