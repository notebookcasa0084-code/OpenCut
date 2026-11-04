#!/usr/bin/env bash
set -e

echo "==> Verificando servidor de exibição headless (Xvfb)..."

if [ -z "$DISPLAY" ]; then
    export DISPLAY=:99
fi

if ! pgrep -x "Xvfb" > /dev/null; then
    echo "==> Iniciando Xvfb no DISPLAY $DISPLAY..."
    Xvfb $DISPLAY -screen 0 1280x1024x24 &
    sleep 1
else
    echo "==> Xvfb já está rodando no DISPLAY $DISPLAY."
fi

echo "==> Compilando e executando OpenCut Desktop (GPUI)..."
cargo run --bin desktop
