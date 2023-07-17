from tkinter import *
from tkinter import ttk

deliveryMethod = 0


def create_banner(window):
    banner = Frame(window, bg="green", padx=10, pady=10)
    banner.grid(column=0, row=0, sticky="N E W")

    Label(banner, text="LOGO STAND-IN").grid(column=1, row=1, padx=10, pady=5, sticky="N E W")
    Label(banner, text="Luigi's Homestyle Pizzeria").grid(column=2, row=1, padx=10, pady=5, sticky="N W")
    Button(banner, text="CART STAND-IN").grid(column=3, row=1, padx=10, pady=5, sticky="N E")
    #Button(banner, image="CART IMAGE FILE", command=cart_move).grid(column=3, row=1, padx=10, pady=5, sticky="N E")


def create_bg(window):
    backing = Frame(window, padx=10, pady=10)
    backing.grid(column=0, row=1, sticky="W E S")
    return backing


def item_listing(frame, img, itemName, price, itemNum):
    Label(frame, text=img).grid(column=1, row=itemNum+1)
    #Label(frame, image=img).grid(column=1, row=itemNum+1)
    Label(frame, text=itemName).grid(column=2, row=itemNum+1)

    quantity = StringVar(value="Quantity")
    Entry(frame, textvariable=quantity).grid(column=3, row=itemNum+1)

    Button(frame, text="Edit").grid(column=4, row=itemNum+1)
    #Button(frame, text="Edit", command=detail_move).grid(column=4, row=itemNum+1)

    Button(frame, text="Add").grid(column=5, row=itemNum+1)
    #Button(frame, text="Add", command=add_item).grid(column=5, row=itemNum+1)

    Label(frame, text="$"+str(price)).grid(column=6, row=itemNum+1)


def order_move(deliveryCheck):
    global deliveryMethod
    deliveryMethod = deliveryCheck

    orderWindow = Tk()
    orderWindow.title("Luigi's Homestyle Pizzeria App")
    orderWindow.columnconfigure(0, weight=1)
    orderWindow.rowconfigure(0, weight=1)

    create_banner(orderWindow)
    orderBacking = create_bg(orderWindow)
    Label(orderBacking, text="What would you like to order?").grid(column=1,row=1)

    item_listing(orderBacking, "ITEM 1 IMAGE", "Meat Pizza", 19.99, 1)
    item_listing(orderBacking, "ITEM 2 IMAGE", "Veg Pizza", 15.99, 2)

    #Button(orderBacking, text="Finalize Order").grid(column=6, sticky="S")
    Button(orderBacking, text="Finalize Order", command=cart_move).grid(column=6, sticky="S")


def cart_move():
    cartWindow = Tk()
    cartWindow.title("Luigi's Homestyle Pizzeria App")
    cartWindow.columnconfigure(0, weight=1)
    cartWindow.rowconfigure(0, weight=1)

    create_banner(cartWindow)
    cartBacking = create_bg(cartWindow)
    Label(cartBacking, text="Your Cart:").grid(column=1,row=1)

    #item_listing(cartBacking, "ITEM 1 IMAGE", "Meat Pizza", 19.99, 1)
    #item_listing(cartBacking, "ITEM 2 IMAGE", "Veg Pizza", 15.99, 2)

    Button(cartBacking, text="Checkout").grid(column=6, sticky="S")
    #Button(cartBacking, text="Finalize Order", command=checkout_move).grid(column=6, sticky="S")
    #Button(cartBacking, text="Keep Shopping").grid(column=5, sticky="S")
    Button(cartBacking, text="Finalize Order", command=lambda: order_move(deliveryMethod)).grid(column=6, sticky="S")


def home_move():
    homeWindow = Tk()
    homeWindow.title("Luigi's Homestyle Pizzeria App")
    homeWindow.columnconfigure(0, weight=1)
    homeWindow.rowconfigure(0, weight=1)

    create_banner(homeWindow)
    homeBacking = create_bg(homeWindow)

    Label(homeBacking, text="Welcome to Luigi's! Select an order option below:").grid(column=2, row=1)
    Button(homeBacking, text="Order Delivery", command=lambda: order_move(1)).grid(column=1, row=2)
    Button(homeBacking, text="Order Carryout", command=lambda: order_move(0)).grid(column=3, row=2)

    # Insert Specials

    Button(homeBacking, text="Exit App", command=homeWindow.destroy).grid(column=2, row=3)
    homeWindow.mainloop()

home_move()

