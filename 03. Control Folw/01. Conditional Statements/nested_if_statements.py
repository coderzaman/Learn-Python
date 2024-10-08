# Nested if Statements
# If area is ["Mirpur", "Mohammadpur", "Kyallanpur"]
#     if purchase is greater than equal 1000 delivery cost 30
#     else purchase is greater than equal 700 delivery cost 100
#     else purchase is greater than equal 500 delivery cost 120
#     else 150
from keyring.backends.libsecret import available

# else are is ["Farmgate", "Dhanmodi", "Nil khet"]
#     if purchase is greater than equal 1000 delivery cost 50
#     else purchase is greater than equal 700 delivery cost 120
#     else purchase is greater than equal 500 delivery cost 150
#     else 170
# else not delivery available
customer_area = "Mirpur"
purchase = 700
area1 = ["Mirpur", "Mohammadpur", "Kyallanpur"]
area2 = ["Farmgate", "Dhanmodi", "Nil khet"]
if customer_area in area1:
    if purchase >= 1000:
        print("Your Delivery Cost is 30")
    elif purchase >= 700:
        print("Your Deliver Cost is: 100")
    elif purchase >= 500:
        print("Your Delivery Cost is:  120")
    else:
        print("Your Delivery Cost is: 150")
elif customer_area in area2:
    if purchase >= 1000:
        print("Your Delivery Cost is 50")
    elif purchase >= 700:
        print("Your Deliver Cost is: 120")
    elif purchase >= 500:
        print("Your Delivery Cost is:  150")
    else:
        print("Your Delivery Cost is: 170")
else:
    print("Delivery Not available in your area")
