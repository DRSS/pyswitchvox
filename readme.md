## Synopsis

Pyswitchvox is a simple python library for initiating calls in a switchvox system from python.

## Code Example

```python
import pyswitchvox
myvox = Switchvox('user', 'password', 'server')
response = myvox.call(900,902)
response.json()

```

## Motivation

A quick and simple way to start calls from a python application.  We use pyswitchvox in our django application to start sales calls from sales reps to customers.

## Installation

`pip install pyswitchvox`


## Tests

Run `nosetests` to run tests.

## Contributors

Stephen Castle

## License

MIT