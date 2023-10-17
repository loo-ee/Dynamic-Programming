from diffie_hellman.prime_randomizer import generate_random_prime
import random


def __get_key(number: int, exponent: int, prime_key: int) -> int:
    powered = pow(number, exponent, prime_key)

    return powered


def __get_secret() -> int:
    prime_num: int
    generated_key: int

    while True:
        prime_num = generate_random_prime()

        print('Prime number: ', prime_num)
        choice = input('Press [X] to generate another prime number: ')

        if choice.lower() != 'x':
            break

    while True:
        generated_key = random.randint(1, 100)

        print('Prime number: ', generated_key)
        choice = input('Press [X] to generate another number: ')

        if choice.lower() != 'x':
            break

    private_key_1 = random.randint(1, 100)
    private_key_2 = random.randint(1, 100)

    public_key_1 = __get_key(generated_key, private_key_1, prime_num)
    public_key_2 = __get_key(generated_key, private_key_2, prime_num)

    shared_secret_1 = __get_key(public_key_2, private_key_1, prime_num)
    shared_secret_2 = __get_key(public_key_1, private_key_2, prime_num)

    return [shared_secret_1, shared_secret_2]


def run():
    shared_secret_1, shared_secret_2 = __get_secret()

    print(f'\nShared secret 1: {shared_secret_1}')
    print(f'Shared secret 2: {shared_secret_2}')
