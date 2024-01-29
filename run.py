import multiprocessing
import os
import subprocess
import sys


def run(args):
    seed, skeleton = args

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

    subprocess.run(program_command, env=my_env)


if __name__ == "__main__":
    # Define the range of seeds
    seeds = range(8)
    skeletons = [False, True]
    arg_combinations = [(seed, skeleton) for seed in seeds for skeleton in skeletons]

    # Create a multiprocessing pool with the number of desired processes
    # You can adjust the number of processes based on your system's capabilities
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        # Use the pool.map function to distribute the seeds among the processes
        pool.map(run, arg_combinations)
