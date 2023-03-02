num_full_boxes = 0.0

num_itemsA = int(input())
num_itemsB = int(input())
num_itemsC = int(input())

# a box can hold max 5 items
num_full_boxes += num_itemsA / 5
num_full_boxes += num_itemsB / 5
num_full_boxes += num_itemsC / 5

print(f"Number of full boxes: {int(num_full_boxes)}")
