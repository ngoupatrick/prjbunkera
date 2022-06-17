import enum
class listMenu(enum.Enum):
    users = "Users"
    image = "Image"
    audio = "Audio"
    text = "Text"

    @classmethod
    def has_value(cls, item):
        return item in cls.__members__.values()