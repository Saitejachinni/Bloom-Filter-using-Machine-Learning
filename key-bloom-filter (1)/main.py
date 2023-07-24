def fnv1a_hash(key, seed):
    fnv_prime = 16777619
    hash_value = seed
    for byte in key:
        hash_value = (hash_value ^ byte) * fnv_prime
    return hash_value
def insert_keyBF(b2, buff, i):
    h1 = fnv1a_hash(buff, seed1)
    h2 = fnv1a_hash(buff, seed2)
    h3 = fnv1a_hash(buff, seed3)
    # h4 = fnv1a_hash(buff, seed4)
    # h5 = fnv1a_hash(buff, seed5)

    _set_(b2, h1)
    _set_(b2, h2)
    _set_(b2, h3)
    # _set_(b2, h4)
    # _set_(b2, h5)

def lookup_keyBF(b2, buff, i):
    h1 = fnv1a_hash(buff, seed1)
    h2 = fnv1a_hash(buff, seed2)
    h3 = fnv1a_hash(buff, seed3)
    # h4 = fnv1a_hash(buff, seed4)
    # h5 = fnv1a_hash(buff, seed5)
    if _test_(b2, h1) == 1:
        if _test_(b2, h2) == 1:
            if _test_(b2, h3) == 1:
                # if _test_(b2, h4) == 1:
                #     if _test_(b2, h5) == 1:
                return 1
    return 0
