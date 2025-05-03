# !/bin/bash

problem_name=$1
contest_name=${problem_name%%_*}
test_dir=test/${problem_name}
base_url=${contest_name}

echo "Problem Name: ${problem_name}"
echo "Contest Name: ${contest_name}"
echo "Test Directory: ${test_dir}"
echo "Base URL: ${base_url}"

if [ ! -e ${test_dir} ]; then
    echo "Creating test directory: ${test_dir}"
    oj dl -d ${test_dir} https://atcoder.jp/contests/${base_url}/tasks/${problem_name//-/_}
else
    echo "Test directory already exists: ${test_dir}"
fi

echo "Running test command: oj test -c 'python3 problems/${contest_name}/${problem_name}.py' -d ${test_dir}"
oj test -c "python3 problems/${contest_name}/${problem_name}.py" -d ${test_dir}