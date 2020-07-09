# WithBond EasyPost Carrier Integration

The carrier integration for WithBond on the EasyPost platform.

Carrier documentation can be found here: https://docs.withbond.io.
Carrier Integration documentation can be found [here](https://docs.google.com/document/d/1yzQqW2oj7JBHL12wsprN1LAu19u9qyUFtLGHWSLWAXE/edit#heading=h.plemo0ol8nvx).
Additional Carrier Integration documentation notes can be found in the [DOCUMENTATION.md](DOCUMENTATION.md) file.

Showcased at the first ever 2020 EasyPost Hackathon! **Do not distribute.**

## Install

```bash
pip3 install -e ."[dev]"

cp .env.example .env
```

## Usage

### Start the API

```bash
# Barebones
python3 app.py

# Docker
docker-compose up -d
```

### Hit the API

**cURL**

```bash
./create.sh
```

**Python**

```python
python3 create_shipment.py  
```

## Development

```bash
# Install dev dependencies
pip3 install -e ."[dev]"

# Lint the project
pylint withbond/*.py
```
