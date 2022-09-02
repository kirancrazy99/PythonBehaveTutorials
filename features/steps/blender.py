

class Blender(object):

    Transformation_Map = {'Red Tree Frog':'Mush',
                          'Apples':'Apple juice',
                          'iPhone':'Toxic Wastage',
                          'Galaxy Nexus':'Toxic Wastage'}

    def __init__(self):
        self.thing = None
        self.result = None

    @classmethod
    def search_result_for(cls,thing):
        return cls.Transformation_Map.get(thing,'DIRT')

    def add(self,thing):
        self.thing = thing

    def switch_on(self):
        self.result = self.search_result_for(self.thing)

