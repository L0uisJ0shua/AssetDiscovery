#!/usr/bin/bash

## TODO ##
# Script is roughly tested but does not work properly to install all the
# components properly yet

# Go
echo "[+] Grabbing Go..."
wget https://golang.org/dl/go1.16.4.linux-amd64.tar.gz
echo "[+] Installing Go lang..."
sudo rm /usr/local/go
sudo tar -C /usr/local -xzf go1.16.4.linux-amd64.tar.gz

# httpx
echo "[+] Installing httpx..."
GO111MODULE=on go get -v github.com/projectdiscovery/httpx/cmd/httpx

# aquatone
echo "[+] Grabbing aquatone..."
wget https://github.com/michenriksen/aquatone/releases/download/v1.7.0/aquatone_linux_amd64_1.7.0.zip
echo "[+] Installing aquatone by moving it to /usr/bin..."
sudo tar -C /usr/bin -xzf aquatone_linux_amd64_1.7.0.zip

# amass
echo "[+] Installing OWASP Amass..."
sudo apt install amass

# nuclei
echo "[+] Installing Nuclei..."
GO111MODULE=on go get -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei
