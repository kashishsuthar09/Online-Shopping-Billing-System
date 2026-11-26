from tkinter import *
from tkinter import ttk

f = Tk()
f.geometry("650x600")
f.title("ONLINE SHOPPING BILL")
f.config(bg="#f2f6ff")


title = Label(
    f,
    text="ONLINE SHOPPING BILLING SYSTEM",
    font=("Arial", 18, "bold"),
    bg="#304ffe",
    fg="white",
    pady=15
)
title.pack(fill=X)


Label(
    f,
    text="Customer Name",
    font=("Arial", 11, "bold"),
    bg="#f2f6ff"
).place(x=80, y=90)

customer = Entry(f, width=30)
customer.place(x=220, y=90)


Label(
    f,
    text="Product",
    font=("Arial", 11, "bold"),
    bg="#f2f6ff"
).place(x=80, y=140)

product = ttk.Combobox(
    f,
    values=["Shirt", "Jeans", "Shoes", "Bag", "Watch"],
    width=27
)
product.place(x=220, y=140)


Label(
    f,
    text="Quantity",
    font=("Arial", 11, "bold"),
    bg="#f2f6ff"
).place(x=80, y=190)

quantity = Entry(f, width=30)
quantity.place(x=220, y=190)


Label(
    f,
    text="Price",
    font=("Arial", 11, "bold"),
    bg="#f2f6ff"
).place(x=80, y=240)

price = Entry(f, width=30)
price.place(x=220, y=240)


def calculate():

    name = customer.get()
    p = product.get()
    q = int(quantity.get())
    pr = float(price.get())

    total = q * pr

    if total >= 2000:
        discount = total * 10 / 100
    elif total >= 1000:
        discount = total * 5 / 100
    else:
        discount = 0

    final_amount = total - discount

    bill.config(
        text=
        "           SHOPPING BILL\n"
        "--------------------------------------\n"
        "Customer : " + name +
        "\nProduct  : " + p +
        "\nQuantity : " + str(q) +
        "\nPrice    : Rs. " + str(pr) +
        "\n--------------------------------------\n"
        "Total    : Rs. " + str(total) +
        "\nDiscount : Rs. " + str(discount) +
        "\nFinal Bill: Rs. " + str(final_amount) +
        "\n--------------------------------------\n"
        "     THANK YOU FOR SHOPPING!"
    )


def clear():

    customer.delete(0, END)
    product.set("")
    quantity.delete(0, END)
    price.delete(0, END)

    bill.config(text="")


Button(
    f,
    text="CALCULATE BILL",
    command=calculate,
    bg="#304ffe",
    fg="white",
    font=("Arial", 10, "bold"),
    width=15
).place(x=170, y=290)

Button(
    f,
    text="CLEAR",
    command=clear,
    bg="#ff5252",
    fg="white",
    font=("Arial", 10, "bold"),
    width=12
).place(x=340, y=290)


bill = Label(
    f,
    text="",
    font=("Courier New", 11),
    bg="white",
    fg="#222222",
    justify=LEFT,
    width=55,
    height=12,
    relief=GROOVE,
    bd=2
)
bill.place(x=100, y=350)


f.mainloop()
