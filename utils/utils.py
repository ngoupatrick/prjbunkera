import enum
class listMenu(enum.Enum):
    users = "Users"
    zmq = "ZMQ Messaging"

    @classmethod
    def has_value(cls, item):
        return item in cls.__members__.values()