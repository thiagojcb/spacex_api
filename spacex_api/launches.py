"""Functions to retrieve launches information."""
from ._helpers._api import _get

def get_launches(method="", **query):
    """Get launches based on query strings.

        Get launches based on query strings from
        the API.

    Parameters
    ----------
        method : str (optional)
            the method used for the request.
        query : keyword args
            keyword args based on the API query strings.
    Returns
    -------
        list
            a list of the launches.
    """
    return _get("launches", method, query)
