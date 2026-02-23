

"""
Calculate the output voltage magnitude and phase of an RC low-pass filter
"""

import cmath
import math


def calculate_circuit_output(f):
    """
    Calculate the output voltage magnitude and phase of an RC low-pass filter
    given an input frequency f in Hz.
    Returns: vout_mag: output voltage magnitude in Volts
             vout_phase: output voltage phase in radians
    """

    # Calculate input
    w = 2 * math.pi * f  # rad/s
    v_in = 5 * cmath.exp(1j * w)

    # Define the circuit
    z1 = 1  # kOhm
    c = 1e-9  # Farads
    z2 = 1 / (1j * w * c)
    v_out = (z2 * v_in) / (z1 + z2)  # Volts

    # Calculate magnitude and phase
    vout_mag = abs(v_out)
    vout_phase = cmath.phase(v_out)

    return vout_mag, vout_phase


def display_results(vout_mag, vout_phase):
    """Display the output voltage magnitude and phase using an f string"""
    print(f"Output voltage magnitude: {vout_mag} V")
    print(f"Output voltage phase: {vout_phase} radians")


if __name__ == "__main__":
    f = input("Enter frequency in Hz: ")  # remember f will be a string
    vout_mag, vout_phase = calculate_circuit_output(float(f))
    display_results(vout_mag, vout_phase)