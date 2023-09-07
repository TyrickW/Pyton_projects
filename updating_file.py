approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]
approved_devices = ["8rp2k75", "hl0s5o1", "4n482ts", "a307vir", "3rcv4w6"]

# Define a function named `login` that takes in two parameters, `username` and `device_id`

def login(username, device_id):
    # If `username` belongs to `approved_users`,

    if username in approved_users:
        print("The user", username, "is approved to access the system.")

        # assign `ind` to the index of `username` in `approved_users`,
        ind = approved_users.index(username)

        # and execute the following conditional
        # If `device_id` matches the element at the index `ind` in `approved_devices`,
        if device_id == approved_devices[ind]:

            print(device_id, "is the assigned device for", username)

        else:

            print(device_id, "is not their assigned device.")

    #Part of the outer conditional and handles the case when `username` does not belong to `approved_users`,

    else:

        print("The username", username, "is not approved to access the system.")


# Call the function
login("bmoreno", "hl0s5o1")
login("elarson", "r2s5r9g")
login("abernard", "4n482ts")