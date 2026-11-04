#!/usr/bin/env bash
set -e

echo "==> Iniciando o ambiente de desenvolvimento do OpenCut..."

# Verifica se o diretório node_modules existe na raiz ou apps/web
if [ -d "node_modules" ] || [ -d "apps/web" ]; then
    echo "==> Iniciando aplicação web (Next.js)..."
    # Adicione aqui a lógica de inicialização web se necessário, ou chame o gerenciador do moon
fi

echo "==> Ambiente configurado. Utilize './dev-desktop.sh' para rodar a interface GPUI."
