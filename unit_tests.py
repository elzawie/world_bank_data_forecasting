import unittest
from requests.exceptions import MissingSchema
from retrieval_funcs import create_world_bank_api_url_string, retrieve_url_content
from preprocessing_funcs import convert_bytes_to_unicode, extract_dates_and_values_from_json


class RetrievalFuncsTests(unittest.TestCase):

    def test_create_world_bank_api_url_valid(self):
        country_code = 'AFG'
        indicator_code = 'NY.GDP.MKTP.CN'
        valid_url = 'https://api.worldbank.org/v2/country/afg/indicator/NY.GDP.MKTP.CN?format=json'
        created_url = create_world_bank_api_url_string(country_code, indicator_code)
        self.assertEqual(created_url, valid_url)

    def test_create_world_bank_api_url_invalid_country_code_type(self):
        country_code = ['deu']
        indicator_code = 'NY.GDP.MKTP.CN'

        with self.assertRaises(AssertionError):
            create_world_bank_api_url_string(country_code, indicator_code)

    def test_create_world_bank_api_url_invalid_indicator_code_type(self):
        country_code = 'deu'
        indicator_code = ['NY.GDP.MKTP.CN']

        with self.assertRaises(AssertionError):
            create_world_bank_api_url_string(country_code, indicator_code)

    def test_retrieve_url_content_valid(self):
        url = 'https://api.worldbank.org/v2/country/afg/indicator/NY.GDP.MKTP.CN?format=json'
        content_first_50_chars = b'[{"page":1,"pages":2,"per_page":50,"total":60,"sou'
        content_retrieved_first_50_chars = retrieve_url_content(url)[:50]
        self.assertEqual(content_retrieved_first_50_chars, content_first_50_chars)

    def test_retrieve_url_content_no_protocol(self):
        url = '//api.worldbank.org/v2/country/deu/indicator/NY.GDP.MKTP.CN?format=json'
        with self.assertRaises(MissingSchema):
            retrieve_url_content(url)

    def test_retrieve_url_content_incorrect_protocol(self):
        url = 'htps//api.worldbank.org/v2/country/deu/indicator/NY.GDP.MKTP.CN?format=json'
        with self.assertRaises(MissingSchema):
            retrieve_url_content(url)


class PreprocessingFuncsTests(unittest.TestCase):

    def test_convert_bytes_to_unicode_valid(self):
        bytes_object = b'[{"message":[{"id":"120","key":"Invalid value","value":"The provided parameter value is not valid"}]}]'
        unicode = '[{"message":[{"id":"120","key":"Invalid value","value":"The provided parameter value is not valid"}]}]'
        decoded_bytes = convert_bytes_to_unicode(bytes_object)
        self.assertEqual(decoded_bytes, unicode)

    def test_convert_bytes_to_unicode_incorrect_input_type(self):
        incorrect_input = [{"message": [{"id": "120", "key": "Invalid value", "value": "The provided parameter value is not valid"}]}]
        with self.assertRaises(AssertionError):
            convert_bytes_to_unicode(incorrect_input)

    def test_extract_dates_and_values_from_json_valid(self):
        json_data = [{"page":1},[{"indicator":{"value":"GDP (current LCU)"},"date":"2019","value": 'null'}]]
        indicator_name = "GDP (current LCU)"
        dates = ["2019"]
        values = ['null']
        extracted_name, extracted_date, extracted_value = extract_dates_and_values_from_json(json_data)
        self.assertEqual(extracted_name, indicator_name)
        self.assertEqual(extracted_date, dates)
        self.assertEqual(extracted_value, values)

    def test_extract_dates_and_values_from_json_invalid_parameter(self):
        json_data = [{"message": [{"id": "120", "key": "Invalid value", "value": "The provided parameter value is not valid"}]}]
        with self.assertRaises(IndexError):
            extract_dates_and_values_from_json(json_data)


if __name__ == '__main__':
    unittest.main()
