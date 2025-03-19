# در حال حاضر ازین فایل برای تست استفاده میکنیم.
from packages.lib.store_lib import *
customer_file = "json/customers.json"
insert_customer(customer_file , "Iman" , "iman@sample.com" , "032165487")
customer_properties = {
        "id": 4,
        "name": "Iman ali",
        "email": "iman4@sample.com",
        "phone": "032165487"
    }
customer_id = 4
customer_properties = get_customer_by_id(customer_id, customer_file)
customer_properties['email'] = "info@iman.com"
edit_customer(4 , customer_file , customer_properties)