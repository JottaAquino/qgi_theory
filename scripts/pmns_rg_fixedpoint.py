#!/usr/bin/env python3
"""
Transparência do fluxo RG/MaxEnt para o kernel de overlap PMNS.
Este script NÃO ajusta parâmetros contínuos; ele demonstra a convergência
para o ponto fixo esperado (b=1/6) e expõe o workflow e métricas.

Saídas:
- CSV com iterações e erro
- Figura com convergência (erro vs iteração)
"""
import csv
import numpy as np
import click
import matplotlib.pyplot as plt

SEED = 13579

@click.command()
@click.option('--iters', default=200, type=int)
@click.option('--out', default='code/data/outputs/pmns_convergence.csv')
@click.option('--fig', default='paper/figures/pmns_convergence.pdf')
def main(iters, out, fig):
    rng = np.random.default_rng(SEED)
    # Exemplo didático: b_k converge para 1/6 via iteração de contrato
    b = rng.uniform(0.05, 0.25)
    target = 1.0/6.0
    hist = []
    for k in range(iters):
        # operador de contração (simulado), substitua pela dinâmica real do funcional
        b = 0.5*(b + target)
        err = abs(b - target)
        hist.append((k, b, err))
    with open(out, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['iter','b','abs_err'])
        w.writerows(hist)
    # figura
    its = [h[0] for h in hist]
    errs = [h[2] for h in hist]
    plt.figure()
    plt.semilogy(its, errs)
    plt.xlabel('iteração')
    plt.ylabel('|b - 1/6|')
    plt.title('Convergência do ponto fixo (ilustrativo)')
    plt.grid(True, ls=':')
    plt.tight_layout()
    plt.savefig(fig)
    print(f"Saved: {out}, {fig}")

if __name__ == '__main__':
    main()




