from hashlib import new as newhasher


def hash_string(string):
    hasher = newhasher("md5")
    hasher.update(string.encode())
    return hasher.hexdigest()
