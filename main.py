class Event:
    def __init__ (self, payload):
        self.payload = payload

class OrderSubmittedEvent(Event):
    def __init__ (self, payload):
        super().__init__(payload)

class OrderProcessedEvent(Event):
    def __init__(self, payload):
        super().__init__(payload)

class OrderRejectedEvent(Event):
    def __init__(self, payload):
        super().__init__(payload)


class CommunicationQueue:
    def __init__(self):
        self.queue = []

    def add.event(self, event):
        self.queue.append(event)
    
    def get_events(self):
        return self.queue
    
    def process_events(self):
    while self.queue:
        event = self.queue.pop(0)
        print(f"Processing event: {type(event).__name__}, Payload: {event.payload}")
    
class Store:
    def __init__(self, name, communication_queue):
        self.name = name
        self.communication_queue = communication_queue
        self.stock = {"Laptop": 5, "Desktop": 3, "Monitor": 10}

    def process_order(self, order):
        item = order['item']
        quantity = order['quantity']

        if  item in self.stock and self.stock[item] >= quantity:
            self.stock[item] -= quantity
            self.communication_queue.add.event(OrderProcessedEvent({
                "customer": order['customer'],
                "item": item,
                "quantity": quantity,
                "status": "processed"
            }))
        else:
                self.communication_queue.add_event(OrderRejectedEvent({
                "customer": order['customer'],
                "item": item,
                "quantity": quantity,
                "status": "rejected"
            }))

class Customer:
    def __init__(self, name, communication_queue):
        self.name = name
        self.communication_queue = communication_queue
    
    def submit_order(self, item , quantity): 
        order = {
                "customer": order['customer'],
                "item": item,
                "quantity": quantity
        }
        print(f"{self.name} is sunmitting an order for {quantity} x {item}.")
        self.communication_queue.add_event(OrderSubmittedEvent(order))
        return order
    
if __name__ == "__main__":
    queue = CommunicationQueue()

    store = Store("Abdurrahmans Technical Store", queue)

    customer1 = Customer("Bekir", queue)
    customer2 = Customer("Safa", queue)

    order1 = customer1.submit_order("Laptop", 2)
    order2 = customer2.submit_order("Desktop", 4)
    order3 = customer1.submit_order("Monitor", 5)

    store.process_order(order1)
    store.process_order(order2)
    store.process_order(order3)

    print("\nProcessing events from the queue:\n")
    queue.process_events()  