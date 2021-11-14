def returnAllRoutes():
    list = []
    file_object2 = open(r'/users/guero/desktop/universal/classworm/cs196124/extra/google_transit/routes.txt',"r+")
    for line in file_object2:
        split = line.split(',')
        if (split[0] != 'route_id'):
            list += (split[0])
            print(split[0])
    return list