# Script para sacar el SHA2 de cada file
# 1.0 - Ulises2k
import os
import hashlib
import time

DirWindows = ['c:\\Program Files\\', 'c:\\Program Files (x86)\\', 'c:\\Windows\\']
DirLinux = ['/usr/bin/', '/usr/sbin/', '/usr/local/bin/', '/usr/local/sbin/', '/etc/']


def create_hashfile(pathfilename=""):
    sha256_hash = hashlib.sha256()
    with open(pathfilename, "rb") as f:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
        ts=time.time()
        hash=sha256_hash.hexdigest()
        print(f'{ts};{hash};{pathfilename}')


def recorrer_dir(d=""):
    for nombre_directorio, dirs, ficheros in os.walk(d):            
        for nombre_fichero in ficheros:
            pathfilename=""
            pathfilename=os.path.join(pathfilename, nombre_directorio, nombre_fichero)
            create_hashfile(pathfilename)





SistemaOperativo = os.name
if SistemaOperativo == 'nt':
    for d in DirWindows:
        pathname=recorrer_dir(d)
else:
    for d in DirLinux:
        pathname=recorrer_dir(d)



