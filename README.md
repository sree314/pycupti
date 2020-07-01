# pycupti

Provides a Python3 interface to the CUDA CUPTI library. It is
incomplete.

## Installation

Clone this repository. Then run:

```
python3 setup.py develop --user

```

I recommend `develop` instead of `install` since pycupti is unstable
software.

`pycupti` requires `pycuda` and will install it automatically when you
run the above command.

`pycupti` can be used "offline" when there is no CUPTI library
installed, in that case, the API calls will not work (and
`pycupti.api` will be missing, but `pycupti.constants` will still be
available).

## Usage

`pycupti` is a very thin wrapper around the CUPTI API. If you know how
to use CUPTI, you know how to use `pycupti`.

For full-fledged examples of how to use this API, see the `gen_all_metrics.py` and `gen_all_events.py` scripts in the [`npreader2` repository](https://github.com/sree314/npreader2/)

