from Station import Station
import os


class Graph:
    def __init__(self):
        """
        class has 2 attribute:
            map_data: store data of map
            require_data: store data of require
        """
        self.map_data = {}
        self.require_data = {}

    def __check_input(self, file_name):
        """
        function check valid file_name
        """
        # check file exist
        if not os.access(file_name, os.F_OK):
            print('File not found')
            exit(1)
        # check permistion of file
        if not os.access(file_name, os.R_OK):
            print('Permistion denined')
            exit(1)

    def __load_data(self, file_name):
        """
        input: file_name
        output:
            -return content of file
        """
        self.__check_input(file_name)
        with open(file_name, 'r') as f:
            f_content = f.read()
        if len(f_content.split('\n\n')) != 2:
            print('Invalid file')
            exit(1)
        f_content = f_content.split('\n\n')
        f_content[0] += '\n'
        return f_content

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

    def print_status_run(self, path):
        result = []
        for item in path:
            if len(item.train) > 0:
                result.append('{}-{}'.format(str(item),
                                     ','.join([x.id for x in item.train])))
        print('|'.join(result))
