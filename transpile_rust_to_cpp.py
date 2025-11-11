#!/usr/bin/env python3
import re, sys, os

def transpile(rust_code: str) -> str:
    cpp_code = []
    cpp_code.append('#include <iostream>')
    cpp_code.append('using namespace std;')
    cpp_code.append('')

    # Rust main 변환
    rust_code = rust_code.replace('fn main()', 'int main()')
    rust_code = re.sub(r'let\s+(\w+)\s*=\s*(.*?);', r'auto \1 = \2;', rust_code)
    rust_code = re.sub(r'println!\s*\("([^"]*)"\);', r'cout << "\1" << endl;', rust_code)

    cpp_code.append(rust_code)
    return "\n".join(cpp_code)

if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else "-"
    rust_src = open(src).read() if src != "-" else sys.stdin.read()
    cpp_out = transpile(rust_src)
    print(cpp_out)
