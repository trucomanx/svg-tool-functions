#!/usr/bin/python3

import json
import numpy as np


def generate_integer_system(vars_dict, coef_min=0, coef_max=2, seed=None):

    rng = np.random.default_rng(seed)

    vars_vector = np.array(list(vars_dict.values()), dtype=int)
    vars_keys = list(vars_dict.keys())

    n = len(vars_vector)

    A = rng.integers(
        low=coef_min,
        high=coef_max + 1,
        size=(n, n)
    )

    r = A @ vars_vector

    return {
        "matrix_operator": A.tolist(),   # matriz -> lista de listas
        "vector_result": r.tolist(),     # vetor -> lista
        "vars_values": vars_vector.tolist(),
        "vars_keys": vars_keys
    }


if __name__ == "__main__":

    vars_dict = {"x": 2, "y": 1, "z": 3}

    res = generate_integer_system(vars_dict, 0, 2, seed=42)

    # salvar em json
    with open("system.json", "w") as f:
        json.dump(res, f, indent=4)

    # carregar de volta
    with open("system.json", "r") as f:
        loaded = json.load(f)

    print(loaded)
