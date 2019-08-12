from tableau.client.requests.base_request import BaseRequest


class UpdateWorkbookNowRequest(BaseRequest):
    """
    Update workbook now request for sending API requests to Tableau Server.

    :param ts_connection:       The Tableau Server connection object.
    :type ts_connection:        class
    """
    def __init__(self,
                 ts_connection):
        super().__init__(ts_connection)

    @property
    def base_update_workbook_now_request(self):
        return self._request_body

    def get_request(self):
        return self.base_update_workbook_now_request
