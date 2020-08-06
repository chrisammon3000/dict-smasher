[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

# dict-smasher

`dict-smasher` is a Python library for for flattening nested dictionaries. It can flatten keys that contain nested dictionaries and lists of dictionaries.

#### -- Project Status: [Active]

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
Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Authors
* **Gregory Lindsey** - [abk7777](https://github.com/abk7777)

## License
[MIT](https://choosealicense.com/licenses/mit/)


[contributors-shield]: https://img.shields.io/github/contributors/abk7777/dict-smasher.svg?style=flat-square
[contributors-url]: https://github.com/abk7777/dict-smasher/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/abk7777/dict-smasher.svg?style=flat-square
[forks-url]: https://github.com/abk7777/dict-smasher/network/members
[stars-shield]: https://img.shields.io/github/stars/abk7777/dict-smasher.svg?style=flat-square
[stars-url]: https://github.com/abk7777/dict-smasher/stargazers
[issues-shield]: https://img.shields.io/github/issues/abk7777/dict-smasher.svg?style=flat-square
[issues-url]: https://github.com/abk7777/dict-smasher/issues
[license-shield]: https://img.shields.io/github/license/abk7777/dict-smasher.svg?style=flat-square
[license-url]: https://github.com/abk7777/dict-smasher/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/gregory-lindsey/