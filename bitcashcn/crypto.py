from hashlib import new, sha256 as _sha256
schnorr = False
try:
    from freecrypto import PrivateKey as ECPrivateKey, PublicKey as ECPublicKey
    schnorr = True
except:
    from coincurve import PrivateKey as ECPrivateKey, PublicKey as ECPublicKey


def sha256(bytestr):
    return _sha256(bytestr).digest()


def double_sha256(bytestr):
    return _sha256(_sha256(bytestr).digest()).digest()


def double_sha256_checksum(bytestr):
    return double_sha256(bytestr)[:4]


def ripemd160_sha256(bytestr):
    return new('ripemd160', sha256(bytestr)).digest()


hash160 = ripemd160_sha256
