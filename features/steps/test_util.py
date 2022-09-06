class NamedNumber:
    Map = {'one':1,
           'two':2,
           'three':3,
           'four':4,
           'five':5}

    @classmethod
    def from_string(cls,named_number):
        name = named_number.strip().lower()
        return cls.Map[name]