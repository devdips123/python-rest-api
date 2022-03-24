import redis
import json
import dao
customer = {
    "id": 21,
    "name": "Debasish Sahoo",
    "phone": "216-225-4546"
}

def getAll():
    customers = dao.getAll()
    
    return customers

def create(cust):
    return dao.createCustomer(cust)

def deleteById(id):
    return dao.deleteCustomerById(id)

def getById(id):
    return dao.getCustomerById(id)

    
if __name__ == '__main__':
    customers = getAll()
    print(f"Total Customers: {customers}")