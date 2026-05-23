@echo off
echo ==========================================
echo   Energy Analysis - Auto Setup
echo ==========================================

echo.
echo [1/3] Creating virtual environment...
python -m venv venv

echo.
echo [2/3] Upgrading pip...
call venv\Scripts\python.exe -m pip install --upgrade pip --quiet

echo.
echo [3/3] Installing pandas, numpy, scikit-learn, etc...
call venv\Scripts\python.exe -m pip install pandas numpy matplotlib seaborn scikit-learn jupyter

echo.
echo ==========================================
echo   SETUP COMPLETE! OPENING NOTEBOOK...
echo ==========================================
echo.

call venv\Scripts\activate.bat
jupyter notebook Energy_Analysis.ipynb

pause