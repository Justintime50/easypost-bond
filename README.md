# EasyPost Bond Carrier Integration Hackathon Project

[![Build Status](https://github.com/Justintime50/easypost-bond/workflows/build/badge.svg)](https://github.com/Justintime50/easypost-bond/actions)

A proof of concept carrier integration for `Bond` on the EasyPost platform. Showcased at the first ever 2020 EasyPost Hackathon! This project provided a template that we later followed when EasyPost decided to integrate Bond on its platform. 

**NOTE:** This project was built during a Hackathon and lacks rigor and best practices. **Do not distribute.**

* Carrier documentation can be found here: https://docs.withbond.io.
* Additional Carrier Integration documentation notes can be found in the [DOCUMENTATION.md](DOCUMENTATION.md) file.

## Install

```bash
# Change your `.env` variables as needed including adding the API key
cp .env.example .env

# Install the project
make install
```

## Usage

Create, buy, retrieve, and refund shipments all from the example script along with retrieving tracker info by changing values and running the script.

```bash
venv/bin/python examples/requests_examples.py
```

## Development

```bash
# Start the Flask API
make run

# Lint the entire project
make lint

# Run unit tests
make test
```
