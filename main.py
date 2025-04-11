import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from apps.mylib.store_lib import *
file_name = "json/products.json"

class CoffeeStoreApp:
    def __init__(self , master):
        self.master = master
        self.master.title("Coffe Store")
        self.master.geometry("400x400+1990+200")
        self.create_widgets()

        

    def create_widgets(self):

        self.product_list_box = tk.Listbox(self.master)
        self.product_list_box.pack(fill=tk.BOTH , expand = True , padx=10 , pady=10)

        add_add = ttk.Button(self.master , text="add product" , bootstyle = "success" , command=self.add_window)
        add_add.pack(side=LEFT , padx= 10 , pady= 10)

        self.refresh_product_list()

    def refresh_product_list(self):
        # حذف تمامی موارد داخل لیست باکس
        self.product_list_box.delete(0, tk.END)

        # فراخوانی تمامی محصولات موجود در پایگاه داده
        product_list = read_json(file_name)
        for product in product_list:
            # درج تک تک محصولات درون لیست باکس
            self.product_list_box.insert(tk.END , f"{product['name_fa']}   {product['price']}")
    
    def add_product(self):
        name_fa = self.name_fa.get()
        name_en = self.name_en.get()
        unit_fa = self.unit_fa.get()
        unit_en = self.unit_en.get()
        price = self.price.get()
        stock = self.stock.get()
        insert_product(file_name , name_fa, name_en, unit_fa, unit_en, price , stock)
        self.refresh_product_list()
    
    def add_window(self):
        window = ttk.Window("add product","solar", resizable=(False, False))
        window.geometry("300x300+2700+200")
        label_name_fa = ttk.Label(window, text="Fa Name :")
        label_name_fa.grid(column=0, row=1, sticky=ttk.W, padx=10, pady=5)
        self.name_fa =ttk.Entry(window,bootstyle="success", text="Example :لیبریکا ")
        self.name_fa.grid(column=1, row=1, sticky=ttk.W, padx=10, pady=5)
        label_name_en = ttk.Label(window, text="En Name : ")
        label_name_en.grid(column=0, row=2, sticky=ttk.W, padx=10, pady=5)
        self.name_en = ttk.Entry(window, bootstyle="success", text="Example :new name of coffee " )
        self.name_en.grid(column=1, row=2, sticky=ttk.W, padx=10, pady=5)
        label_unit_fa = ttk.Label(window, text="unit_fa : ")
        label_unit_fa.grid(column=0, row=3, sticky=ttk.W, padx=10, pady=5)
        self.unit_fa = ttk.Entry(window, bootstyle="success", text="Example :گرم" )
        self.unit_fa.grid(column=1, row=3, sticky=ttk.W, padx=10, pady=5)
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

def main():
    # create master window
    master = ttk.Window(themename="darkly")
    app = CoffeeStoreApp(master)
    master.mainloop()

main()
