#!/usr/bin/env bash
set -e

echo "==> Verificando dependências e permissões dos scripts..."
chmod +x dev.sh dev-desktop.sh 2>/dev/null || true

echo "==> Executando inicializador principal do OpenCut..."
./dev.sh
