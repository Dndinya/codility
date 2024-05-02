users = [
    {
        "id": 30,
        "username": "Ruth.Nduta",
        "email": "ruthnduta891@gmail.com",
        "messages": [
            {
                "msg_id": 45,
                "read": False,
                "user_id": 30
            },
            
            {
                "msg_id": 3,
                "read": False,
                "user_id": 30
            },
            {
                "msg_id": 112,
                "read": False,
                "user_id": 30
            }
        ]
    },
    {
        "id": 31,
        "username": "Pascaline.Chumba",
        "email": "pjerono56@gmail.com",
        "messages": []
    },
    {
        "id": 45,
        "username": "Josephbill",
        "email": "josephbill00@gmail.com",
        "messages": [
            {
                "msg_id": 3,
                "read": False,
                "user_id": 45
            }
        ]
    },
    {
        "id": 26,
        "username": "Simon.Thuo",
        "email": "simonthuo85@gmail.com",
        "messages": []
    },
    {
        "id": 112,
        "username": "Christine.Kiage",
        "email": "christinekiage@gmail.com",
        "messages": [
                  {
                "msg_id": 45,
                "read": False,
                "user_id": 27
            },
            {
                "msg_id": 3,
                "read": False,
                "user_id": 27
            },
            {
                "msg_id": 112,
                "read": False,
                "user_id": 27
            }
            ]
    }]
    
given_user_id = 30 

# filter the users object to get the object belonging to the logged in user 
users_object = next((user for user in users if user["id"] == given_user_id ) , None)

# validate if the user object
if users_object:
    print("users messages: ")
    print(users_object["messages"])
    
    # filter for read status 
    filtered_messages = [item for item in users_object["messages"] if not item["read"]]
    
    # use my filtered list to tag the msg_id 
    sort_order_set = set(item["msg_id"] for item in filtered_messages)
    
    # sort and tag users list based on the sort order i.e. bias on unread status 
    sorted_users = [
                   {
                       **user,
                       "tag" : "unread" if user["id"] in sort_order_set else "read"
                   }
                   for user in users
        ]
    sorted_users.sort(key=lambda x: sort_order_set.__contains__(x["id"]), reverse=True )
    print("Sorted array filtered list " , sorted_users)
else:
    print("user not found")



#  filter out ruth or logged in user from the sorted list 









