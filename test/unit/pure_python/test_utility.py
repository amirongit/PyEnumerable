from random import choice


def generate_random_args(length: int, range_: range) -> tuple[int, ...]:
    return tuple(choice(range_) for _ in range(length))

