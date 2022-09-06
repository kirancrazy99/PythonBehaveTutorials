class Department:
    def __init__(self, name, members=None):
        if not members:
            members = []
        self.name = name
        self.members = members

    def add_m(self, name):
        assert name not in self.members
        self.members.append(name)

    @property
    def count(self):
        return len(self.members)

    def __len__(self):
        return self.count


class Model:
    def __init__(self):
        self.users = []
        self.departments = {}

    def add_users(self, name, department):
        assert name not in self.users
        if department not in self.departments:
            self.departments[department] = Department(department)
        self.departments[department].add_m(name)

    def count_persons_per_dept(self):
        pass

    def get_head_count(self, department):
        return self.departments[department].count
