import requests


class JiraSite(object):
    def __init__(self, jira_url: str, jira_username: str, jira_password: str, debug_mode: bool = False,
                 jira_destination: str = None):
        self.jira_destination = jira_destination
        self.debug_mode = debug_mode
        self.jira_url = jira_url.rstrip('/')
        self.jira_username = jira_username
        self.jira_password = jira_password
        self.session = requests.session()

        try:
            self.login()
        except Exception as ex:
            print(ex)
            pass

    def run(self):
        self.session.request(method="GET", url=f'{self.jira_url}/{self.jira_destination}')

    def login(self):
        url = f"{self.jira_url}/login.jsp"

        payload = f'atl_token=&login=Log%20In&os_destination={self.jira_destination}&os_password={self.jira_password}&os_username={self.jira_username}&user_role='
        headers = {
            'Origin': f'{self.jira_url}',
            'Upgrade-Insecure-Requests': '1',
            'DNT': '1',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
            'Sec-Fetch-User': '?1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
        }

        response = self.session.request("POST", url, headers=headers, data=payload)
        if self.debug_mode:
            print(response.text.encode('utf8'))
        # if response.status_code != 302:
        #     raise AuthenticationException()
