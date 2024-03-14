list_of_users = ["sysadmin", "serviceadmin",
                 "dbalevel1", "dbalevel2", "dbalevel3"]

greetings = "Hello"

for user in list_of_users:
    print(f'{greetings}, {user}\n')

print(list_of_users)

list_of_users[0] = 'sysadmin_np'
print(list_of_users)

list_of_users.append('cbs_non_prod')
print(list_of_users)

list_of_users.insert(0, 'master_admin')
print(list_of_users)

del list_of_users[0]
print(list_of_users)

# Need to find a way to indentify what's element position to be popped - to be implemented
print(list_of_users)
removed_user = list_of_users.pop(-1)
print(removed_user)
