"""
http://www.pythonchallenge.com/pc/def/map.html
"""
from string import maketrans

secret = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
intab = string.ascii_letters
outtab = intab[2:] + intab[0:2]

if __name__ == "__main__":
    trans_tab = str.maketrans(intab, outtab)
    print("secret:\n {}\n translated:\n {}".format(secret, secret.translate(trans_tab)))


