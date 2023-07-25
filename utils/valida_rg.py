import re

def valida_rg(rg):

    padrao_rg = r'^\d{2}\.\d{3}\.\d{3}-[0-9A-Za-z]$'

    if re.match(padrao_rg, rg):
        return True
    else:
        return False

rg = "12.345.678-x"
print(valida_rg(rg))