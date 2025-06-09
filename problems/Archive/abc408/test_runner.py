import subprocess
import glob
import os
import sys

# 実行対象ファイルをカレントファイルから自動検出(abc_*.py)
def detect_target():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    dir_name = os.path.basename(current_dir)
    files = sorted(glob.glob(f"{dir_name}_*.py"))
    print(files)
    if not files:
        print("No target .py file found in this directory.")
        sys.exit(1)
    print("Select target file to test:")
    for idx, f in enumerate(files):
        print(f"{idx+1}: {f}")
    sel = input("Enter number (default 1): ")
    sel = int(sel) if sel.strip() else 1
    return files[sel-1]

# 入力ファイルのパス（上位ディレクトリを参照）
def find_input_files():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
    input_files = sorted(glob.glob(os.path.join(base_dir, "input*.txt")))

    valid_files = []
    for file_path in input_files:
        if os.path.getsize(file_path) > 0:
            valid_files.append(file_path)

    if not valid_files:
        print("No non-empty input*.txt files found.")
        sys.exit(1)
    return valid_files

def main():
    target_file = detect_target()
    input_files = find_input_files()

    print(f"実行するテストファイル数: {len(input_files)}")
    for input_file in input_files:
        print(f"\n=== Testing with {os.path.basename(input_file)} ===")
        with open(input_file, "r") as f:
            content = f.read()
            if not content.strip():
                print(f"スキップ: {os.path.basename(input_file)} は空のファイルです")
                continue

            proc = subprocess.run(
                ["python3", target_file],
                input=content,
                text=True,
                capture_output=True
            )
        print("Output:")
        print(proc.stdout)
        if proc.stderr:
            print("Errors:")
            print(proc.stderr, file=sys.stderr)

if __name__ == "__main__":
    main()