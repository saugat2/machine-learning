import os
import sys
import subprocess
import venv

def main():
    print("==========================================")
    print("  Energy Analysis - Environment Setup Tool")
    print("==========================================\n")

    venv_dir = "venv"
    
    # Step 1: Create the virtual environment
    print(f"[1/3] Creating virtual environment in '{venv_dir}' folder...")
    try:
        venv.create(venv_dir, with_pip=True)
    except Exception as e:
        print(f"Failed to create virtual environment: {e}")
        return
    
    # Determine the path to the pip executable inside the new venv
    if sys.platform == "win32":
        pip_executable = os.path.join(venv_dir, "Scripts", "pip.exe")
    else:
        pip_executable = os.path.join(venv_dir, "bin", "pip")
        
    if not os.path.exists(pip_executable):
        print(f"\nError: Could not find pip at {pip_executable}")
        return

    # List of required packages based on the Energy_Analysis project
    packages = [
        "pandas", 
        "numpy", 
        "matplotlib", 
        "seaborn", 
        "scikit-learn", 
        "jupyter"
    ]
    
    # Step 2: Upgrade pip to avoid warnings
    print("\n[2/3] Upgrading pip to the latest version...")
    subprocess.check_call([pip_executable, "install", "--upgrade", "pip", "--quiet"])
    
    # Step 3: Install all required packages
    print(f"\n[3/3] Installing required packages: {', '.join(packages)}...")
    subprocess.check_call([pip_executable, "install"] + packages)
    
    print("\n==========================================")
    print("             SETUP COMPLETE!              ")
    print("==========================================")
    
    # Generate OS-specific activation instructions
    if sys.platform == "win32":
        activate_cmd = f"{venv_dir}\\Scripts\\activate"
    else:
        activate_cmd = f"source {venv_dir}/bin/activate"
        
    print(f"\nTo start reviewing the analysis, please run the following commands in your terminal:")
    print(f"  1. {activate_cmd}")
    print(f"  2. jupyter notebook Energy_Analysis.ipynb\n")
    print("Press Enter to exit...")
    input()

if __name__ == "__main__":
    main()
