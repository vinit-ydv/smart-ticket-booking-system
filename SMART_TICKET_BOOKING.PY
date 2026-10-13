movies = [
    ["Avengers: Endgame", 250],
    ["KGF Chapter 2", 220],
    ["RRR", 200],
    ["3 Idiots", 180]
]

bookings = []
booking_id = 1001


def show_movies():
    print("\n===== AVAILABLE MOVIES =====")

    for i in range(len(movies)):
        print(i + 1, ".", movies[i][0], "- Rs.", movies[i][1])


def book_ticket():
    global booking_id

    show_movies()

    choice = int(input("\nEnter movie number: "))

    if choice < 1 or choice > len(movies):
        print("Invalid movie number.")
        return

    name = input("Enter your name: ")
    tickets = int(input("Enter number of tickets: "))

    if tickets <= 0:
        print("Invalid number of tickets.")
        return

    movie_name = movies[choice - 1][0]
    price = movies[choice - 1][1]
    total = price * tickets

    booking = [
        booking_id,
        name,
        movie_name,
        tickets,
        total
    ]

    bookings.append(booking)

    print("\n===== BOOKING SUCCESSFUL =====")
    print("Booking ID :", booking_id)
    print("Name       :", name)
    print("Movie      :", movie_name)
    print("Tickets    :", tickets)
    print("Total      : Rs.", total)

    booking_id += 1


def view_bookings():
    if len(bookings) == 0:
        print("\nNo bookings found.")
        return

    print("\n===== ALL BOOKINGS =====")

    for booking in bookings:
        print("\nBooking ID :", booking[0])
        print("Name       :", booking[1])
        print("Movie      :", booking[2])
        print("Tickets    :", booking[3])
        print("Total      : Rs.", booking[4])


def cancel_ticket():
    if len(bookings) == 0:
        print("\nNo bookings found.")
        return

    booking_number = int(input("\nEnter Booking ID: "))

    for booking in bookings:
        if booking[0] == booking_number:
            bookings.remove(booking)
            print("\nTicket cancelled successfully.")
            return

    print("\nBooking ID not found.")


while True:
    print("\n================================")
    print("   SMART TICKET BOOKING SYSTEM")
    print("================================")
    print("1. Show Movies")
    print("2. Book Ticket")
    print("3. View Bookings")
    print("4. Cancel Ticket")
    print("5. Exit")
    print("================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_movies()

    elif choice == "2":
        book_ticket()

    elif choice == "3":
        view_bookings()

    elif choice == "4":
        cancel_ticket()

    elif choice == "5":
        print("\nThank you for using Smart Ticket Booking System!")
        break

    else:
        print("\nInvalid choice. Please enter 1 to 5.")