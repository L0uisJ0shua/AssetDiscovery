#!/usr/bin/python3

import sys
import os
import time
import subprocess
import argparse

def main():
    description = "Python Script to Enumerate Assets if web service is present. Created by L0j0"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("--domain-file", type=str, metavar="domainfile", required=True)
    parser.add_argument("-P", type=int, metavar="ports", nargs="+")

    args = parser.parse_args()
    assets = []

    with open(args.domain_file, "r") as r_file:
        lines = r_file.read().split("\n")
        assets = lines

    if args.P == None:
        ports = args.P
    else:
        ports = [80, 443, 8080]

    cwd = os.getcwd()
    start = time.time()

    for asset in assets:
        if asset == "":
            continue
        ## Make Directory
        if not os.path.exists(f"{cwd}/{asset}"):
            os.mkdir(asset)
        os.chdir(cwd+f"/{asset}")

        ## Conducting Enumeration
        initial_scan(asset, ports)
        os.chdir("../")

    end = time.time()
    print(f"Runtime for the scan is {end - start} seconds")


def initial_scan(asset: str, ports: list):
    port_numbers = ""
    with open (f"{asset}_initial_nmap_scan.txt", "w+") as temp_file:
        for port in ports:
            port_numbers += f"{port},"
        subprocess.run(args=f"nmap -p {port_numbers[:-1]} {asset}", shell=True, stdout=temp_file)

if __name__ == "__main__":
    main()
