import pytest
import requests

from requests.exceptions import RequestException

from tests.test_vars import *


def service_available():
    try:
        requests.get(BASE_URL)
        return True
    except RequestException:
        return False


@pytest.mark.skipif(service_available() is False, reason='Service unavailable')
class TestRecordsAPI:
    # =============================================
    # ================== Fixtures =================

    def _post_record(self, **kwargs):
        return requests.post(RECORDS_URL, json=kwargs)

    # =============================================
    # ============ Positive test cases ============

    def test_api_return_records_list(self):
        resp = requests.get(RECORDS_URL)
        assert 'results' in resp.json(), f'Response does not contain records list'

    @pytest.mark.skip
    def test_api_create_records(self):
        resp = self._post_record(record='Test', list=f'{LIST_URL}1/')
        assert resp.status_code == 201, f'Record was not created. Response Code={resp.status_code}'

    def test_api_returns_record(self):
        resp = requests.get(f'{RECORDS_URL}5/')
        assert resp.status_code == 200, f'Request does not return record. Response Code={resp.status_code}'

    def test_record_contain_required_fields(self):
        req_fields = ['url', 'record', 'list']
        resp_body = requests.get(f'{RECORDS_URL}5/').json()
        assert all(fld in resp_body for fld in req_fields), \
            f'Record does not contain all required fields.\n Required: {req_fields}.\n Actual: {resp_body.keys()}'

    # =============================================
    # ============ Negative test cases ============

    def test_api_send_errors_on_empty_post_body(self):
        resp_body = self._post_record().json()
        assert resp_body['record'] == [REQUIRED_FIELD_ERROR]
        assert resp_body['list'] == [REQUIRED_FIELD_ERROR]

    def test_api_send_errors_on_empty_post_values(self):
        resp_body = self._post_record(record='', list='').json()
        assert resp_body['record'] == [BLANK_FIELD_ERROR]
        assert resp_body['list'] == [NULL_FIELD_ERROR]

    def test_api_send_errors_on_not_existing_list(self):
        resp_body = self._post_record(list=f'{LIST_URL}not_exist/').json()
        assert resp_body['list'] == [NOT_EXIST_ERROR]
