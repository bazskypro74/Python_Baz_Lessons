from yougileapi import Yougile_CompanyApi

api = Yougile_CompanyApi("https://ru.yougile.com/api-v2")


def test_company_list():
    auth = {
        "login" : "bazskypro74@gmail.com",
        "password" : "258369zaq@",
        "company_name" : ""
        }

    # login = "bazskypro74@gmail.com"
    # password = "258369zaq@"
    # company_name =""

    comp = api.get_company_list(auth)
    result = len(comp)
    assert result > 0
