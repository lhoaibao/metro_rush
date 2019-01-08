#!/usr/bin/env python3
from Graph import Graph


def main():
    a = Graph()
    a.excute_data('delhi-metro-stations')
    a.parse_map()
    # for item in a.map:
    #     if item.line_name == 'Red Line':
    #         print(item, a.map[item])
    a.run_trains()


if __name__ == '__main__':
    main()
