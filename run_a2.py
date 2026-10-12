"""
Reproduce every result of the assignment with one command:

    python run_a2.py --scale medium --seed <ID4>

The script executes ibaidullina.ipynb top-to-bottom (like "Run All") and passes
scale and seed through environment variables. All tables (CSV) and figures (PNG)
are written to results/, and the executed notebook is saved as
results/executed_<scale>.ipynb.
"""
import argparse
import os
import subprocess
import sys

NOTEBOOK = "ibaidullina.ipynb"


def main():
    ap = argparse.ArgumentParser(description="ShopStream A2: reproduce all results")
    ap.add_argument("--scale", default="medium", choices=["tiny", "small", "medium", "large"])
    ap.add_argument("--seed", type=int, required=True, help="last 4 digits of the student ID")
    a = ap.parse_args()

    os.makedirs("results", exist_ok=True)
    env = dict(os.environ, A2_SCALE=a.scale, A2_SEED=str(a.seed))

    cmd = [
        sys.executable, "-m", "jupyter", "nbconvert",
        "--to", "notebook", "--execute", NOTEBOOK,
        "--output-dir", "results", "--output", f"executed_{a.scale}",
        "--ExecutePreprocessor.timeout=-1",          # no time limit
        "--ExecutePreprocessor.kernel_name=python3",  # kernel of the active environment
    ]
    print("Running:", " ".join(cmd))
    subprocess.run(cmd, env=env, check=True)
    print("Done. See results/")


if __name__ == "__main__":
    main()
