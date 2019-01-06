from Station import Station
from collections import deque


class Graph:
    def __init__(self):
        self.map = {}
        self.map_data = {}
        self.require_data = {}

    def __load_data(self, file_name):
        try:
            with open(file_name, 'r') as f:
                f_content = f.read().split('\n\n')
                f_content[0] += '\n'
            return f_content
        except Exception:
            return None

    def __excute_map_data(self, map_data):
        result = {}
        map_data = map_data.split('#')[1:]
        for item in map_data:
            item = item.split('\n')[:-1]
            res = []
            for i in range(1, len(item)):
                data = item[i].split(':')
                if 'Conn' in item[i]:
                    res.append(Station(item[0], data[0], data[1], data[3].strip()))
                else:
                    res.append(Station(item[0], data[0], data[1]))
            result[item[0]] = res
        return result

    def __excute_require_data(self, require_data):
        result = {}
        require_data = require_data.split('\n')[:-1]
        map_data = self.map_data
        for i in range(len(require_data)):
            require_data[i] = require_data[i].split(':')
        result['START'] = map_data[require_data[0][0][6:]][int(require_data[0][1])-1]
        result['END'] = map_data[require_data[1][0][4:]][int(require_data[1][1])]
        result['TRAINS'] = int(require_data[2][0][7:])
        return result

    def excute_data(self, file_name):
        (map_data, require_data) = self.__load_data(file_name)
        self.map_data = self.__excute_map_data(map_data)
        self.require_data = self.__excute_require_data(require_data)

    def get_egde(self, stations, index):
        result = []
        if index == 0:
            result.append(stations[index+1])
        elif index == len(stations) - 1:
            result.append(stations[index-1])
        else:
            result.append(stations[index+1])
            result.append(stations[index-1])
        check = stations[index].conn
        if check:
            list = self.map_data[check]
            for i in range(1, len(list)-1):
                if list[i].station_name == stations[index].station_name:
                    result.append(list[i-1])
                    result.append(list[i+1])
        return result

    def parse_map(self):
        result= {}
        map_data = self.map_data
        list_line = map_data.keys()
        for item in list_line:
            ls = map_data[item]
            for i in range(len(ls)):
                result[ls[i]] = self.get_egde(ls, i)
        self.map = result

    def bfs(self):
        start = self.require_data['START']
        end = self.require_data['END']
        graph = self.map
        if start.compare(end):
            return [start]
        visited = {start}
        queue = deque([(start,[])])
        while queue:
            cur, path = queue.popleft()
            visited.add(cur)
            for neighbor in graph[cur]:
                if neighbor.compare(end):
                    return path + [cur, neighbor]
                if neighbor in visited:
                    continue
                queue.append((neighbor, path+[cur]))
                visited.add(neighbor)
