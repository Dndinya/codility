import json
def solution(array_of_users, target_id):
    result = []
    unread_users = []
    read_users = []
    
    # Iterate through users, categorize them based on read/unread messages
    for user in array_of_users:
        if user["id"] == target_id:
            unread_messages = any(msg["read"].lower() == "false" for msg in user["messages"])
            user["Tag"] = "unread" if unread_messages else "read"
            if unread_messages:
                unread_users.append(user)
            else:
                read_users.append(user)
        else:
            unread_messages = any(msg["read"].lower() == "false" for msg in user["messages"])
            user["Tag"] = "unread" if unread_messages else "read"
            if unread_messages:
                unread_users.append(user)
            else:
                read_users.append(user)

    # result.append(user)
    # Sort users with unread messages first, then read users
    result.extend(unread_users)
    result.extend(read_users)
    
    return result

array_of_users = [
    {
        "id": 30,
        "username": "Ruth.Nduta",
        "email": "ruthnduta891@gmail.com",
        "messages": [
            {
                "receipient_id": 45,
                "read": "false",
                "user_id": 30
            },
            {
                "receipient_id": 3,
                "read": "false",
                "user_id": 30
            },
            {
                "receipient_id": 112,
                "read": "false",
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
                "read": "true",
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
                "read": "false",
                "user_id": 27
            },
            {
                "msg_id": 3,
                "read": "false",
                "user_id": 27
            },
            {
                "msg_id": 112,
                "read": "false",
                "user_id": 27
            }
            ]
    }]

sorted_array = solution(array_of_users, 30)
for user in sorted_array:
    print(json.dumps(user, indent=4))

