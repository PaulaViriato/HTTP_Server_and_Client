# Inicio do programa Cliente:
import sys
import time
import json
import http.client
import collections

server = ""
port   = None

# Estabele conexao HTTP no servidor criado
# que possui IP "server" e opera na porta
# "port", depois executa uma requisicao GET
def conexao (requisicao):
    global server
    global port

    connection = http.client.HTTPConnection(server, port)
    connection.request("GET", requisicao)

    response = connection.getresponse()
    mensagem = str(response.read())
    mensagem = mensagem[2:(len(mensagem)-1)]
    mensagem = mensagem.replace("\\","")
    resjson  = json.loads(mensagem)
    
    return resjson

# Realiza a primeira analise exigida
# Dados sobre a rede e quantidade de IXs
def firstanalise ():
    resix  = conexao ("/api/ixids")
    ixids  = resix["data"]
    ixids  = sorted(set(ixids))
    netid  = []
    result = {}

    for iid in ixids:
        resnt = conexao ("/api/ixnets/"+str(iid))
        nets  = resnt["data"]
        nets  = sorted(set(nets))
        for nid in nets:
            if (nid in netid):
                result[str(nid)]["cixs"] += 1
            else:
                netid.append (nid)
                result[str(nid)] = {}
                result[str(nid)]["name"] = ""
                result[str(nid)]["cixs"] = 1

    maior = 0
    for nid in netid:
        resnt = conexao ("/api/netname/"+str(nid))
        result[str(nid)]["name"] = resnt["data"]
        if (len(resnt["data"]) > maior):
            maior = len(resnt["data"])

    final = sorted(netid)
    for nid in final:
        linha = [str(nid), result[str(nid)]["name"],
                 str(result[str(nid)]["cixs"])]
        print (("{:^7} {:>"+str(maior+1)+"} {:>7}").format(*linha))

# Realiza a segunda analise exigida
# Dados sobre o IX e quantidade de redes
def secondanalise ():
    resix  = conexao ("/api/ixids")
    ixids  = resix["data"]
    ixids  = sorted(set(ixids))
    
    maior = 0
    for iid in ixids:
        resnm = conexao ("/api/ixname/"+str(iid))
        name  = resnm["data"]
        resnt = conexao ("/api/ixnets/"+str(iid))
        nets  = resnt["data"]
        nets  = sorted(set(nets))
        cnts  = len(nets)
        linha = [str(iid), str(name), str(cnts)]
        print (("{:^7} {:>45} {:>5}").format(*linha))

# Programa principal (main)
if __name__ == "__main__":
    global server
    global port

    # Inicializadores para Linux
    # Reestabelece-los quanto for
    # para o Linux
    ip_port         = str(sys.argv[1])
    stropt          = str(sys.argv[2])
    server, strport = ip_port.split(':')
    port            = int(strport)
    opt             = int(stropt)

    # EXCLUIR OU COMENTAR NO LINUX - inicio:
    #entrada         = str(input())
    #ip_port, stropt = entrada.split(' ')
    #server, strport = ip_port.split(':')
    #port            = int(strport)
    #opt             = int(stropt)
    # EXCLUIR OU COMENTAR NO LINUX - fim.

    if (opt == 0): firstanalise ()
    elif (opt == 1): secondanalise ()
    else: print ("Analise invalida!")
# Fim do programa Cliente.