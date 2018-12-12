# HTTP Server and Client

## Desenvolvido por: Paula Jeniffer dos Santos Viriato
## Email: paulaviriato@dcc.ufmg.br
<br><br>
## SOBRE O CODIGO:
-> Linguagem: Python3.6.7<br>
-> Script de compilacao: compile.sh<br>
-> Script de execucao do servidor: servidor.sh<br>
-> Script de execucao do cliente: cliente.sh<br>
-> Disponivel no GitHub: github.com/PaulaViriato/HTTP_Server_and_Client<br>
<br>
## REQUISITOS:
-> Python3. Comando de instalacao: sudo apt install python3.5<br>
-> Pyinstaller. Comando de instalacao: pip3 install pyinstaller<br>
<br>
## Compilacao:
-> Comando script: ./compile.sh<br>
-> Sem script:<br>
   - Comando inicial: cd code
   - Comando para o servidor: pyinstaller servidor.py
   - Comando para o cliente: pyinstaller cliente.py
   - Comando inicial: cd ..
<br>
## Execucao do Servidor com o script:
-> Necessita estar como usuário sudo.<br>
-> Comando primeiro plano: ./servidor.sh porta netfile ixfile netixlanfile<br>
-> Comando finalizacao primeiro plano: ctrl + c<br>
-> Comando segundo plano: nohup ./servidor.sh porta netfile ixfile netixlanfile > servidor.error 2> servidor.log &<br>
-> Comando finalizacao segundo plano: fg 1 + ctrl + c<br>
<br>
## Execucao do Servidor sem o script:
-> Necessita estar como usuário sudo.<br>
-> Comando primeiro plano: ./code/dist/servidor/servidor porta netfile ixfile netixlanfile<br>
-> Comando finalizacao primeiro plano: ctrl + c<br>
-> Comando segundo plano: nohup ./code/dist/servidor/servidor porta netfile ixfile netixlanfile > servidor.error 2> servidor.log &<br>
-> Comando finalizacao segundo plano: fg 1 + ctrl + c<br>
<br>
## Execucao do Cliente:
-> Comando com script: ./cliente.sh servidor:porta opcao<br>
-> Comando sem script: ./code/dist/cliente/cliente servidor:porta opcao<br>
<br>
## Observacoes:
-> Relatorio em: relatorio.pdf<br>
-> Nao e necessario bibliotecas externas<br>
-> Arquivos do banco de dados testado estao no diretorio input.
