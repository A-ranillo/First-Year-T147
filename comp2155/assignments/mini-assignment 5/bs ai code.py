import threading
import time

class TicketBooking:
    def __init__(self, available_seats):
        self.available_seats = available_seats
        self.lock = threading.Lock()
        self.seat = 0

    def book_seat(self, counter_id):
        with self.lock:
            if self.available_seats > 0:
                self.seat += 1
                self.available_seats -= 1
                time.sleep(0.01)
                print(f"Counter {counter_id} booked seat {self.seat}")
            else:
                print(f"No seats available for Counter {counter_id}")

def main():
    # define max seats
    max_seats = 100
    # instantiate ticket booking instance
    TicketBooking(max_seats)
    # create a list to hold all the threads
    threads = []
    # Create 110 threads simulating 110 counters
    for i in range(110):
        booking = threading.Thread(target=TicketBooking.book_seat, args=(i+1,))
        threads.append(booking)
        booking.start()
    # Wait for all threads to finish
    for booking in threads:
        booking.join()

if __name__ == "__main__":
    main()
