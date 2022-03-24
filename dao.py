import redis
import json
import traceback

client = redis.Redis(host='localhost', port=6379)

def getAll():
    customers = []
    try: 
        keys = client.keys()
        for key in keys:
            cust = client.get(key).decode('utf-8')
            try:
                customers.append(json.loads(cust))
            except json.decoder.JSONDecodeError as e:
                pass
            #json.loads
    except Exception as e:
        print(f"Exception occurred while accessing redis: {type(e)} {e}")
        #traceback.print_exc()

    return customers

def getCustomerById(id):
    cust = {}
    try:
        cust = client.get(key).decode('utf-8')
    except Exception as e:
        print(f"Got exception while getCustomerById: {e}")
    return cust

def createCustomer(cust):
    try:
        client.set(cust.get('id'),json.dumps(cust))
        return True
    except Exception as e:
        print(f"Error in creating record in redis: {e}")
        return False

def deleteCustomerById(id):
    try:
        response = client.delete(id)
        print(f"Response by delete call: {response}")
        return True
    except Exception as e:
        return False