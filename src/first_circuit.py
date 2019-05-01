# first test with Google Cirq for Python
"""
Creation of quantum circuit as shown below for Noisy Intermediate-Scale Quantum (NISQ) quantum computers:

(0, 1): ───────────────H───@───────H───
                           │
(0, 2): ───H───@───H───H───@───@───H───
               │               │
(0, 3): ───────@───────H───────@───H───
               │
(1, 0): ───────X───────────────────────
"""

import cirq


def build_4qbits_circuit():
    num_qbits = 4

    qbits = [cirq.GridQubit(x,y) for x in range (num_qbits) for y in range(num_qbits)]
    print(qbits)

    circuit = cirq.Circuit()

    # all gates applied to the circuit
    h1 = cirq.H(qbits[2])
    toffoli = cirq.TOFFOLI(qbits[2], qbits[3], qbits[4])
    h2 = cirq.H(qbits[1])
    h3 = cirq.H(qbits[2])
    h4 = cirq.H(qbits[3])
    cz1 = cirq.CZ(qbits[2], qbits[1])
    cz2 = cirq.CZ(qbits[2], qbits[3])

     # moments of gates to apply on circuit
    moment1 = cirq.Moment([h1])
    moment2 = cirq.Moment([toffoli])
    moment3 = cirq.Moment([h1])
    moment4 = cirq.Moment([h2, h3, h4])
    moment5 = cirq.Moment([cz1])
    moment6 = cirq.Moment([cz2])
    moment7 = cirq.Moment([h2, h3, h4])

    circuit = cirq.Circuit((moment1, moment2, moment3, moment4, moment5, moment6, moment7))

    print(circuit)

    return circuit


def simulate(circuit):
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=3)
    print(result)


if __name__ == "__main__":
    circuit_4q = build_4qbits_circuit()
    simulate(circuit_4q)