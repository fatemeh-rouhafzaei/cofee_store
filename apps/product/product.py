from apps.rw_files.rw_files import RWFiles
class Product(RWFiles):
    def __init__(self, file_name):
        super().__init__(file_name)

    def product_names(self,products):
        product_names_list = []
        for product in products:
            product_names_list.append(product['name_en'])
        return product_names_list

    def insert_product(self,path, name_fa , name_en , unit_fa, unit_en, price, stock):
        # دریافت محصولات فعلی
        # file_name = "json/products.json"
        products_list = self.read_json(path)
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
        self.write_json(products_list , path)

    def remove_product(self,path, product_id):
        products_list = self.read_json(path)
        products_len = len(products_list)
        for product in products_list:
            for key , value in product.items():
                if ((key == "id") & (value == product_id)):
                    product_index =  products_list.index(product)
                    products_list.pop(product_index)
                else:
                    return "not_found"
        if len(products_list) == products_len - 1:
            self.write_json(products_list ,path)
            return "success"
        else:
            return "failed"

    def get_product_by_id(self,path, product_id):
        # دریافت محصولات فعلی
        products_list = self.read_json(path)
        for product in products_list:
            for key , value in product.items():
                if ((key == "id") & (value == product_id)):
                    return product

    def edit_product(self,path, product_id ,  product_properties):
        products_list = self.read_json(path)
        for product in products_list:
            for key , value in product.items():
                if ((key == "id") & (value == product_id)):
                    product['name_fa']  = product_properties['name_fa']  
                    product['name_en']  = product_properties['name_en']  
                    product['unit_fa']  = product_properties['unit_fa']  
                    product['unit_en']  = product_properties['unit_en']  
                    product['price']  = product_properties['price']  
                    product['stock']  = product_properties['stock']

        self.write_json(products_list ,path)
