class Loader:
    @staticmethod
    def parse_format(string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)
        return seq
class Factory:
    @staticmethod
    def build_sequence():
        a = []
        return a
    @staticmethod
    def build_number(string):
        st = int(string)
        return st

res = Loader.parse_format("4, 5, -6", Factory)
print(res)
res2 = Loader.parse_format("4, 5, -6", Factory)
print(res2)