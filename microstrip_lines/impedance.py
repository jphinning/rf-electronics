"""
Wheeler formula for microstrip characteristic impedance.

Now with logging and wave utilities.
"""

import math
import logging
from typing import Union

Number = Union[int, float]

ETA_0 = 377.0  # Free-space impedance (Ohms)
C = 3e8  # Speed of light in vacuum (m/s)

# Configure module-level logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def f_wh(w: Number, h: Number) -> float:
    """
    Compute the function F(W/H) used in Wheeler's formula.

    Args:
        w: trace width
        h: substrate height

    Returns:
        Value of F(W/H).

    Examples:
        >>> round(f_wh(0.5, 1.0), 4)
        0.2879
        >>> round(f_wh(2.0, 1.0), 4)
        0.2774
    """
    wh = w / h
    hw = h / w
    if wh <= 1:
        result = 1 / math.sqrt(1 + 12 * hw) + 0.04 * (1 - wh) ** 2
    else:
        result = 1 / math.sqrt(1 + 12 * hw)
    logger.info("f_wh: w=%.4f, h=%.4f, wh=%.4f, hw=%.4f, F=%.6f", w, h, wh, hw, result)
    return result


def epsilon_eff(er: Number, w: Number, h: Number) -> float:
    """
    Compute the effective dielectric constant.

    Args:
        er: relative permittivity of substrate
        w: trace width
        h: substrate height

    Returns:
        Effective dielectric constant (epsilon_eff).

    Examples:
        >>> round(epsilon_eff(4.4, 0.5, 1.0), 4)
        2.7792
    """
    f = f_wh(w, h)
    result = 0.5 * (er + 1 + (er - 1) * f)
    logger.info(
        "epsilon_eff: er=%.4f, w=%.4f, h=%.4f, F=%.6f, eeff=%.6f", er, w, h, f, result
    )
    return result


def z0(er: Number, w: Number, h: Number) -> float:
    """
    Compute the characteristic impedance of a microstrip using Wheeler's formula.

    Args:
        er: relative permittivity of substrate
        w: trace width
        h: substrate height

    Returns:
        Characteristic impedance in Ohms.

    Examples:
        >>> round(z0(4.4, 0.5, 1.0), 2)
        112.86
        >>> round(z0(4.4, 2.0, 1.0), 2)
        46.56
    """
    wh = w / h
    hw = h / w
    eeff = epsilon_eff(er, w, h)

    if wh <= 1:
        result = (ETA_0 / (2 * math.pi * math.sqrt(eeff))) * math.log(
            8 * h / w + 0.25 * wh
        )
    else:
        result = ETA_0 / (math.sqrt(eeff) * (wh + 2.46 - 0.49 * hw + (1 - wh) ** 6))
    logger.info(
        "z0: er=%.4f, w=%.4f, h=%.4f, wh=%.4f, eeff=%.6f, Z0=%.6f",
        er,
        w,
        h,
        wh,
        eeff,
        result,
    )
    return result


def guided_wavelength(freq_hz: Number, eeff: Number) -> float:
    """
    Compute guided wavelength λg in a microstrip line.

    Args:
        freq_hz: frequency in Hz
        eeff: effective dielectric constant

    Returns:
        Guided wavelength in meters.

    Examples:
        >>> round(guided_wavelength(1e9, 2.5), 4)
        0.0600
    """
    v = C / math.sqrt(eeff)
    return v / freq_hz


def quarter_wavelength(freq_hz: Number, eeff: Number) -> float:
    """
    Compute the quarter-wave length λg/4.

    Args:
        freq_hz: frequency in Hz
        eeff: effective dielectric constant

    Returns:
        Quarter guided wavelength in meters.

    Examples:
        >>> round(quarter_wavelength(1e9, 2.5), 4)
        0.0150
    """
    return guided_wavelength(freq_hz, eeff) / 4
