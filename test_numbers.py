def test_int(parse_toml_with_numbers):
    numbers_toml = parse_toml_with_numbers
    print(f'number1: {numbers_toml["parameters"]["number1"]}')
    print(f'number2: {numbers_toml["parameters"]["number2"]}')
    assert isinstance(numbers_toml["parameters"]["number1"], int)
    assert isinstance(numbers_toml["parameters"]["number2"], int)
