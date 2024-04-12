def find_friends(graph, user):
    direct_friends = list(graph[user])
    friends_of_friends = set()

    visited = set()
    queue = [user]
    visited.add(user)

    while queue:
        node = queue.pop(0)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                if neighbor not in direct_friends:
                    friends_of_friends.add(neighbor)
                queue.append(neighbor)

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
    'Омелько': ['Тарас', 'Петро', 'Панас'],
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
