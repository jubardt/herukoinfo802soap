from spyne import Application, rpc, ServiceBase, Iterable, AnyDict, Integer
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class CarListService(ServiceBase):



    @rpc(_returns=AnyDict)
    def carList(ctx):
        return {"Peugeot206": [500,200], "TeslaX": [780,150], "VolkswageneUp":[180,50], "VolvoEmbla":[320,40], "LucideAirDream": [250,60]}






#Lance le service Soap avec l'appel à notre méthode say_hello
application = Application([CarListService], 'spyne.examples.hello.soap',in_protocol=Soap11(validator='lxml'),out_protocol=Soap11())
wsgi_application = WsgiApplication(application)