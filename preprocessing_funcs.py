def convert_bytes_to_unicode(bytes_object):
    """Function used to convert bytes object representing JSON into a JSON string

    Arguments:
        bytes_object {[bytes]} -- bytes object representing data

    Returns:
        [str] -- string representing JSON content
    """
    assert isinstance(bytes_object, bytes), "bytes_object must have bytes type"

    return bytes_object.decode('utf8').replace("'", '"')


def extract_dates_and_values_from_json(json_data):
    """Function used to extract indicator name, dates and values from the JSON
    returned by the World Bank API

    Arguments:
        json_data {[list]} -- json array returned by the World Bank API
    """
    assert isinstance(json_data, list), "json_data must be a list"

    try:
        _, metadata = json_data[0], json_data[1]
        indicator_name = [observation['indicator']['value'] for observation in metadata[0:1]].pop()
        dates = [observation['date'] for observation in metadata]
        values = [observation['value'] for observation in metadata]
        return indicator_name, dates, values
    except IndexError:
        msg = json_data[0]['message'][0]['value']
        raise IndexError(f'{msg}. Please make sure that country and indicator codes are correct')
