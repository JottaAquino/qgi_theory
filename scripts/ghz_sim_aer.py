#!/usr/bin/env python3
import json, csv, math, random
import click
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import numpy as np
import matplotlib.pyplot as plt

SEED = 424242
random.seed(SEED)
np.random.seed(SEED)

def ghz_circuit(n: int) -> QuantumCircuit:
    qc = QuantumCircuit(n, n)
    qc.h(0)
    for i in range(n-1):
        qc.cx(i, i+1)
    qc.measure(range(n), range(n))
    return qc

@click.command()
@click.option('--shots', default=16384, type=int)
@click.option('--qubits', multiple=True, type=int, default=[3,5,7])
@click.option('-o', '--output', default='code/data/outputs/ghz_results.csv')
def main(shots, qubits, output):
    sim = AerSimulator()
    rows = []
    for n in qubits:
        qc = ghz_circuit(n)
        result = sim.run(qc, shots=shots, seed_simulator=SEED).result()
        counts = result.get_counts()
        # Expect GHZ: peaks at all-0 and all-1
        # Estimate <ZZ> as 1.0 in ideal limit; we record empirical proxy per pair
        bitstrings = list(counts.keys())
        probs = {b: counts[b]/shots for b in bitstrings}
        # Build simple ZZ proxy over nearest neighbors
        zz_vals = []
        for b, p in probs.items():
            z = np.array([1 if bit=='0' else -1 for bit in b])
            pair = np.prod(z)  # product over all, equals +1 for all-0/all-1
            zz_vals.append(pair * p)
        zz = float(np.sum(zz_vals))
        rows.append({'n': n, 'shots': shots, 'zz_proxy': f"{zz:.6f}"})
    # Save CSV
    with open(output, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['n','shots','zz_proxy'])
        w.writeheader()
        w.writerows(rows)
    # Quick figure
    plt.figure()
    ns = [r['n'] for r in rows]
    vals = [float(r['zz_proxy']) for r in rows]
    plt.plot(ns, vals, marker='o')
    plt.xlabel('qubits (n)')
    plt.ylabel('<ZZ> proxy')
    plt.title('GHZ (Aer, ideal) — <ZZ> proxy vs n')
    plt.grid(True, ls=':')
    plt.tight_layout()
    plt.savefig('paper/figures/ghz_correlations.pdf')
    print(f"Saved: {output} and paper/figures/ghz_correlations.pdf")

if __name__ == '__main__':
    main()




