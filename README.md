# AssetDiscovery

AssetDiscover is tool scripted for the use of discovery of assets from a given domain or a list of given domain and run vulnerability scans on web domains for low-hanging fruits and known CVEs. This tool is a combination of amaas, httprobe, nuclei and many other domain enumeration tools. 

# Setup
To setup, there are a few prerequisite tools to install:
    - Go
    - Nuclei
    - amass
    - subfinder
    - crobat
    - httprobe

There is currently a work-in-progress script that we are working on to help standardise installation to make it easier to setup.

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
This tool is created to help combine functionalities for different tools to better identify assets belonging to target and identify low-hanging fruits or common CVE vulnerabilities found in websites. This will allow users of the tool to identify targets and enumerate general web technology used by the website.
