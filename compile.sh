#!/bin/bash

cd code;
pyinstaller servidor.py;
pyinstaller cliente.py;
rm -rf build;
rm -rf __pycache__;
rm cliente.spec;
rm servidor.spec;
cd ..;
chmod 777 servidor.sh;
chmod 777 cliente.sh;

