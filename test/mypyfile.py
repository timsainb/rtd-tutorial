"""
test - testest
"""

__version__ = "0.1.0"


class test(Exception):
    """Raised if the kind is invalid."""
    pass


def testtestest(kind=None):
    """
    Return a list of random ingredients as strings.
    :param kind: Optional "kind" of ingredients.
    :type kind: list[str] or None
    :raise lumache.InvalidKindError: If the kind is invalid.
    :return: The ingredients list.
    :rtype: list[str]
    """
    return ["shells", "gorgonzola", "parsley"]
