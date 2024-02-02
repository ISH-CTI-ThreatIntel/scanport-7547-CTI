import socket

def verificar_porta(ip, porta):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10)  # Timeout de 10 segundos para a tentativa de conexão
    try:
        resultado = sock.connect_ex((ip, porta))
        if resultado == 0:
            print(f"A porta {porta} no endereço {ip} está ABERTA.")
        else:
            print(f"A porta {porta} no endereço {ip} está FECHADA.")
    except socket.error as e:
        print(f"Erro de conexão: {e}")
    finally:
        sock.close()

if __name__ == "__main__":
    print("""
██╗  ██╗███████╗██╗███╗   ███╗██████╗  █████╗ ██╗     ██╗         ██╗███████╗██╗  ██╗    
██║  ██║██╔════╝██║████╗ ████║██╔══██╗██╔══██╗██║     ██║         ██║██╔════╝██║  ██║    
███████║█████╗  ██║██╔████╔██║██║  ██║███████║██║     ██║         ██║███████╗███████║    
██╔══██║██╔══╝  ██║██║╚██╔╝██║██║  ██║██╔══██║██║     ██║         ██║╚════██║██╔══██║    
██║  ██║███████╗██║██║ ╚═╝ ██║██████╔╝██║  ██║███████╗███████╗    ██║███████║██║  ██║    
╚═╝  ╚═╝╚══════╝╚═╝╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝    ╚═╝╚══════╝╚═╝  ╚═╝    
                                                                                         
██████╗  ██████╗ ██████╗ ████████╗ █████╗     ███████╗███████╗██╗  ██╗███████╗           
██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╔══██╗    ╚════██║██╔════╝██║  ██║╚════██║           
██████╔╝██║   ██║██████╔╝   ██║   ███████║        ██╔╝███████╗███████║    ██╔╝           
██╔═══╝ ██║   ██║██╔══██╗   ██║   ██╔══██║       ██╔╝ ╚════██║╚════██║   ██╔╝            
██║     ╚██████╔╝██║  ██║   ██║   ██║  ██║       ██║  ███████║     ██║   ██║             
╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝       ╚═╝  ╚══════╝     ╚═╝   ╚═╝             
                                                                                         
""")
    print("""
Dica: Verifique o endereço do seu roteador antes de utilizar o script, o qual normalmente poderá ser o mesmo valor do Gateway da sua conexão. 

Comandos para identificar:

Windows: >ipconfig 
"Gateway Padrão...... <IP Router>"

Linux: >ip route 
"default via <IP Router>"
""")
    # Solicita ao usuário o endereço IP
    IP_ROTEADOR = input("Digite o endereço IP do roteador para verificar a porta 7547: ")
    PORTA = 7547
    verificar_porta(IP_ROTEADOR, PORTA)
