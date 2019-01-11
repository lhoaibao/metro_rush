from Graph import Graph
from Train import Train
from collections import deque


class AlgoBFS(Graph):
    def __init__(self):
        self.map = {}

    def __get_egde(self, stations, index):
        """
        get the connet station from this station to a list
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

    def __parse_map(self):
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
        self.__parse_map()
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
            self.print_status_run(path)
