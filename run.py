import functools
import multiprocessing
import os
import subprocess
import sys


def run(seed, skeleton: bool = False):
    # Replace 'your_program.py' with the name of the Python program you want to run
    program_command = [
        'python',
        'cleanrl/dqn.py' if not skeleton else 'cleanrl/skeleton_dqn.py',
        '--seed',
        f'{seed}',
        '--env-id',
        sys.argv[1]
    ]

    my_env = os.environ.copy()
    my_env["CUDA_VISIBLE_DEVICES"] = "0" if not skeleton else "1"


    # Run the program using subprocess
    subprocess.run(program_command, env=my_env)


if __name__ == "__main__":
    # Define the range of seeds
    seeds = range(16)

    # Create a multiprocessing pool with the number of desired processes
    # You can adjust the number of processes based on your system's capabilities
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        # Use the pool.map function to distribute the seeds among the processes
        pool.map(functools.partial(run, skeleton=False), seeds)
        pool.map(functools.partial(run, skeleton=True), seeds)
