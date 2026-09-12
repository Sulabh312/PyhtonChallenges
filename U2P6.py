tree = [(0, 0)]
sample = (3, 4)
max_step = 2
def nearest_node(tree, sample):
    nearest = tree[0]
    min_dis = float('inf')
    for node in tree:
        dx = sample[0] - node[0]
        dy = sample[1] - node[1]

        dis = (dx**2 + dy**2)**0.5
        if dis < min_dis:
            min_dis = dis
            nearest = node 
    return nearest
nearest = nearest_node(tree, sample)
print("nearest node:", nearest)

dx = sample[0] - nearest[0]
dy = sample[1] - nearest[1]
distance = (dx**2 + dy**2)**0.5
unit_x = dx/distance
unit_y = dy/distance
new_node = (nearest[0] + unit_x * max_step, nearest[1] + unit_y * max_step)
path_collision = False
if not path_collision:
    tree.append(new_node)
    print("new node:", new_node)