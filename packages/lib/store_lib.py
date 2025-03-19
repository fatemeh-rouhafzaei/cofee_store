import json
def read_json(file_name):
    # Opening JSON file
    with open(file_name, 'r' , encoding= 'utf-8') as openfile:
        # Reading from json file
        return json.load(openfile)

def write_json(file_name, data):
    with open(file_name, "w", encoding= 'utf-8') as outfile:
        json.dump(data, outfile,ensure_ascii=False, indent= 4)
# customers email list:
def customers_email(customers):
    customers_email_list = []
    for item in customers:
        customers_email_list.append(item['email'])
    return customers_email_list

def insert_customer(file_name , name , email , phone):
    customers_list = read_json(file_name)
    last_customer = customers_list[-1]
    new_customer_id = last_customer['id'] + 1
    new_customer = {
      "id": new_customer_id,
      "name": name,
      "email": email,
      "phone": phone
    }
    customers_list.append(new_customer)
    write_json(file_name , customers_list)
    
def get_customer_by_id(customer_id , file_name):
    # دریافت محصولات فعلی
    customers_list = read_json(file_name)
    for customer in customers_list:
        for key , value in customer.items():
            if ((key == "id") & (value == customer_id)):
                return customer

def edit_customer(customer_id , file_name , customer_properties):
    customers_list = read_json(file_name)
    for customer in customers_list:
        for key , value in customer.items():
            if ((key == "id") & (value == customer_id)):
                customer['name']  = customer_properties['name']  
                customer['email']  = customer_properties['email']  
                customer['phone']  = customer_properties['phone']  
    write_json(file_name , customers_list)


def product_names(products):
    product_names_list = []
    for product in products:
        product_names_list.append(product['name_en'])
    return product_names_list

def insert_product(file_name , name_fa , name_en , unit_fa, unit_en, price, stock):
    # دریافت محصولات فعلی
    # file_name = "json/products.json"
    products_list = read_json(file_name)
    # دریافت آخرین محصول موجود
    last_product = products_list[-1]
    # ایجاد آی دی برای محصول جدید بر اساس آی دی آخرین محصول
    new_product_id = last_product['id'] + 1
    # ایجاد محصول جدید با استفاده از داده ورودی و قابل موجود در فایل جیسون
    new_product = {
        "id": new_product_id,
        "name_fa": name_fa,
        "name_en": name_en,
        "unit_fa": unit_fa,
        "unit_en": unit_en,
        "price": price,
        "stock": stock
    }
    # اضافه کردن محصول جدید به لیست محصولات واکشی شده از فایل جیسون
    products_list.append(new_product)

    # جایگزین لیست محصولات جدید با لیست محصولات قبلی در فایل جیسون
    write_json(file_name , products_list)

def remove_product(product_id , file_name):
    products_list = read_json(file_name)
    products_len = len(products_list)
    for product in products_list:
        for key , value in product.items():
            if ((key == "id") & (value == product_id)):
                product_index =  products_list.index(product)
                products_list.pop(product_index)
            else:
                return "not_found"
    if len(products_list) == products_len - 1:
        write_json(file_name , products_list)
        return "success"
    else:
        return "failed"

def get_product_by_id(product_id , file_name):
    # دریافت محصولات فعلی
    products_list = read_json(file_name)
    for product in products_list:
        for key , value in product.items():
            if ((key == "id") & (value == product_id)):
                return product

def edit_product(product_id , file_name , product_properties):
    products_list = read_json(file_name)
    for product in products_list:
        for key , value in product.items():
            if ((key == "id") & (value == product_id)):
                product['name_fa']  = product_properties['name_fa']  
                product['name_en']  = product_properties['name_en']  
                product['unit_fa']  = product_properties['unit_fa']  
                product['unit_en']  = product_properties['unit_en']  
                product['price']  = product_properties['price']  
                product['stock']  = product_properties['stock']

    write_json(file_name , products_list)

def insert_order(file_name , customer_id , product_id , quantity , total_price , order_date):

    
    orders_list = read_json(file_name)
    last_order = orders_list[-1]
    new_order_id = last_order['id'] + 1
    new_order = {
      "id": new_order_id,
      "customer_id": customer_id,
      "product_id": product_id,
      "quantity": quantity,
      "total_price": total_price,
      "order_date": order_date,
    }
    orders_list.append(new_order)
    write_json(file_name , orders_list)
