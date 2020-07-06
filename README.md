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

Replace `123...` with the API key:

```bash
./curl.sh 123...
```

**Python**

```python
import os
from dotenv import load_dotenv
import withbond

load_dotenv()
API_KEY = os.getenv('API_KEY')

CUSTOMER = withbond.Shipment.create(
	data={
		'api_key': API_KEY,
        'test': 'lala,
        # TODO
	}
)
```

## Development

```bash
# TODO
```
