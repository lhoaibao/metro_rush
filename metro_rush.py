#!/usr/bin/env python3
import sys
from AlgoBFS import AlgoBFS


def main():
    a = AlgoBFS()
    a.excute_data(sys.argv[1])
    a.run_trains()


if __name__ == '__main__':
    main()
    # try:
    #     main()
    # except Exception:
    #     print('sorry, program have some error')
