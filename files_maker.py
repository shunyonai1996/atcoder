import subprocess
import glob
import os
import sys

def main():
    contest_id = sys.argv[1]
    dir = f"./problems/abc{contest_id}"
    os.makedirs(dir)
    problems = ['a', 'b', 'c']
    for problem in problems:
        with open(f"{dir}/abc{contest_id}_{problem}.py", mode='w'):
            pass

if __name__ == "__main__":
    main()