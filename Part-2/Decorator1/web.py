from login import login_req

def home_page(name,status):
    print("Home Page")
@login_req
def order_page(name,status):
    print("Order details")
@login_req
def update_profile(name,status):
    print("Updating Profile")

def contact_page(name,status):
    print("Contact US Page")

home_page('RG',False)
order_page('RG',False)
update_profile('RG',False)
contact_page('RG',True)