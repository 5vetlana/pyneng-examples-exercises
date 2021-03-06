import pytest
import task_21_1a
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists

# Checking that the test is called via pytest ... and not python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Tests should be called using this expression:\npytest {__file__}\n\n")


def test_functions_created():
    """
    Checking that the function has been created
    """
    check_function_exists(task_21_1a, "parse_output_to_dict")


def test_function_return_value():
    """
    Function check
    """
    correct_return_value = [
        {
            "address": "15.0.15.1",
            "intf": "FastEthernet0/0",
            "protocol": "up",
            "status": "up",
        },
        {
            "address": "10.0.12.1",
            "intf": "FastEthernet0/1",
            "protocol": "up",
            "status": "up",
        },
        {
            "address": "10.0.13.1",
            "intf": "FastEthernet0/2",
            "protocol": "up",
            "status": "up",
        },
        {
            "address": "unassigned",
            "intf": "FastEthernet0/3",
            "protocol": "up",
            "status": "up",
        },
        {"address": "10.1.1.1", "intf": "Loopback0", "protocol": "up", "status": "up"},
        {
            "address": "100.0.0.1",
            "intf": "Loopback100",
            "protocol": "up",
            "status": "up",
        },
    ]
    with open("output/sh_ip_int_br.txt") as f:
        sh_ip_int_br = f.read()
    template = "templates/sh_ip_int_br.template"

    return_value = task_21_1a.parse_output_to_dict(template, sh_ip_int_br)
    assert return_value != None, "The function returns None"
    assert (
        type(return_value) == list
    ), f"The function should return a list, instead it returns a {type(return_value).__name__}"
    assert (
        return_value == correct_return_value
    ), "Function returns wrong value"


def test_function_return_value_different_args():
    """
    Checking the function with different arguments
    """
    correct_return_value = [
        {
            "hostname": "R1_LONDON",
            "uptime": "1 day, 15 hours, 32 minutes",
            "version": "15.3(2)S1",
        }
    ]

    with open("output/sh_version.txt") as f:
        sh_version = f.read()
    template = "templates/sh_version.template"

    return_value = task_21_1a.parse_output_to_dict(template, sh_version)
    assert return_value != None, "The function returns None"
    assert (
        type(return_value) == list
    ), f"The function should return a list, instead it returns a {type(return_value).__name__}"
    assert (
        return_value == correct_return_value
    ), "Function returns wrong value"
