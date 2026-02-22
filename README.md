# Social Network Simulator (Python)

## Overview
A simple command-line social network system built using Python dictionaries and sets.

Each user is stored as a key in a dictionary, and their friends are stored as a set.

This project demonstrates:
- Dictionary usage
- Set operations
- Basic system design logic
- Menu-driven programs

---

## Data Structure

```python
network = {
    "user1": {"friend1", "friend2"},
    "user2": {"friend1"}
}
```

- Key → username
- Value → set of friends

---

## Features

### 1. Add User
- Adds a new user to the network
- Prevents duplicate users

### 2. Add Friend
- Adds a friend connection
- Validates:
  - User exists
  - Friend exists
  - Cannot add self
  - No duplicate friendships

### 3. Mutual Friends
- Finds common friends between two users
- Uses set intersection:
```python
common = network[u1] & network[u2]
```

### 4. Friend Suggestions
- Suggests friends-of-friends
- Uses set union:
```python
suggestions |= network[friend]
```
- Removes existing friends from suggestions

### 5. Most Connected User
- Finds the user with the highest number of friends

### 6. Network Size
- Shows total friends of a user

---

## Core Concepts Used

### Dictionary
Stores users and their connections

### Set
Used for:
- Unique friend storage
- Fast lookup
- Operations like:
  - Union (`|`)
  - Intersection (`&`)
  - Difference (`-`)

---

## How Suggestions Work

Step-by-step:
1. Take user's friends
2. Get friends of those friends
3. Combine all using union
4. Remove:
   - Already existing friends
   - (Optional improvement: remove self)

---

## Example

```
Users:
A → B, C
B → A, D
C → A, D

Suggestions for A:
→ D
```

---

## Menu System

```
1. Add User
2. Add Friend
3. Mutual Friends
4. Suggestions
5. Most Connected User
6. Network Size
7. Exit
```

---

## Possible Improvements

- Make friendships mutual (bidirectional)
- Save/load data using JSON
- Add user deletion
- Add friend removal
- Rank suggestions based on frequency
- Add login system
- Convert to GUI or web app

---

## Learning Outcome

After completing this project, you will understand:
- Real-world use of sets
- Graph-like structures
- Relationship mapping
- Basic system design thinking

---

## Run the Program

```bash
python filename.py
```

---

## Author

Aditya
