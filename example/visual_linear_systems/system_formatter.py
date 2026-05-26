#!/usr/bin/python3

def transfor_system_to_format_1(system, coef_mode="expanded", add_unknowns=True, unknown='?'):

    A = system["matrix_operator"]
    r = system["vector_result"]
    vars_keys = system["vars_keys"]

    seqs = []

    # =====================================
    # EQUAÇÕES
    # =====================================

    for row, result in zip(A, r):

        seq = []

        first_term = True

        for coef, var in zip(row, vars_keys):

            if coef == 0:
                continue

            sign = "+" if coef > 0 else "-"
            abs_coef = abs(coef)

            # =====================================
            # COMPACT
            # =====================================

            if coef_mode == "compact":

                if first_term:

                    if coef < 0:
                        seq.append("-")

                else:
                    seq.append(sign)

                if abs_coef != 1:

                    for digit in str(abs_coef):
                        seq.append(digit)

                seq.append(var)

            # =====================================
            # EXPANDED
            # =====================================

            elif coef_mode == "expanded":

                for i in range(abs_coef):

                    # primeiro termo da equação
                    if first_term and i == 0:

                        if coef < 0:
                            seq.append("-")

                    else:
                        seq.append(sign)

                    seq.append(var)

            first_term = False

        # caso linha inteira seja zero
        if first_term:
            seq.append("0")

        # =========================
        # RESULTADO
        # =========================

        seq.append("=")

        result_str = str(result)

        if result < 0:
            seq.append("-")
            result_str = str(abs(result))

        for digit in result_str:
            seq.append(digit)

        seqs.append(seq)

    # =====================================
    # INCÓGNITAS
    # =====================================
    if add_unknowns:
        for var in vars_keys:

            seqs.append([var, "=", unknown])

    return seqs
    
    

    
