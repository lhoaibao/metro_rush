#!/usr/bin/env python3
import sys
from AlgoBFS import AlgoBFS


def main():
    a = AlgoBFS()
    try:
        a.excute_data(sys.argv[1])
    except Exception:
        print('Invalid file')
        return None
    if len(sys.argv) == 3:
        if sys.argv[2] == 'one_path':
            a.run_trains(sys.argv[2])
        else:
            print('wrong mode')
    elif len(sys.argv) == 2:
        a.run_trains()
    else:
        print('wrong argument')

if __name__ == '__main__':
    main()
