# WithBond EasyPost Carrier Integration

[![Build Status](https://github.com/Justintime50/withbond-easpost/workflows/build/badge.svg)](https://github.com/Justintime50/withbond-easpost/actions)

The carrier integration for WithBond on the EasyPost platform. Showcased at the first ever 2020 EasyPost Hackathon! This project stands as a proof of concept and template should EasyPost decide to integrate WithBond on their platform. Note it was built as a Hackathon project and lacks rigor and best practices. **Do not distribute.**

* Carrier documentation can be found here: https://docs.withbond.io.
* Additional Carrier Integration documentation notes can be found in the [DOCUMENTATION.md](DOCUMENTATION.md) file.

## Install

```bash
make install
```

Change your `.env` variables as needed including adding the API key.

## Usage

### Start the API Server

```bash
# Run the dev service locally
make run
```

### Hit the API

```bash
venv/bin/python examples/requests_examples.py
```

## Development

```bash
# Lint the entire project
make lint

# Run unit tests
make test
```
