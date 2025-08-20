def ohms_law(voltage, resistance):
    """
    Calculate current using Ohm's Law.

    Parameters:
    voltage (float): Voltage in volts.
    resistance (float): Resistance in ohms.

    Returns:
    float: Current in amperes.
    """
    if resistance == 0:
        raise ValueError("Resistance cannot be zero.")
    
    return voltage / resistance

def power_calculation(voltage, current):
    """
    Calculate power using the formula P = V * I.

    Parameters:
    voltage (float): Voltage in volts.
    current (float): Current in amperes.

    Returns:
    float: Power in watts.
    """
    return voltage * current

def voltage_divider(input_voltage, r1, r2):
    """
    Calculate output voltage in a voltage divider circuit.

    Parameters:
    input_voltage (float): Input voltage in volts.
    r1 (float): Resistance of the first resistor in ohms.
    r2 (float): Resistance of the second resistor in ohms.

    Returns:
    float: Output voltage across r2 in volts.
    """
    if r1 + r2 == 0:
        raise ValueError("The sum of resistances cannot be zero.")
    
    return input_voltage * (r2 / (r1 + r2))

def rc_time_constant(resistance, capacitance):
    """
    Calculate the time constant of an RC circuit.

    Parameters:
    resistance (float): Resistance in ohms.
    capacitance (float): Capacitance in farads.

    Returns:
    float: Time constant in seconds.
    """
    if resistance < 0 or capacitance < 0:
        raise ValueError("Resistance and capacitance must be non-negative.")
    
    return resistance * capacitance

def series_resistance(resistances):
    """
    Calculate total resistance in a series circuit.

    Parameters:
    resistances (list of float): List of resistances in ohms.

    Returns:
    float: Total resistance in ohms.
    """
    if not resistances:
        raise ValueError("List of resistances cannot be empty.")
    
    return sum(resistances)

def parallel_resistance(resistances):
    """
    Calculate total resistance in a parallel circuit.

    Parameters:
    resistances (list of float): List of resistances in ohms.

    Returns:
    float: Total resistance in ohms.
    """
    if not resistances:
        raise ValueError("List of resistances cannot be empty.")
    
    if any(r <= 0 for r in resistances):
        raise ValueError("All resistances must be positive.")
    
    reciprocal_sum = sum(1 / r for r in resistances)
    
    if reciprocal_sum == 0:
        raise ValueError("Total resistance cannot be zero.")
    
    return 1 / reciprocal_sum