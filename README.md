# AssetDiscovery

AssetDiscover is tool scripted for the use of discovery of assets from a given domain or a list of given domain and run vulnerability scans on web domains for low-hanging fruits and known CVEs. This tool is a combination of amaas, httprobe, nuclei and many other domain enumeration tools. 

# Setup
To setup, there are a few prerequisite tools to install:
* [Go](https://golang.org/)
* [Nuclei](https://github.com/projectdiscovery/nuclei)
* [OWASP amass](https://github.com/OWASP/Amass)
* [subfinder](https://github.com/projectdiscovery/subfinder)
* [crobat](https://github.com/Cgboal/SonarSearch)
* [httprobe](https://github.com/tomnomnom/httprobe)

For ease of setup (For Kali users):
```bash
./setup.sh
```
`setup.sh` requires root privileges as it places Go into your `/usr/local` folder and also uses apt to install amass.

We will look into improving `setup.sh` further for non-Kali users in the future.

# Usage

Basic Usage of the tool:

```
python3 AssetDiscover.py -d <domain> --nuclei -t <directory of nuclei templates>
```

Usage of tool with bruteforce subdomain
```
python3 AssetDiscover.py -d <domain> --brute-force -w <wordlist> --nuclei -t <directory of nuclei templates>
```

## Why use this tool?
This tool is created to help combine functionalities for different tools to better identify assets belonging to target and identify low-hanging fruits or common CVE vulnerabilities found in websites. This will allow users of the tool to identify targets and enumerate general web technology used by the websites.

