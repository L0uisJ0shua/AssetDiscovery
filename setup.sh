#!/usr/bin/bash

## TODO ##
# Require testing if the script works well

# Go
echo "[-] Checking if Go is present..."
if ! go_loc="$(type -p 'go --version')" || [[ -z $go_loc ]]; then
    echo "[+] Grabbing Go..."
    wget https://golang.org/dl/go1.16.4.linux-amd64.tar.gz
    echo "[+] Installing Go lang..."
    sudo rm -rf /usr/local/go
    sudo tar -C /usr/local -xzf go1.16.4.linux-amd64.tar.gz
    sudo rm go1.16.4.linux-amd64.tar.gz
    export PATH="$PATH:/usr/local/go/bin"
    export PATH="$PATH:$HOME/go/bin"
    go --version
    echo "[+] Go is installed successfully."
else
    echo "[+] Go already installed."
fi

set -e

# httprobe
echo "[-] Checking if httprobe is installed..."
if ! probe_loc="$(type -p 'httprobe -h')" || [[ -z $probe_loc ]]; then
    echo "[+] Installing httpprobe..."
    go get -u github.com/tomnomnom/httprobe
    echo "[+] httprobe is installed successfully."
else
    echo "[+] httprobe already installed."
fi

# SonarSearch
echo "[-] Checking if SonarSearch is present..."
if ! crobat_loc="$(type -p 'crobat -h')" || [[ -z $crobat_loc ]]; then
    echo "[+] Installing SonarSearch..."
    go get github.com/Cgboal/SonarSearch/crobat
    echo "[+] Installed SonarSearch"
else
    echo "[+] SonarSearch already installed."
fi

# amass
echo "[-] Checking if OWASP Amass is installed..."
if ! amass_loc="$(type -p 'amass -version')" || [[ -z $amass_loc ]]; then
    echo "[+] Installing OWASP Amass..."
    sudo apt -y install amass
    amass -version
    echo "[+] OWASP Amass is installed successfully"
else
    echo "[+] OWASP Amass already installed."
fi

# subfinder
echo "[-] Checking if Subfinder is installed..."
if ! amass_loc="$(type -p 'subfinder -h')" || [[ -z $amass_loc ]]; then
    echo "[+] Installing Subfinder..."
    GO111MODULE=on go get -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder
    subfinder -h
    echo "[+] subfinder installed successfully"
else
    echo "[-] Subfinder already installed"
fi

# nuclei
echo "[-] Checking if Nuclei is installed..."
if ! amass_loc="$(type -p 'nuclei -version')" || [[ -z $amass_loc ]]; then
    echo "[+] Installing Nuclei..."
    GO111MODULE=on go get -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei
    nuclei -version
    echo "[+] Nuclei is installed successfully"
else
    echo "[+] Nuclei already installed."
fi

echo "[+] Setup of pre-requsite for AssetDiscovery is successfully complated."
