from .static_data import FLAT_RATE, SERVICE_LEVEL


def get_rates():
    rates = {
        "service": SERVICE_LEVEL,
        "rate": FLAT_RATE
    }

    return {"rates": rates}
