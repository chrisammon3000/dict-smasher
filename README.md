# dict-smasher

`dict-smasher` is a Python library for for flattening nested dictionaries. It can flatten keys that contain nested dictionaries and lists of dictionaries.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dict-smasher.

```bash
pip install -i https://test.pypi.org/simple/ dict-smasher==0.0.1
```

## Usage

```python
from dict_smasher import dict_smasher, dict_write, select_keys

dict_smasher(nested_dict) # flattens dictionary
select_keys(nested_dict, keys) # select specific keys
dict_write(nested_dict, header, path) # output csv file
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)