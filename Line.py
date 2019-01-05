from Station import Station


class Line:
    def __init__(self):
        self.name = ''
        self.stations = []

    def excute_line(self, line):
        line = line.split('\n')
        line.pop(-1)
        self.name = line[0]
        list_station = []
        for i in range(1, len(line)):
            item = line[i].split(':')
            if 'conn' in  line[i]:
                list_station.append(Station(int(item[0]), item[1], item[3]))
            else:
                list_station.append(Station(int(item[0]), item[1]))
        self.stations = list_station

    def get_info(self):
        list = []
        for item in self.stations:
            list.append(str(item.id)+':'+item.name)
        return list
