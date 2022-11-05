import requests
from pprint import pprint

presidents = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Jackson", "Van Buren", "Harrison", "Tyler",
                  "Polk", "Taylor", "Fillmore", "Pierce", "Buchanan", "Lincoln", "Johnson", "Hayes", "Grant", "Garfield", "Arthur"
                ,"Cleveland", "Coolidge", "Taft", "Wilson", "Harding", "Hoover", "Roosevelt", "Truman", "Eisenhower", "Kennedy", "Nixon"
                  "Ford", "Carter", "Reagan", "Bush", "Clinton", "Obama", "Trump", "Biden"]


def test_ddg():
    resp = requests.get('https://api.duckduckgo.com/?q=presidents+of+the+united+states&format=json')
    rsp_data = resp.json()
    assert "Presidents" in rsp_data["Heading"]
    pprint(resp.json())


test_ddg()

