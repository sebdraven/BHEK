'''
Created on Sep 18, 2012

@author: slarinier
use python bhek.py --scriptjs bhek.js --domains_filedomaine_list_txt --url_file list_panel.txt --padding 0
'''
import argparse
import re
import sys
import subprocess
from subprocess import Popen, PIPE
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='BHEK Tracking by google')
    parser.add_argument('--scriptjs', dest='scriptjs',help='Script JS for CasperJS')
    parser.add_argument('--domains_file', dest='domains_file')
    parser.add_argument('--url_file', dest='url_file')
    parser.add_argument('--padding',dest='padding')
    args=parser.parse_args()
    urls=[]
    domains=[]
    urls_to_add=[]
    domains_to_add=[]
    if args.scriptjs ==None:
        parser.print_help()
        sys.exit(-1)
    if args.domains_file == None:
        parser.print_help()
        sys.exit(-1)
    else:
        with open(args.domains_file,'r') as fr:
            for ligne in fr:
                domains.append(ligne.strip())
    if args.url_file == None:
        parser.print_help()
        sys.exit(-1)
    else: 
        with open(args.url_file,'r') as fr:
            for ligne in fr:
                urls.append(ligne.strip())
    result=subprocess.Popen(['casperjs' ,args.scriptjs,args.padding],stdout=PIPE)
    pattern_blackhole='(http://(.*)/bhadmin\.php)'
    re_blackhole = re.compile(pattern_blackhole)
    
    for ligne in result.stdout:
        m=re_blackhole.search(ligne)
        if m:
            url=m.group(1)
            domaine=m.group(2)
            print url
            print domaine
            if not url in urls:
                urls_to_add.append(url)
            if not domaine in domains:
                domains_to_add.append(domaine)
    with open(args.domains_file,'a') as fw:
        for domain_to_add in domains_to_add:
            fw.write(domain_to_add+'\n')
    with open(args.url_file,'a') as fw:
        for url_to_add in urls_to_add:
            fw.write(url_to_add+'\n')        
    pass