from watchgod import run_process
import os


def run_server():
    os.system('clear')
    import subprocess
    subprocess.run(["python3", "main.py"])


if __name__ == '__main__':
    run_process(".", run_server)
