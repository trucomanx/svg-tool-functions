#!/usr/bin/python3

import json
import numpy as np

def generate_integer_vars(
        vars_keys,
        var_min=0,
        var_max=10,
        seed=None
    ):

    rng = np.random.default_rng(seed)

    values = rng.integers(
        low=var_min,
        high=var_max + 1,
        size=len(vars_keys)
    )

    return {
        k: int(v)
        for k, v in zip(vars_keys, values)
    }


def generate_integer_system(
        vars_dict,
        coef_min=-2,
        coef_max=2,
        seed=None,
        max_tries=1000
    ):

    rng = np.random.default_rng(seed)

    vars_vector = np.array(list(vars_dict.values()), dtype=int)
    vars_keys = list(vars_dict.keys())

    n = len(vars_vector)

    # =====================================
    # GERA MATRIZ INVERTÍVEL
    # =====================================

    for _ in range(max_tries):

        A = rng.integers(
            low=coef_min,
            high=coef_max + 1,
            size=(n, n)
        )

        # rank completo
        if np.linalg.matrix_rank(A) == n:
            break

    else:
        raise ValueError(
            "Não foi possível gerar matriz invertível"
        )

    r = A @ vars_vector

    return {
        "matrix_operator": A.tolist(),
        "vector_result": r.tolist(),
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
