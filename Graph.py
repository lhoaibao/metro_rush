from Station import Station
from Train import Train
from collections import deque


class Graph:
    def __init__(self):
        """
        class has 3 attribute:
            map: value of this attribute depend on type of algo
            map_data: store data of map
            require_data: store data of require
        """
        self.map = {}
        self.map_data = {}
        self.require_data = {}

    def __load_data(self, file_name):
        """
        input: file_name
        output:
            -return content of file
            -return None if file not exist or can not open
        """
        try:
            with open(file_name, 'r') as f:
                f_content = f.read().split('\n\n')
                f_content[0] += '\n'
            return f_content
        except Exception:
            return None

    def __excute_map_data(self, map_data):
        """
        this function handling the data of map
        """
        result = {}
        map_data = map_data.split('#')[1:]
        for item in map_data:
            item = item.split('\n')[:-1]
            res = []
            for i in range(1, len(item)):
                data = item[i].split(':')
                if 'Conn' in item[i]:
                    res.append(Station(item[0], data[0], data[1],
                               data[3].strip()))
                else:
                    res.append(Station(item[0], data[0], data[1]))
            result[item[0]] = res
        return result

    def __excute_require_data(self, require_data):
        """
        this function hangling the data of require
        """
        result = {}
        r_data = require_data.split('\n')[:-1]
        m_data = self.map_data
        for i in range(len(r_data)):
            r_data[i] = r_data[i].split(':')
        result['START'] = m_data[r_data[0][0][6:]][int(r_data[0][1])-1]
        result['END'] = m_data[r_data[1][0][4:]][int(r_data[1][1])]
        result['TRAINS'] = int(r_data[2][0][7:])
        return result

    def excute_data(self, file_name):
        """
        this function is call first to excute all the data
        """
        (map_data, require_data) = self.__load_data(file_name)
        self.map_data = self.__excute_map_data(map_data)
        self.require_data = self.__excute_require_data(require_data)

    def __get_egde(self, stations, index):
        """
        """
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
            for i in range(len(list)):
                if list[i].station_name == stations[index].station_name:
                    result.append(list[i])
        return result

    def parse_map(self):
        """
        map is a dict store type {station:[station,...]}
        value is the egde of this station
        """
        result = {}
        map_data = self.map_data
        list_line = map_data.keys()
        for item in list_line:
            ls = map_data[item]
            for i in range(len(ls)):
                result[ls[i]] = self.__get_egde(ls, i)
        self.map = result

    def __bfs(self, start, end):
        """
        """
        graph = self.map
        if start.compare(end):
            return [start]
        visited = {start}
        queue = deque([(start, [])])
        while queue:
            cur, path = queue.popleft()
            visited.add(cur)
            for neighbor in graph[cur]:
                if neighbor.compare(end):
                    return path + [cur, neighbor]
                if neighbor not in visited:
                    queue.append((neighbor, path+[cur]))
                    visited.add(neighbor)

    def __print_status_run(self, path):
        result = []
        for item in path:
            if len(item.train) > 0:
                result.append('{}-{}'.format(str(item),
                                     ','.join([x.id for x in item.train])))
        print('|'.join(result))

    def run_trains(self):
        trains = []
        num_train = self.require_data['TRAINS']
        start = self.require_data['START']
        end = self.require_data['END']
        path = self.__bfs(start, end)
        for i in range(num_train):
            trains.append(Train('T'+str(i+1), start))
        start.train = trains.copy()
        turn = 0
        while len(end.train) != num_train:
            turn += 1
            print('turn {}:'.format(turn))
            for i in range(num_train):
                if i > 0 and trains[i].index < len(path)-2:
                    if trains[i-1].pos.station_name == path[trains[i].index+1].station_name:
                        break
                if trains[i].index < len(path)-1:
                    store = trains[i]
                    path[trains[i].index].train.remove(trains[i])
                    trains[i].index += 1
                    trains[i].pos = path[trains[i].index]
                    path[trains[i].index].train.append(store)
            self.__print_status_run(path)
