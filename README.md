# WithBond EasyPost Carrier Integration

The carrier integration for WithBond on the EasyPost platform.

Carrier documentation can be found here: https://docs.withbond.io.

Showcased at the first ever 2020 EasyPost Hackathon! **Do not distribute.**

## Install

```bash
pip3 install -e ."[dev]"

cp .env.example .env
```

## Usage

### Start the API

```bash
python3 app.py
```

### Hit the API

**cURL**

```bash
./curl.sh
```

**Python**

```python
python3 test.py  
```

## Development

```bash
# Install dev dependencies
pip3 install -e ."[dev]"

# Lint the project
pylint withbond/*.py
```
