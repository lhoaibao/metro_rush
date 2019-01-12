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
    a.run_trains()

if __name__ == '__main__':
    main()
