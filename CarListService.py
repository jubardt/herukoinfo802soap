from spyne import Application, rpc, ServiceBase, Iterable, AnyDict, Integer
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class CarListService(ServiceBase):



    @rpc(_returns=AnyDict)
    def carList(ctx):
        return {"Peugeot206": [20,480], "TeslaX": [65,40], "VolkswageneUp":[10,500], "VolvoEmbla":[95,10], "LucideAirDream": [80,60]}






#Lance le service Soap avec l'appel à notre méthode say_hello
application = Application([CarListService], 'spyne.examples.hello.soap',in_protocol=Soap11(validator='lxml'),out_protocol=Soap11())
wsgi_application = WsgiApplication(application)