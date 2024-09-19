K = int(input())
room_nums = list(map(int, input().split()))

# Calculate Captain's room number using set properties
captain_room = (K * sum(set(room_nums)) - sum(room_nums)) // (K-1)

# Output the Captain's room number
print(captain_room)