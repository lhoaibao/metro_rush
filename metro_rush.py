#!/usr/bin/env python3
from Graph import Graph


def main():
    A = Graph()
    a = A.load_graph('delhi-metro-stations')
    print(A.map['Yellow Line'].get_info())


if __name__ == '__main__':
    main()
