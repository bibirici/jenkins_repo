def test_string(parse_toml_with_strings):
    strings_toml = parse_toml_with_strings
    print(f'string1: {strings_toml["parameters"]["string1"]}')
    print(f'string2: {strings_toml["parameters"]["string2"]}')
    assert isinstance(strings_toml["parameters"]["string1"], str)
    assert isinstance(strings_toml["parameters"]["string2"], str)
