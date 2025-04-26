import { readFileSync } from 'fs';
import { join } from 'path';

const input = readFileSync(join(__dirname, '..//Users/shunyonai/Documents/GitHub/competitive-programming/input.txt'), 'utf8')
    .trim()
    .split('\n');

// 1行目を数値として取得
const N = +input[0];

// 2行目をスペース区切りの数値配列として取得
const [a, b] = input[1].split(' ').map(Number);

// 3行目を文字列として取得
const S = input[2];

console.log(N);
console.log(a, b);
console.log(S);