# در حال حاضر ازین فایل برای تست استفاده میکنیم.
from packages.lib.store_lib import *

#  برای نمونه در تابع زیر کار ثبت یک محصول جدید را بر عهده دارد
file_name = "json/products.json"

insert_product(file_name , 'ppp','ooo','www','gr',12200 , 10000)
# product_id = 4
# product  = get_product_by_id(product_id , file_name)
# print(product)
# product['price'] = 1200
# product['name_en'] = "test coffee"
# edit_product(product_id , file_name , product)

# result = remove_product(product_id , file_name)
# print(result)
# if result == "success":
#     message_text = f"a product with id: {product_id} deleted"
#     message_type = "info"
    
#     # print(f"a product with id: {product_id} deleted") 
# elif result == "not_found":
#     # print(f"product not found")
#     message_text = f"product not found"
#     message_type = "warning"

# else:
#     # print(f"product removing failed.")
#     message_text = f"product removing failed."
#     message_type = "danger"

# show_message(message_text , message_type)
