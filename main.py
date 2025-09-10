
import ecommerce_utils


cart = {
    "Laptop": 1000,
    "Smartphone": 500,
    "Headphones": 150
}

discount_percent = 10  
gst_percent = 18  


ecommerce_utils.generate_invoice(cart, discount_percent, gst_percent)
