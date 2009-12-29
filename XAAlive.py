import urllib2
from twitter import Api
from BeautifulSoup import BeautifulSoup

USERNAME = "enter_your_username"
PASSWORD = "enter_your_password"

def getGD():    
    page = urllib2.urlopen("http://www.axiaplus.gr/gd.htm").read()
    soup = BeautifulSoup(page)
    GD = soup.find("tr")
    deiktis = GD.td.nextSibling.string
    metavoli = GD.td.nextSibling.nextSibling.string
    with open("XAAlive-txt", "r") as fin:
        if fin.readline() == deiktis:
            msg = ""
            fin.close()
        else:
            fin.close()
            with open("XAAlive-txt", "w") as fout:
                msg = "%s (%s%s)" % (deiktis, metavoli, "%")
                fout.write(deiktis)
                fout.close()
    return msg

def post(username,password,message):
    if message:
        api = Api(username, password)
        api.PostUpdate(message)

if __name__ == "__main__":
    r = post(USERNAME, PASSWORD, getGD())
