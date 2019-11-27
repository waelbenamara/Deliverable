from requests import Session
from bs4 import BeautifulSoup as bs
 
with Session() as s:
    site = s.get("http://moodle.medtech.tn/login/index.php")
    bs_content = bs(site.content, "html.parser")
    token = bs_content.find("input", {"name":"logintoken"})["value"]
    print(token)                                          
    login_data = {"username":"wael.benamara","password":"sy4R@6D@", "csrf_token":token}
    s.post("http://moodle.medtech.tn/login/index.php",login_data)
    home_page = s.get("http://moodle.medtech.tn/user/profile.php?id=1331")
    print(home_page.headers)
page_soup = bs(home_page.headers,'html.parser')
#containers=page_soup.findAll('div',{'class':'partbox'})
print(page_soup)