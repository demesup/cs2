def find_friends(graph, root):
    direct_friends = []
    friends_of_friends = set()

    visited = set()
    queue = [(root, 0)]
    visited.add(root)

    while queue:
        node, level = queue.pop(0)
        if level == 2:
            break
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                if level == 0:
                    direct_friends.append(neighbor)
                elif level == 1:
                    friends_of_friends.add(neighbor)
                queue.append((neighbor, level + 1))

    return direct_friends, friends_of_friends


def check_friendship(root, friends, graph):
    for friend in friends:
        if root in graph[friend] and friend in graph[root]:
            print(root, " та ", friend, " справжні друзі :)")
        else:
            print(root, " та ", friend, " не справжні друзі :(")


graph = {
    'Тарас': ['Параска', 'Омелько', 'Панас'],
    'Параска': ['Тарас', 'Омелько', 'Марфа'],
    'Омелько': ['Тарас', 'Петро', 'Марія'],
    'Марфа': ['Параска', 'Панас'],
    'Панас': ['Омелько', 'Марфа'],
    'Остап': ['Іванко', 'Андрійко'],
    'Іванко': ['Тарас', 'Параска'],
    'Андрійко': ['Остап', 'Іванко'],
    'Іван': ['Марія', 'Петро'],
    'Марія': ['Іван', 'Петро'],
    'Петро': ['Іван', 'Марія']
}

user = 'Тарас'
direct_friends, friends_of_friends = find_friends(graph, user)
print("Друзі юзера ", user, ":", direct_friends)
print("Друзі друзів юзера", user, ":", list(friends_of_friends))

check_friendship(user, direct_friends, graph)
check_friendship(user, friends_of_friends, graph)
