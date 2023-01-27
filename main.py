import hmac
import string
import random

CHARSROLL = 15
MAXROLL = 100000


def random_string(size=6, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def get_roll(server_seed, client_seed, nonce):
    hash = hmac.new(server_seed.encode(), f"{client_seed}-{nonce}".encode(), "sha512").hexdigest()
    partHash = hash[:CHARSROLL]
    roll = int(partHash, 16) % MAXROLL
    return roll + 1


def create_public_hash(server_seed, salt):
    return hmac.new(server_seed.encode(), salt.encode(), "sha256").hexdigest()


if __name__ == "__main__":
    server_seed = random_string(32)
    secret_sald = random_string(12)
    client_seed = "ABCDE5FG"
    nonce = 0

    # create public Hash
    print(create_public_hash(server_seed, secret_sald))
    # get roll
    print(get_roll(server_seed, client_seed, nonce))