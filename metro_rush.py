#!/usr/bin/env python3
from Graph import Graph


def main():
    a = Graph()
    a.excute_data('delhi-metro-stations')
    a.parse_map()
    a.bfs()

if __name__ == '__main__':
    main()
