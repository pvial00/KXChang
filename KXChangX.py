from Crypto.Util import number

def genBase(size):
    A = number.getPrime(size)
    B = number.getPrime(size)
    while B == A:
        B = number.getPrime(size)
    return A, B


def keygen(size):
    A, B = genBase(size)
    N = A * B
    sk = number.getRandomRange(1, (N - 1))
    return sk, B, N

def kxchang_demo(size):
    # Generate keys for both parties
    skA, pkA, nA = keygen(size)
    skB, pkB, nB = keygen(size)
    S = nA * nB
    
    # Generate phase 1 by encrypting the public key
    phase1A = pow(pkA, skA, S)
    phase1B = pow(pkA, skB, S)
    # Generate the phase 2 secret modulus
    phase2A = pow(phase1B, skA, S)
    phase2B = pow(phase1A, skB, S)
    # Both parties encrypt y using the secret modulus and send phase3
    phase3A = pow(pkB, skA, phase2A)
    phase3B = pow(pkB, skB, phase2B)
    # Compute the shared secret
    phase4A = pow(phase3B, skA, phase2A)
    phase4B = pow(phase3A, skB, phase2B)
