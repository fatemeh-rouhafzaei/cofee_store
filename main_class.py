import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from packages.lib.product.product import Product
class CoffeeStoreApp(Product , customer):
    def __init__(self , master , file_name_1 , file_name_2):
        super().__init__(file_name_1 , file_name_2)
        self.master = master
        self.master.title("Coffe Store")
        self.master.geometry("400x400+1990+200")
        self.create_widgets_product()
        self.create_widgets_customer()

        

    def create_widgets_product(self):
        self.product_list_box = tk.Listbox(self.master)
        self.product_list_box.pack(fill=tk.BOTH , expand = True , padx=10 , pady=10)
        add_product_btn = ttk.Button(self.master , text="add product" , bootstyle = "success" , command=self.add_product_window)
        add_product_btn.pack(side=LEFT , padx= 10 , pady= 10)
        self.refresh_product_list()

        self.customer_list_box = tk.Listbox(self.master)
        self.customer_list_box.pack(fill=tk.BOTH , expand = True , padx=10 , pady=10)
        add_customer_btn = ttk.Button(self.master , text="add customer" , bootstyle = "success" , command=self.add_product_window)
        add_customer_btn.pack(side=LEFT , padx= 10 , pady= 10)

    def refresh_product_list(self):
        # حذف تمامی موارد داخل لیست باکس
        self.product_list_box.delete(0, tk.END)

        # فراخوانی تمامی محصولات موجود در پایگاه داده
        product_list = self.read_json()
        for product in product_list:
            # درج تک تک محصولات درون لیست باکس
            self.product_list_box.insert(tk.END , f"{product['name']}   {product['price']}")
    
    def add_product(self):
        name = self.name.get()
        email = self.email.get()
        phone = self.phone.get()
        unit_en = self.unit_en.get()
        price = self.price.get()
        stock = self.stock.get()
        self.insert_product(name, email, phone, unit_en, price , stock)
        self.refresh_product_list()
    
    def add_product_window(self):
        window = ttk.Window("add product","solar", resizable=(False, False))
        window.geometry("300x300+2700+200")
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
    def create_widgets_customer(self):
        self.customer_list_box = tk.Listbox(self.master)
        self.customer_list_box.pack(fill=tk.BOTH , expand = True , padx=10 , pady=10)
        add_customer_btn = ttk.Button(self.master , text="add customer" , bootstyle = "success" , command=self.add_customer_window)
        add_customer_btn.pack(side=LEFT , padx= 10 , pady= 10)
        self.refresh_customer_list()

        self.customer_list_box = tk.Listbox(self.master)
        self.customer_list_box.pack(fill=tk.BOTH , expand = True , padx=10 , pady=10)
        add_customer_btn = ttk.Button(self.master , text="add customer" , bootstyle = "success" , command=self.add_customer_window)
        add_customer_btn.pack(side=LEFT , padx= 10 , pady= 10)

    def refresh_customer_list(self):
        # حذف تمامی موارد داخل لیست باکس
        self.customer_list_box.delete(0, tk.END)

        # فراخوانی تمامی محصولات موجود در پایگاه داده
        customer_list = self.read_json()
        for customer in customer_list:
            # درج تک تک محصولات درون لیست باکس
            self.customer_list_box.insert(tk.END , f"{customer['name']}   {customer['email']}")
    
    def add_customer(self):
        name = self.name.get()
        email = self.email.get()
        phone = self.phone.get()
        self.insert_customer(name , email , phone)
        self.refresh_customer_list()
    
    def add_customer_window(self):
        window = ttk.Window("add customer","solar", resizable=(False, False))
        window.geometry("300x300+2700+200")
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
        submit_add = ttk.Button(window, bootstyle="danger" , text="save", command=self.add_customer)
        submit_add.grid(columnspan=2, row=4, sticky=ttk.EW, padx=10, pady=5)

def main(file_name):
    # create master window
    master = ttk.Window(themename="darkly")
    app = CoffeeStoreApp(master , file_name_1 , file_name_2)
    master.mainloop()

file_name_1 = "json/products.json"
file_name_2 = "json/customers.json"
main(file_name_1)
