import threading
import time

class TicketBooking:
    def __init__(self, available_seats):
        self.available_seats = available_seats
        self.lock = threading.Lock()
        self.counter = 1
        self.seat = 0

    def seats(self):
        self.lock.acquire()
        if self.counter < self.available_seats+1:
            self.seat += 1
            time.sleep(0.01)
            print(f"counter {self.counter} booked seat {self.seat}")
        else:
            print(f"No available for Counter {self.counter}")
        self.lock.release()
        self.counter += 1
    pass

test = TicketBooking(100)
threads = []

for i in range(110):
    booking = threading.Thread(target=test.seats)
    threads.append(booking)
    booking.start()

for booking in threads:
    booking.join()