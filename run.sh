#!/bin/bash
echo "=== OpenCut - Gerenciador de Inicialização ==="
echo "Escolha o modo de execução:"
echo "1) Web (Porta 5173)"
echo "2) Desktop (via Xvfb)"
read -p "Digite sua escolha [1 ou 2]: " choice

case $choice in
    1)
        ./dev.sh
        ;;
    2)
        ./dev-desktop.sh
        ;;
    *)
        echo "Opção inválida. Executando modo Web por padrão..."
        ./dev.sh
        ;;
esac
