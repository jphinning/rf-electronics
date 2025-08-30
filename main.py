import logging
from microstrip_lines import impedance


def main():
    logging.basicConfig(level=logging.INFO)

    er = 0.378
    w, h = 3.15, 1.5
    freq = 2.240e9

    z = impedance.z0(er, w, h)

    eeff = impedance.epsilon_eff(er, w, h)
    lq = impedance.quarter_wavelength(freq, eeff)

    print(f"Z0 = {z:.2f} Ω")
    print(f"ε_eff = {eeff:.3f}")
    print(f"Quarter wavelength at 1 GHz = {lq:.4f} m")


if __name__ == "__main__":
    main()
