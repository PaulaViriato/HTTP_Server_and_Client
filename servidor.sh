#!/bin/bash
if [ "root" != `whoami` ]
    then echo "Necessario sudo para executar este script!"
    exit
fi
if [ -z $4 ]; then
    echo "Sao necessarios 4 parametros!"
    echo "Formato: porta netfile ixfile netixlanfile"
    exit
else
    sudo ./code/dist/servidor/servidor $1 $2 $3 $4;
fi
