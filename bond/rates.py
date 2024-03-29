from bond.static_data import FLAT_RATE, SERVICE_LEVEL


def get_rates():
    """Get the bond rates and services
    """
    rates = {
        'service': SERVICE_LEVEL,
        'rate': FLAT_RATE
    }

    return {'rates': rates}
