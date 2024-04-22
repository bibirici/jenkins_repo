import toml
import pytest


def pytest_addoption(parser):
    parser.addoption("--str_toml", action="store", required=False, help="path for strings file.")
    parser.addoption("--int_toml", action="store", required=False, help="path for numbers file.")


@pytest.fixture
def parse_toml_with_strings(request):
    toml_str_file = request.config.getoption("--str_toml")
    with open(toml_str_file, "r") as f:
        parsed_str_toml = toml.load(f)
    return parsed_str_toml


@pytest.fixture
def parse_toml_with_numbers(request):
    toml_int_file = request.config.getoption("--int_toml")
    with open(toml_int_file, "r") as f:
        parsed_int_toml = toml.load(f)
    return parsed_int_toml
