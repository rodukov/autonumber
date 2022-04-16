# Auto Number [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github/rodukov) [<img src="https://img.shields.io/badge/powerful-generator-FF3939"/>](https://github.com/rodukov)

Useful utility that allows you to generate cell phone numbers of all countries of the world

## Installing:

```bash
git clone https://github.com/rodukov/autonumber
cd autonumber
```

## Examples of use:

This example generates Polish numbers.<br>
<br>
`country_tag` this is the country code<br>
`operator_tag` operator code<br>
`max_length` number length (WITHOUT PLUS SIGN)<br>
`minimum` range beginning (optional, 0 by default)<br>
`maximum` end of range (optional, maximum default value)<br>

```python
>>> from autonumber import autonumber
>>> numbers = autonumber.load(country_tag="48", operator_tag="532", max_length=11, minimum=0, maximum=25)
>>> print(numbers)
['+48532000000', '+48532000001', '+48532000002', '+48532000003', '+48532000004', '+48532000005', '+48532000006', '+48532000007', '+48532000008', '+48532000009', '+48532000010', '+48532000011', '+48532000012', '+48532000013', '+48532000014', '+48532000015', '+48532000016', '+48532000017', '+48532000018', '+48532000019', '+48532000020', '+48532000021', '+48532000022', '+48532000023', '+48532000024', '+48532000025']
```
