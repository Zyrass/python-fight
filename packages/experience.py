#!/usr/bin/env python3

class Experience:
    @staticmethod
    def creation_table_experience(debut_exp, fin_exp, num_niveau):
        exp_table = [0]
        for i in range(1, num_niveau + 1):
            exp_suivant = int(debut_exp * ((fin_exp / debut_exp) ** (i / (num_niveau - 1))))
            exp_table.append(exp_suivant)
        return exp_table
