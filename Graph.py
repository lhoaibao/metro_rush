from Line import Line
from Train import Train


class Graph:
    def __init__(self):
        """
        4 attribue:
            map: dictionary store with from name_line:
        """
        self.map = {}
        self.start = []
        self.end = []
        self.total_train = 0
        self.list_info_train = {}



    def load_graph(self, file_name):
        """
        input: file_name
        excute content of file into small part by obj
        -   require of user
        -   a map to run
        """
        with open(file_name) as f:
            file_content = f.read().split('\n\n')
        self.__excute_line_require(file_content[1])
        self.__excute_data_map(file_content[0])

    def __excute_line_require(self, data):
        """
        get 3 line end and analysis the require info
        -   start station
        -   end station
        -   total train
        """
        data = data.split('\n')
        start = data[0].split(':')
        self.start = [start[0][6:], int(start[1])]
        end = data[1].split(':')
        self.end = [end[0][4:], int(end[1])]
        self.total_train = int(data[2][7:])

    def __excute_data_map(self, data):
        """
        get content of file except the last 3 line to analysis
        the map
        """
        data += '\n'
        data = data.split('#')
        data.pop(0)
        for item in data:
            obj = Line()
            item = obj.excute_line(item)
            self.map[obj.name] = obj

    def set_train(self):
        num = self.total_train
        start = self.start
        list_temp = {}
        for i in range(num):
            id = 'T'+str(i+1)
            list_temp[id] = Train()

    def __store_data(self):
        pass
