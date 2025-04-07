import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from packages.mylib.product.product import Product
from packages.mylib.customer.customer import Customer
class CoffeeStoreApp(Product , Customer):
    def __init__(self , master , products_app , customers_app):
        # Product.__init__(self, products_app)
        # Customer.__init__(self, customers_path)
        self.products_app = products_app
        self.customers_app = customers_app
        self.master = master
        self.master.title("Coffe Store")
        self.master.geometry("800x800")

        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(pady=10, fill="both" , expand=True)

        self.product_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.product_frame , text="products")

        self.customer_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.customer_frame , text="customers")

        add_product_btn = ttk.Button(self.master , text="add product" , bootstyle = "success" , command=self.add_product_window)
        add_product_btn.pack(side=LEFT , padx= 10 , pady= 10)

        add_customer_btn = ttk.Button(self.master , text="add customer" , bootstyle = "success" , command=self.add_customer_window)
        add_customer_btn.pack(side=LEFT , padx= 10 , pady= 10)

        self.refresh_product_list()
        self.refresh_customer_list()


    def refresh_product_list(self):
        # حذف تمامی موارد موجود در فریم محصولات
        for product_child in self.product_frame.winfo_children():
            product_child.destroy()

        # تعیین مسیر فایل JSON حاوی اطلاعات محصولات
        path = f"json/{self.products_app}.json"

        # خواندن لیست محصولات از فایل JSON
        product_list = self.read_json(path)

        # ایجاد رابط کاربری برای هر محصول در لیست محصولات
        for product in product_list:
            # ایجاد یک فریم جدید برای محصول
            frame = ttk.Frame(self.product_frame)

            # افزودن فریم به فریم اصلی با فاصله‌گذاری مناسب
            frame.pack(fill="x", padx=10, pady=5)

            # افزودن لیبل با نام فارسی محصول و قیمت آن
            ttk.Label(frame, text=f"{product['name_fa']}   {product['price']}").pack(side="left")

            # ایجاد متغیر عددی برای مقدار اولیه تعداد محصول
            qty = ttk.IntVar(value=1)

            # ایجاد Spinbox برای انتخاب تعداد محصول، از ۱ تا موجودی انبار
            ttk.Spinbox(frame, from_=1, to=product['stock'], textvariable=qty, width=5).pack(side="right")

            # افزودن دکمه "اضافه کردن به سبد خرید" برای هر محصول
            ttk.Button(frame, text="add to cart", command=lambda p=product, q=qty: self.add_to_cart(p, q.get())).pack(side="right")

            
    def add_to_cart(self , p , q):
        print("added" , p , q)
    
    def add_product(self):
        name = self.name.get()
        email = self.email.get()
        phone = self.phone.get()
        unit_en = self.unit_en.get()
        price = self.price.get()
        stock = self.stock.get()
        path = f"json/{self.products_app}.json"
        self.insert_product(path , name, email, phone, unit_en, price , stock)
        self.refresh_product_list()
    
    def add_product_window(self):
        window = ttk.Window("add product","solar", resizable=(False, False))
        window.geometry("300x300")
        label_name = ttk.Label(window, text="Fa Name :")
        label_name.grid(column=0, row=1, sticky=ttk.W, padx=10, pady=5)
        self.name =ttk.Entry(window,bootstyle="success", text="Example :لیبریکا ")
        self.name.grid(column=1, row=1, sticky=ttk.W, padx=10, pady=5)
        label_email = ttk.Label(window, text="En Name : ")
        label_email.grid(column=0, row=2, sticky=ttk.W, padx=10, pady=5)
        self.email = ttk.Entry(window, bootstyle="success", text="Example :new name of coffee " )
        self.email.grid(column=1, row=2, sticky=ttk.W, padx=10, pady=5)
        label_phone = ttk.Label(window, text="phone : ")
        label_phone.grid(column=0, row=3, sticky=ttk.W, padx=10, pady=5)
        self.phone = ttk.Entry(window, bootstyle="success", text="Example :گرم" )
        self.phone.grid(column=1, row=3, sticky=ttk.W, padx=10, pady=5)
        label_unit_en = ttk.Label(window, text="unit_en : ")
        label_unit_en.grid(column=0, row=3, sticky=ttk.W, padx=10, pady=5)
        self.unit_en = ttk.Entry(window, bootstyle="success", text="Example :gr" )
        self.unit_en.grid(column=1, row=3, sticky=ttk.W, padx=10, pady=5)
        label_price = ttk.Label(window, text="enprice : ")
        label_price.grid(column=0, row=4, sticky=ttk.W, padx=10, pady=5)
        self.price = ttk.Entry(window, bootstyle="success", text="Example :2000" )
        self.price.grid(column=1, row=4, sticky=ttk.W, padx=10, pady=5)
        label_stock = ttk.Label(window, text="stock : ")
        label_stock.grid(column=0, row=5, sticky=ttk.W, padx=10, pady=5)
        self.stock = ttk.Entry(window, bootstyle="success", text="Example :1000" )
        self.stock.grid(column=1, row=5, sticky=ttk.W, padx=10, pady=5)
        submit_add = ttk.Button(window, bootstyle="danger" , text="save", command=self.add_product)
        submit_add.grid(columnspan=2, row=7, sticky=ttk.EW, padx=10, pady=5)
#---------------------------------------------------------------------------        

    def refresh_customer_list(self):
        # حذف تمامی موارد داخل فریم مشتری
        for customer_child in self.customer_frame.winfo_children():
            customer_child.destroy()        
        # فراخوانی تمامی مشتریان موجود در پایگاه داده
        path = f"json/{self.customers_app}.json"
        customer_list = self.read_json(path)
        for customer in customer_list:
            # درج تک تک محصولات درون فریم مشتری
            frame = ttk.Frame(self.customer_frame)
            frame.pack(fill="x" , padx=10 , pady=5)
            ttk.Label(frame , text=f"{customer['name']}   {customer['email']}").pack(side="left")

    
    def add_customer(self):
        name = self.name.get()
        email = self.email.get()
        phone = self.phone.get()
        path = f"json/{self.customers_app}.json"
        self.insert_customer(path , name, email, phone)
        self.refresh_customer_list()
    
    def add_customer_window(self):
        window = ttk.Window("add customer","solar", resizable=(False, False))
        window.geometry("300x300")
        label_name = ttk.Label(window, text="Name :")
        label_name.grid(column=0, row=1, sticky=ttk.W, padx=10, pady=5)
        self.name =ttk.Entry(window,bootstyle="success", text="Example :لیبریکا ")
        self.name.grid(column=1, row=1, sticky=ttk.W, padx=10, pady=5)
        label_email = ttk.Label(window, text="email : ")
        label_email.grid(column=0, row=2, sticky=ttk.W, padx=10, pady=5)
        self.email = ttk.Entry(window, bootstyle="success", text="Example :new name of coffee " )
        self.email.grid(column=1, row=2, sticky=ttk.W, padx=10, pady=5)
        label_phone = ttk.Label(window, text="phone : ")
        label_phone.grid(column=0, row=3, sticky=ttk.W, padx=10, pady=5)
        self.phone = ttk.Entry(window, bootstyle="success", text="Example :گرم" )
        self.phone.grid(column=1, row=3, sticky=ttk.W, padx=10, pady=5)
        submit_add = ttk.Button(window, bootstyle="danger" , text="save", command=self.add_customer)
        submit_add.grid(columnspan=2, row=4, sticky=ttk.EW, padx=10, pady=5)

def main(products_app , customers_path):
    # create master window
    master = ttk.Window(themename="darkly")
    app = CoffeeStoreApp(master , products_app , customers_path)
    master.mainloop()

products_app = "products"
customers_path = "customers"
main(products_app , customers_path)
