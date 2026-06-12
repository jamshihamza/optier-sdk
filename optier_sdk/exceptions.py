"""
OPTIER SDK Exception Definitions.

IMPORTANT:

This file is intentionally minimal during the early
development stages.

Exception classes will be added only after they have
been reviewed against the OEM documentation and mapped
inside docs/sdk/exception_mapping.md.
"""


class OptierError(Exception):
    """
    Base exception for the entire OPTIER SDK.
    """

    pass