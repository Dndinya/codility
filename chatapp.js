function solution(arrayOfUsers, targetId) {
    // Filter users based on the target ID and add tags
    arrayOfUsers.forEach(user => {
        if (user.id === targetId) {
            const unreadMessages = user.messages.some(msg => !msg.read);
            user.tag = unreadMessages ? "unread" : "read";
        } else {
            user.tag = "read"; // Assume all other users are read
        }
    });

    // Sort users based on tags
    arrayOfUsers.sort((a, b) => {
        if (a.tag === "unread" && b.tag === "read") {
            return -1; // Place unread users before read users
        } else if (a.tag === "read" && b.tag === "unread") {
            return 1; // Place read users after unread users
        } else {
            return 0; // Preserve order if both are unread or both are read
        }
    });

    return arrayOfUsers;
}

// Sample input and usage
let dataArray = [
    {
        "id": 30,
        "username": "Ruth.Nduta",
        "email": "ruthnduta891@gmail.com",
        "messages": [
            {
                "receipient_id": 45,
                "read": false,
                "user_id": 30
            },
            {
                "receipient_id": 3,
                "read": false,
                "user_id": 30
            },
            {
                "receipient_id": 112,
                "read": false,
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
                "read": true,
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
                "read": false,
                "user_id": 27
            },
            {
                "msg_id": 3,
                "read": false,
                "user_id": 27
            },
            {
                "msg_id": 112,
                "read": false,
                "user_id": 27
            }
            ]
    }]
;
let sortedArray = solution(dataArray, 30);
console.log(sortedArray);
