def bfs(graph, start):
    visited = set()
    queue = [start]
    visited.add(start)
    result = []
    while queue:
        node = queue.pop(0)
        result.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return result


def find_friends(graph, root):
    friends = list(graph[root])
    friends_of_friends = set()

    for friend in friends:
        bfs_result = bfs(graph, friend)
        for friend_of_friend in bfs_result:
            if friend_of_friend != root and friend_of_friend not in friends:
                friends_of_friends.add(friend_of_friend)
    return friends, friends_of_friends


def check_friendship(root, friends, graph):
    for friend in friends:
        if root in graph[friend] and friend in graph[root]:
            print(root, " та ", friend, " справжні друзі :)")
        else:
            print(root, " та ", friend, " не справжні друзі :(")


graph = {
    'Тарас': ['Параска', 'Омелько', 'Панас'],
    'Параска': ['Тарас', 'Омелько', 'Марфа'],
    'Омелько': ['Тарас', 'Параска', 'Панас'],
    'Марфа': ['Параска', 'Панас'],
    'Панас': ['Омелько', 'Марфа'],
    'Остап': ['Іванко', 'Андрійко'],
    'Іванко': ['Остап', 'Андрійко'],
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
