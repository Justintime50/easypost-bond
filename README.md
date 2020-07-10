# WithBond EasyPost Carrier Integration

The carrier integration for WithBond on the EasyPost platform. Showcased at the first ever 2020 EasyPost Hackathon! **Do not distribute.**

* Carrier documentation can be found here: https://docs.withbond.io.
* Additional Carrier Integration documentation notes can be found in the [DOCUMENTATION.md](DOCUMENTATION.md) file.

## Install

```bash
make install
```

Change your `.env` variables as needed.

## Usage

### Start the API Server

```bash
# Run the dev service locally
make run

# Run the prod service in Docker
make docker
```

### Hit the API

**Web Request via Python (recommended)**

```bash
python3 requests_examples.py
```

**Python (like a client library)**

```python
python3 create_shipment.py  
```

**cURL (deprecated)**

```bash
./create.sh
```

## Development

Ensure you've installed the project first:

```bash
# Lint the entire project
make lint
```
