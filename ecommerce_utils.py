

def apply_discount(price, discount_percent):
    return price - (price * discount_percent / 100)


def add_gst(price, gst_percent=18):
    return price + (price * gst_percent / 100)


def generate_invoice(cart, discount_percent=0, gst_percent=18):
    total = 0
    for product, price in cart.items():
        discounted_price = apply_discount(price, discount_percent)
        final_price = add_gst(discounted_price, gst_percent)
        total += final_price
        print(f"{product}: ${final_price:.2f}")
    print(f"Total Price: ${total:.2f}")
