#!/bin/bash
echo "=== Verificando dependências gráficas para o Desktop ==="
if ! command -v xvfb-run &> /dev/null; then
    echo "Instalando Xvfb para suporte gráfico headless..."
    sudo apt-get update && sudo apt-get install -y xvfb libxkbcommon-dev libxkbcommon-x11-dev
fi

echo "Iniciando versão desktop sob Xvfb..."
export PROTO_HOME="$HOME/.proto"
export PATH="$PROTO_HOME/bin:$PATH"
xvfb-run -a moon run desktop:dev
