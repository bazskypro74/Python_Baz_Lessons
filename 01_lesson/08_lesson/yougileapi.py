import requests


class Yougile_Api:

    def __init__(self, url):
        self.url = url

    def get_company_list(self, login, password, name=""):

        json_date = {
            "login": login,
            "password": password,
            "name": name
        }
        headers = {'Content-Type': 'application/json'}
        query = "limit=50&offset=0"
        url = f"{self.url}/auth/companies?{query}"
        resp = requests.post(url, json=json_date, headers=headers)
        comp = resp.json()['content'][0]
        data = resp.json()['content'][1]['id']
        return comp, data

    def get_token_company(self, login, password, companyID):

        payload = {
            "login": login,
            "password": password,
            "companyID": companyID
            }
        headers = {"Content-Type": "application/json"}
        url = f"{self.url}/auth/keys/get"
        response = requests.post(url, json=payload, headers=headers)
        result = response.json()
        res_status = response.status_code
        return result, res_status

    def create_project_company(self, title, users, token):
        self.auth = token

        json_date = {
            "title": title,
            "users": users
        }
        author = f"Bearer {self.auth}"
        url = f"{self.url}/projects/"
        headers = {'Authorization': author, 'Content-Type': 'application/json'}
        resp = requests.post(url, json=json_date, headers=headers)
        result = resp.json()
        return result

    def update_projects_company(
            self, deleted, title, users, id_projects, token):

        self.auth = token
        self.id = id_projects
        json_date = {
            "deleted": deleted,
            "title": title,
            "users": users
         }
        author = f"Bearer {self.auth}"
        url = f"{self.url}/projects/{self.id}"
        headers = {'Authorization': author, 'Content-Type': 'application/json'}
        resp = requests.put(url, json=json_date, headers=headers)
        result = resp.json()
        return result

    def get_projects_id(self, id_projects, token):

        self.auth = token
        self.id = id_projects
        author = f"Bearer {self.auth}"
        url = f"{self.url}/projects/{self.id}"
        headers = {'Authorization': author, 'Content-Type': 'application/json'}
        resp = requests.get(url, headers=headers)
        result = resp.json()
        return result
