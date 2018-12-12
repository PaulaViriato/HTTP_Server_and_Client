#!/bin/bash
if [ -z $2 ]; then
    echo "Sao necessarios 2 parametros!"
    echo "Formato: servidor:porta opcao"
    exit
else
    ./code/dist/cliente/cliente $1 $2;
fi
