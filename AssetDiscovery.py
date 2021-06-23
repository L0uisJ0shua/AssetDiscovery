#!usr/bin/python3

import sys
import time
import subprocess
import argparse
from subbrute import subbrute


def main():
    description = "This is a custom made script to execute tools for passive and active enumeration. Created by L0j0"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("-d", "--domain", type=str, metavar="domain")
    parser.add_argument("-df", "--domain-file", type=str, metavar="domainfile")
    parser.add_argument("--brute-force", action='store_true', dest="brute_forcing")
    parser.add_argument("-w", type=str, dest="wordlist")
    parser.add_argument("--nuclei", action='store_true')
    parser.add_argument("-t", type=str, dest="templates")

    args = parser.parse_args()
    if args.domain == None and args.domain_file == None:
        parser.print_help()
        sys.exit(1)
    
    if args.nuclei and args.templates == None:
        parser.error("(-) Please give the destination of the nuclei templates! (-t flag is missing argument)")

    if args.brute_forcing and args.wordlist == None:
        parser.error("(-) Please give the destination of the wordlist you wish to use for Brute Forcing. (-w flag is missing argument)")
    
    domainlist = []
    if args.domain_file != None:
        with open(args.domain_file, "r") as my_file:
            lines = my_file.read().split("\n")
            domainlist = lines
    else:
        domainlist.append(args.domain)
    
    # print(domainlist)
    start = time.time()
    for domain in domainlist:
        subprocess.run(args=["mkdir", "{domain}"], shell=True)
        subprocess.run(args=["cd", "{domain}"], shell=True)
        passive_enum_scan(domain)
        if args.brute_forcing:
            domain_brute(domain, args.wordlist)
        cleanup(domain)
        probe(domain)
        if args.nuclei:
            vuln_scanning(domain, args.templates)
        end = time.time()
        print(f"Runtime for the scan is {end - start} seconds")
        subprocess.run(args=["cd", "../"], shell=True)

def passive_enum_scan(domain: str):
    print(f"(+) Begining passive enumeration for {domain}")
    with open("temp.txt", "w+") as temp_file:
        
        ## Tool 1: AMASS Passive Enumeration
        start = time.time()
        print("(+) Scanning target with amass...")
        subprocess.run(args=["amass", "enum", "-d", domain], stdout=temp_file)
        print(f"(+) Amass Scan completed. Elapsed Time: {time.time() - start}")

        ## Tool 2: Subfinder Passive Enumeration
        print("(+) Scanning target with subfinder...")
        subprocess.run(args=[ "subfinder", "-nW", "-d", domain], stdout=temp_file)
        print(f"(+) subfinder Scan completed. Elapsed Time: {time.time() - start}")

        ## Tool 3: Sonar
        print("(+) Scanning target with sonar...")
        subprocess.run(args=["crobat", "-s", domain], stdout=temp_file)
        print(f"(+) Sonar Scan completed. Elapsed Time: {time.time() - start}")

def cleanup(domain: str):
    """
    Sorts and collate only unique occurence of subdomains found.
    """
    with open(f"{domain}_assets.txt", "w+") as asset_file:
        print(f"(+) Scan completed. Taking only unique findings and writing to {domain}_assets.txt")
        subprocess.run(args=["sort", "-u", "temp.txt"], stdout=asset_file)
        subprocess.run(args="rm temp.txt", shell=True)

def probe(domain: str):
    with open(f"{domain}_urls.txt", "w+") as urls_file:

        ## Tool for Probing: httprobe
        start = time.time()
        print("(+) Running httprobe on assets found...")
        subprocess.run(args=f"cat {domain}_assets.txt | httprobe", shell=True, stdout=urls_file)
        print(f"(+) Probed Successful. Results is written to {domain}_urls.txt. Elasped Time: {time.time() - start}")

def vuln_scanning(domain: str, templates: str):

    ## Tool for Vulnerability Scanning: Nuclei
    start = time.time()
    print(f"(+) Scanning {domain}_urls.txt for vulnerabilities with Nuclei...")
    subprocess.run(args=f"nuclei -l {domain}_urls.txt -t {templates} -new-templates -o {domain}_nuclei.txt", shell=True)
    print(f"(+) Nuclei Scan completed. Elapsed Time: {time.time() - start}")



def domain_brute(domain: str, wordlist: str):
    with open("temp.txt", "w+") as temp_files:
        domlist = []
        start = time.time()
        # Tool for Bruteforcing : Subbrute
        print(f"(+) Bruteforcing of Subdomain is enabled!")
        print(f"(+) Running subbrute now...")
        for d in subbrute.run(target=domain, subdomains=wordlist, process_count = 10):
            domlist.append(d[0])
        print(f"(+) Bruteforcing ended. Writing to file now")
        for dom in domlist:
            temp_files.write(dom + "\n")

        print(f"(+) Write Successful.{time.time() - start}")

if __name__ == "__main__":
    main()
