# O código do gerenciador vai ser responsável por gerenciar quem tem acesso ao complexo.
# Também irá gerenciar a quantidade de pessoas que estão presentes, tanto no complexo quanto
# nos prédios e andares.


import time
import zmq
import sys

# Sessão de definição de sockets:
# Socket que irá receber as requisições de entrada dos clientes
porta_servidor = "5555"
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:"+ porta_servidor) 
# Socket que irá efetuar as requsições de autenticação dos clientes
porta_cliente = "5556"
socket_cliente = context.socket(zmq.REQ)
socket_cliente.connect("tcp://localhost:"+porta_cliente)

# Fim da definição de sockets

# Definição das listas de controle de usuários:
usuarios_permitidos = ["1"]     # Contém as id's dos usuários permitidos no complexo
lista_predios = [["1", 0, []]]           # Contém as id's dos prédios, população e lista de usuarios presentes
lista_andares = [[["1", "1"], 0, []]]           # Contém as id's dos andares ([id_predio, id_andar]), população e lista de usuarios presentes

# Fim da definição das listas








# Realiza a autenticação do usuário no complexo
def Autentica_Pessoa(id_user, cargo):
    # Se o usuário tem credencial de visitante, ele tem acesso
    if cargo == "VISITANTE":
        return True
    elif id_user in usuarios_permitidos: # Se não, apenas se for credenciado
        return True
    else:
        return False


def Verifica_Credenciais(id_user, id_predio, id_andar, cargo):
    if id_andar == None:
        print("O usuario deseja ir para um prédio")
    else:
        print("O usuario deseja ir para um andar")
    
    
    print("credenciais")


def Requsicao_Andar():
    print("Envia requsicao para andar")


def Requisicao_Predio():
    print("Envia requsicao para predio")




def main():
    while True:
        #As requisições recebidas serão do tipo: [id_user, predio, andar, cargo]
        requsicao = socket.recv_string()
        id_user, id_predio, id_andar, cargo = requsicao.split()
        #Verificia se usuário pode entrar no complexo
        permissao = Autentica_Pessoa(id_user, cargo)    
        if not permissao:
            # Envia a resposta negando a requisição do usuário
            socket.send_string("NEGADO COMPLEXO")
        else:
            # Se for permitida a entrada do usuário no complexo, deverá ser
            # feita a verificação de autenticação do usuário no destino
            Verifica_Credenciais(id_user, id_predio, id_andar, cargo)










if __name__ == "__main__":
    main()