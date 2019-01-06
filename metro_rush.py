#!/usr/bin/env python3
from Graph import Graph


def main():
    a = Graph()
    a.excute_data('delhi-metro-stations')
    a.parse_map()
    result = a.bfs()
    [print([x.station_name, x.line_name]) for x in result]

if __name__ == '__main__':
    main()
