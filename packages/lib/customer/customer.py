class customer(RWFiles):
    def __init__(self, file_name):
        super().__init__(file_name)

    def customer_names(self,customers):
        customer_names_list = []
        for customer in customers:
            customer_names_list.append(customer['email'])
        return customer_names_list

    def insert_customer(self, name , email , phone):
        # دریافت محصولات فعلی
        # file_name = "json/customers.json"
        customers_list = self.read_json()
        # دریافت آخرین محصول موجود
        last_customer = customers_list[-1]
        # ایجاد آی دی برای محصول جدید بر اساس آی دی آخرین محصول
        new_customer_id = last_customer['id'] + 1
        # ایجاد محصول جدید با استفاده از داده ورودی و قابل موجود در فایل جیسون
        new_customer = {
            "id": new_customer_id,
            "name": name,
            "email": email,
            "phone": phone,
        }
        # اضافه کردن محصول جدید به لیست محصولات واکشی شده از فایل جیسون
        customers_list.append(new_customer)

        # جایگزین لیست محصولات جدید با لیست محصولات قبلی در فایل جیسون
        self.write_json(customers_list)

    def remove_customer(self, customer_id):
        customers_list = self.read_json()
        customers_len = len(customers_list)
        for customer in customers_list:
            for key , value in customer.items():
                if ((key == "id") & (value == customer_id)):
                    customer_index =  customers_list.index(customer)
                    customers_list.pop(customer_index)
                else:
                    return "not_found"
        if len(customers_list) == customers_len - 1:
            self.write_json(customers_list)
            return "success"
        else:
            return "failed"

    def get_customer_by_id(self, customer_id):
        # دریافت محصولات فعلی
        customers_list = self.read_json()
        for customer in customers_list:
            for key , value in customer.items():
                if ((key == "id") & (value == customer_id)):
                    return customer

    def edit_customer(self, customer_id ,  customer_properties):
        customers_list = self.read_json()
        for customer in customers_list:
            for key , value in customer.items():
                if ((key == "id") & (value == customer_id)):
                    customer['name']  = customer_properties['name']  
                    customer['emai']  = customer_properties['email']  
                    customer['phone']  = customer_properties['phone'] 
                     
        self.write_json(customers_list)
