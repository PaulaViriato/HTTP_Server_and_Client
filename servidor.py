# Inicio do programa Servidor:
from http.server import BaseHTTPRequestHandler,HTTPServer
import sys
import time
import json

netjson = None
ixjson = None
netixlanjson = None

# Leitura dos arquivos de dados JSON iniciais
# para as respectivas tabelas net, ix e netixlan.
# Armazenamento dos dados em dicionarios.
def setArquivos (netfile, ixfile, netixlanfile):
    global netjson
    global ixjson
    global netixlanjson

    netarq      = open(netfile, encoding="utf8")
    ixarq       = open(ixfile, encoding="utf8")
    netixlanarq = open(netixlanfile, encoding="utf8")

    nettext      = ""
    ixtext       = ""
    netixlantext = ""

    texto = netarq.readlines()
    for linha in texto: nettext += linha
    netarq.close()

    texto = ixarq.readlines()
    for linha in texto: ixtext += linha
    ixarq.close()

    texto = netixlanarq.readlines()
    for linha in texto: netixlantext += linha
    netixlanarq.close()

    netjson      = json.loads(nettext)
    ixjson       = json.loads(ixtext)
    netixlanjson = json.loads(netixlantext)

# Classe para manipulacao do protocolo HTTP.
# Herda da classe BaseHTTPRequestHandler e
# sobrescreve o metodo do_GET
class HTTP (BaseHTTPRequestHandler): 
    # Verifica o tipo de requisicao feita
    # manipula os dados nos dicionarios globais
    # e retorna a resposta ao requisitante
    def do_GET(self):
        global netjson
        global ixjson
        global netixlanjson

        resposta = ""
        if ("/api/ixids" in self.path):
            listaixids = []
            for ix in ixjson["data"]:
                listaixids.append (int(ix["id"]))
            resjson = {}
            resjson["data"] = listaixids
            resposta = json.dumps(resjson)
        elif ("/api/ixnets/" in self.path):
            desmembra = self.path.split("/api/ixnets/")
            ixid = int(desmembra[len(desmembra)-1])
            listaixnets = []
            for ixlan in netixlanjson["data"]:
                if (int(ixlan["ix_id"]) == ixid):
                    listaixnets.append (int(ixlan["net_id"]))
            resjson = {}
            resjson["data"] = listaixnets
            resposta = json.dumps(resjson)
        elif ("/api/netname/" in self.path):
            desmembra = self.path.split("/api/netname/")
            netid = int(desmembra[len(desmembra)-1])
            netname = ""
            for net in netjson["data"]:
                if (int(net["id"]) == netid):
                    netname = str(net["name"])
            resjson = {}
            resjson["data"] = netname
            resposta = json.dumps(resjson)
        elif ("/api/ixname/" in self.path):
            desmembra = self.path.split("/api/ixname/")
            ixid = int(desmembra[len(desmembra)-1])
            ixname = ""
            for ix in ixjson["data"]:
                if (int(ix["id"]) == ixid):
                    ixname = str(ix["name"])
            resjson = {}
            resjson["data"] = ixname
            resposta = json.dumps(resjson)
        else:
            resjson = {}
            resjson["data"] = "Requisicao invalida!"
            resposta = json.dumps(resjson)

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(resposta, "ascii"))
        return

# Programa principal (main)
if __name__ == "__main__":
    # Inicializadores para Linux
    # Reestabelece-los quanto for
    # para o Linux
    strport      = str(sys.argv[1])
    netfile      = str(sys.argv[2])
    ixfile       = str(sys.argv[3])
    netixlanfile = str(sys.argv[4])
    port         = int(strport)

    # EXCLUIR OU COMENTAR NO LINUX - inicio:
    #entrada = str(input())
    #strport, netfile, ixfile, netixlanfile = entrada.split(' ')
    #port = int(strport)
    # EXCLUIR OU COMENTAR NO LINUX - fim.
    
    try:
        setArquivos (netfile, ixfile, netixlanfile)
        server = HTTPServer(("127.0.0.1", port), HTTP)
        server.serve_forever()
    except KeyboardInterrupt: server.socket.close()
# Fim do programa Servidor.
