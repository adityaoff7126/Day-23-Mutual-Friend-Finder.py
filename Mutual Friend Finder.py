network = {}

def add_user():
    user = input("Enter username: ").lower()

    if user in network:
        print("User already exists")
    else:
        network[user] = set()
        print(f"{user} added")

def add_friend():
    user = input("Enter your username: ").lower()

    if user not in network:
        print("User not found")
        return

    while True:
        f1 = input("Enter friend name (or 'no' to stop): ").lower()

        if f1 == "no":
            break

        if f1 not in network:
            print("Friend does not exist")
            continue

        if f1 == user:
            print("Cannot add yourself")
            continue

        if f1 in network[user]:
            print("Already friends")
            continue

        network[user].add(f1)

def mutual():
    u1 = input("User 1: ").lower()
    u2 = input("User 2: ").lower()

    if u1 not in network or u2 not in network:
        print("User not found")
        return

    common = network[u1] & network[u2]

    print("Mutual friends:", common)

def suggest():
    user = input("Enter user: ").lower()

    if user not in network:
        print("User not found")
        return

    suggestions = set()

    for friend in network[user]:
        suggestions |= network[friend]

    suggestions -= network[user]  
    print("Suggestions:", suggestions)

def most_connected():
    max_user = None
    max_count = 0

    for user, friends in network.items():
        if len(friends) > max_count:
            max_count = len(friends)
            max_user = user

    print(f"Most connected: {max_user} ({max_count} friends)")

def network_size():
    user = input("Enter user: ").lower()

    if user not in network:
        print("User not found")
        return

    print(f"{user} has {len(network[user])} friends")

while True:
    print("\n1.Add User 2.Add Friend 3.Mutual 4.Suggest 5.Top User 6.Size 7.Exit")
    ch = input("Choice: ")

    if ch == "1":
        add_user()
    elif ch == "2":
        add_friend()
    elif ch == "3":
        mutual()
    elif ch == "4":
        suggest()
    elif ch == "5":
        most_connected()
    elif ch == "6":
        network_size()
    elif ch == "7":
        break