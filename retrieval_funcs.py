import requests


def create_world_bank_api_url_string(country_code, indicator_code, output_format="json"):
    """Function used to create the World Bank API query string used to retrieve the time series

    Arguments:
        country_code {[str]} -- string representing country code
        indicator_code {[str]} -- string representing economic indicator

    Keyword Arguments:
        output_format {str} -- format in which data has to be returned. Accepted values include:
                               'xml' and 'json' (default: {"json"})

    Returns:
        [str] -- string representing the API query string
    """
    assert isinstance(country_code, str), "country_code must be a string"
    assert isinstance(indicator_code, str), "indicator_code must be a string"
    assert isinstance(output_format, str), "indicator_code must be a string"

    return f"https://api.worldbank.org/v2/country/{country_code.lower()}/indicator/{indicator_code.upper()}?format={output_format.lower()}"


def retrieve_url_content(url):
    """Function used to retrieve the content of the provided URL

    Arguments:
        url {[str]} -- string representing URL which content has to be retrieved

    Returns:
        [bytes] -- [description]
    """
    assert isinstance(url, str), "url must be a string"
    return requests.get(url).content
