"""
Воспроизводит всё задание одной командой:

    python run_a2.py --scale medium --seed <ID4>

Скрипт запускает ноутбук ibaidullina.ipynb сверху вниз (как "Run All")
и передаёт ему scale и seed через переменные окружения.
Все таблицы (CSV) и графики (PNG) появляются в папке results/,
а выполненная копия ноутбука сохраняется как results/executed_<scale>.ipynb.
"""
import argparse
import os
import subprocess
import sys

NOTEBOOK = "ibaidullina.ipynb"


def main():
    ap = argparse.ArgumentParser(description="ShopStream A2: reproduce all results")
    ap.add_argument("--scale", default="medium", choices=["tiny", "small", "medium", "large"])
    ap.add_argument("--seed", type=int, required=True, help="5820")
    a = ap.parse_args()

    os.makedirs("results", exist_ok=True)
    env = dict(os.environ, A2_SCALE=a.scale, A2_SEED=str(a.seed))

    cmd = [
        sys.executable, "-m", "jupyter", "nbconvert",
        "--to", "notebook", "--execute", NOTEBOOK,
        "--output-dir", "results", "--output", f"executed_{a.scale}",
        "--ExecutePreprocessor.timeout=-1",          # без ограничения по времени
        "--ExecutePreprocessor.kernel_name=python3",  # ядро из текущего .venv
    ]
    print("Running:", " ".join(cmd))
    subprocess.run(cmd, env=env, check=True)
    print("Done. See results/")


if __name__ == "__main__":
    main()
