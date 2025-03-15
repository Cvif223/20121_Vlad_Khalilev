class Server:
    tmp_ip = 0
    def __init__(self):
        Server.tmp_ip = Server.tmp_ip + 1
        self.ip = self.tmp_ip
        self.linked_routers = {}
        self.buffer = []
    def get_data(self):
        b = self.buffer
        self.buffer = []
        return b

    def send_data(self, data):
        for router in self.linked_routers.values():
            router.buffer.append(data)

    def get_ip(self):
        return self.ip

class Router:
    tmp_ip = 0
    def __init__(self):
        Router.tmp_ip = Router.tmp_ip + 1
        self.ip = self.tmp_ip
        self.linked_servers = {}
        self.buffer = []
    def link(self, server):
        self.linked_servers[server.ip] = server
        server.linked_routers[self.ip] = self
    def unlink(self, server):
        del self.linked_servers[server.ip]
        del server.linked_routers[self.ip]

    def send_data(self):
        for data in self.buffer:
            if data.ip in self.linked_servers.keys():
                target_server = self.linked_servers[data.ip]
                target_server.buffer.append(data)
        self.buffer = []



class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip

"""rt1 = Router()
sv1 = Server()
rt1.link(sv1)
sv1.send_data(Data("хуй", 1))
rt1.send_data()"""
assert hasattr(Router, 'link') and hasattr(Router, 'unlink') and hasattr(Router, 'send_data'), "в классе Router присутсвутю не все методы, указанные в задании"
assert hasattr(Server, 'send_data') and hasattr(Server, 'get_data') and hasattr(Server, 'get_ip'), "в классе Server присутсвутю не все методы, указанные в задании"
router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()
assert len(router.buffer) == 0, "после отправки сообщений буфер в роутере должен очищаться"
assert len(sv_from.buffer) == 0, "после получения сообщений буфер сервера должен очищаться"
assert len(msg_lst_to) == 2, "метод get_data вернул неверное число пакетов"
assert msg_lst_from[0].data == "Hi" and msg_lst_to[0].data == "Hello", "данные не прошли по сети, классы не функционируют должным образом"
assert hasattr(router, 'buffer') and hasattr(sv_to, 'buffer'), "в объектах классов Router и/или Server отсутствует локальный атрибут buffer"
router.unlink(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
router.send_data()
msg_lst_to = sv_to.get_data()
assert msg_lst_to == [], "метод get_data() вернул неверные данные, возможно, неправильно работает метод unlink()"