# Auto Number [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github/rodukov)

Useful utility that allows you to generate cell phone numbers of all countries of the world

## Installing:

```bash
git clone https://github.com/rodukov/autonumber
cd autonumber
```

## Examples of use:

This example generates Polish numbers.

country_tag: this is the country code
operator_tag: operator code
max_length: number length (WITHOUT PLUS SIGN)
minimum: range beginning (optional, 0 by default)
maximum: end of range (optional, maximum default value)

```python
>>> from autonumber import autonumber
>>> numbers = autonumber.load(country_tag="48", operator_tag="532", max_length=11, minimum=0, maximum=25)
>>> print(numbers)
['+48532000000', '+48532000001', '+48532000002', '+48532000003', '+48532000004', '+48532000005', '+48532000006', '+48532000007', '+48532000008', '+48532000009', '+48532000010', '+48532000011', '+48532000012', '+48532000013', '+48532000014', '+48532000015', '+48532000016', '+48532000017', '+48532000018', '+48532000019', '+48532000020', '+48532000021', '+48532000022', '+48532000023', '+48532000024', '+48532000025']
```

## What programming languages and tools have I used?

[<img align="left" alt="Python" width="26px" src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" style="padding-right:10px;" />](https://github.com/rodukov)
[<img align="left" alt="Debian" width="26px" src="https://upload.wikimedia.org/wikipedia/commons/6/66/Openlogo-debianV2.svg" style="padding-right:10px;" />](https://github.com/rodukov)
[<img align="left" alt="GitHub" width="26px" src="https://user-images.githubusercontent.com/3369400/139447912-e0f43f33-6d9f-45f8-be46-2df5bbc91289.png" style="padding-right:10px;" />](https://github.com/rodukov)
