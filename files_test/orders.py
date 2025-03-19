# در حال حاضر ازین فایل برای تست استفاده میکنیم.
from packages.lib.store_lib import *

#  برای نمونه  ثبت یک سفارش جدید را بر عهده دارد
file_name = "json/orders.json"

# insert_product(file_name , 'sdfsdf','dsfdsf','dsf','gr',15400 , 10000)
product_id = 2
customer_id = 3
quantity = 200
total_price = 150000
order_date = "2025-02-26"
insert_order(file_name , customer_id , product_id , quantity , total_price , order_date)


# product  = get_product_by_id(product_id , file_name)
# print(product)
# product['price'] = 1200
# product['name_en'] = "test coffee"
# edit_product(product_id , file_name , product)
