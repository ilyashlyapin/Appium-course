import pytest


def test_validate_titles():
    expected_title = "Google.com"
    actual_title = "Gmail.com"
    title = "This is Gmail website"

    # if actual_title == expected_title:
    #     print("Test case pass")
    # else:
    #     print("Test case fail")

    print("Beginning")
    assert expected_title == actual_title, "Titles are not matching"
    assert "Gmails" in title, "Gmail does not exists in the title"
    assert False, "forcefully failing the test"
    print("Ending")


"""
To enable soft assertion we need to install pip install pytest-soft-assertions
and then run pytest FILENAME -s -v --soft-asserts    
"""
