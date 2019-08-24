import os
import json
from customer import newCustomer
from customer import existingUser
from adminLogin import adminLoogin

print("1. Existing CUSTOMER")
print("2. New Customer")
print("3. ADMIN")

select = int(input())

if select == 1:
    existingUser()
elif select == 2:
    newCustomer()
else:
    adminLoogin()

