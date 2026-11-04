#!/bin/bash
echo "=== Iniciando ambiente OpenCut no Codespace ==="
export PROTO_HOME="$HOME/.proto"
export PATH="$PROTO_HOME/bin:$PATH"

echo "Verificando versão do moon..."
moon --version

echo "Iniciando tarefa web:dev..."
moon run web:dev
