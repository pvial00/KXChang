from Crypto.Util import number

def genBase(size):
    A = number.getPrime(size)
    B = number.getPrime(size)
    while B == A:
        B = number.getPrime(size)
    return A, B


def keygen(size):
    A, B = genBase(size)
    sk = number.getRandomRange(1, (B - 1))
    return sk, B, A

def kxchang_demo(size):
    # Generate keys for both parties
    skA, pkA, nA = keygen(size)
    skB, pkB, nB = keygen(size)
    # Generate phase 1 by encrypting the public key
    phase1A = pow(pkA, skA, nA)
    phase1B = pow(pkA, skB, nA)
    # Generate the phase 2 secret modulus
    phase2A = pow(phase1B, skA, nA)
    phase2B = pow(phase1A, skB, nA)
    # Both parties encrypt y using the secret modulus and send phase3
    phase3A = pow(pkB, skA, phase2A)
    phase3B = pow(pkB, skB, phase2B)
    # Compute the shared secret
    phase4A = pow(phase3B, skA, phase2A)
    phase4B = pow(phase3A, skB, phase2B)
