"""
Answer to Question 7.7

System design:
The system will have the Server class, with a list of users, messages, and chats. This class can add and remove users,
and we can make it being able to get chats and messages.
The system will have a Message class, with the fields: "from", "to", "text", and "time".
The system will have a Chat class, with a list of messages.
The system will have a User class, with the fields: "chats", "username", "name", "dateJoined", and "friends".
This class will be able to sendMessage, addFriend, removeFriend, and more.

To this design we could potentially add sign-in/out, update status, support for group chats, friend requests, and more.

Backend components:
- DB, or even multiple for backup and minimzation of lookups.
- Set of clients
- Set of servers (for backups and more)
- Components that connect the frontend to the severs.
- Communication via XML (could be slow but easier to debug)

Hardest problem:
- How to update messages without having the user refreshing the page? Async pulling of messages from the server (e.g web sockets)
- How to know when users are online? Can ping the client every one minute
- Information on the server/local is out of sync, how to deal? Can always take from server, and if not updated - let user know
- How to build for scaling? Split data across many servers
- DOS attacks? Need to look up ways of dealing with this kind of attacks
- SQL injection? Checking the information received well before sending a query

"""