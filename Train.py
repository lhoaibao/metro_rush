class Train:
    def __init__(self, id, line, id_station, name_station):
        self.id = ''
        self.line = ''
        self.id_station = 0
        self.name_station = ''

    def get_status(self):
        status = '{}({}:{})-{}'.format(self.name_station, self.line,
                                       self.id_station, self. id)
        return status
