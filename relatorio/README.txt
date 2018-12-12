Desenvolvido por: Paula Jeniffer dos Santos Viriato
Email: paulaviriato@dcc.ufmg.br

SOBRE O CODIGO:
-> Linguagem: Python3.6.7
-> Script de compilacao: compile.sh
-> Script de execucao do servidor: servidor.sh
-> Script de execucao do cliente: cliente.sh
-> Disponivel no GitHub: github.com/PaulaViriato/HTTP_Server_and_Client

REQUISITOS:
-> Python3. Comando de instalacao: sudo apt install python3.5
-> Pyinstaller. Comando de instalacao: pip3 install pyinstaller

Compilacao:
-> Comando script: ./compile.sh
-> Sem script:
   - Comando inicial: cd code
   - Comando para o servidor: pyinstaller servidor.py
   - Comando para o cliente: pyinstaller cliente.py
   - Comando inicial: cd ..

Execucao do Servidor com o script:
-> Necessita estar como usuário sudo.
-> Comando primeiro plano: ./servidor.sh porta netfile ixfile netixlanfile
-> Comando finalizacao primeiro plano: ctrl + c
-> Comando segundo plano: nohup ./servidor.sh porta netfile ixfile netixlanfile > servidor.error 2> servidor.log &
-> Comando finalizacao segundo plano: fg 1 + ctrl + c

Execucao do Servidor sem o script:
-> Necessita estar como usuário sudo.
-> Comando primeiro plano: ./code/dist/servidor/servidor porta netfile ixfile netixlanfile
-> Comando finalizacao primeiro plano: ctrl + c
-> Comando segundo plano: nohup ./code/dist/servidor/servidor porta netfile ixfile netixlanfile > servidor.error 2> servidor.log &
-> Comando finalizacao segundo plano: fg 1 + ctrl + c

Execucao do Cliente:
-> Comando com script: ./cliente.sh servidor:porta opcao
-> Comando sem script: ./code/dist/cliente/cliente servidor:porta opcao

Observacoes:
-> Relatorio em: relatorio.pdf
-> Nao e necessario bibliotecas externas
-> Arquivos do banco de dados testado estao no diretorio input.
