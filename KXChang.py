from Crypto.Util import number

def genBase(size):
    A = number.getRandomNBitInteger(size)
    B = number.getRandomNBitInteger(size)
    while B == A:
        B = number.getRandomNBitInteger(size)
    return A, B


def keygen(size):
    good = 0
    A, B = genBase(size)
    D = A * B
    x = number.getRandomRange(1, (A - 1))
    y = number.getRandomRange(1, (A - 1))
    z = (x + y) % D
    return z, x, D

def kxchang_demo(size):
    # Generate keys for both parties
    skA, pkA, nA = keygen(size)
    skB, pkB, nB = keygen(size)
    # Exchange public modulus and create the shared modulus
    S = nA * nB
    # One party generates a point between 1 and S minus 1
    y = number.getRandomRange(1, (S - 1))
    # Generate phase 1 by encrypting the public key
    phase1A = pow(pkA, skA, S)
    phase1B = pow(pkA, skB, S)
    # Generate the phase 2 secret modulus
    phase2A = pow(phase1B, skA, S)
    phase2B = pow(phase1A, skB, S)
    # Both parties encrypt y using the secret modulus and send phase3
    phase3A = pow(y, skA, phase2A)
    phase3B = pow(y, skB, phase2B)
    # Compute the shared secret
    phase4A = pow(phase3B, skA, phase2A)
    phase4B = pow(phase3A, skB, phase2B)
