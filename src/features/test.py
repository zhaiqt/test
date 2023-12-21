from sklearn.ensemble import RandomForestRegressor

def create_list():
    item_list = [
        "rice",
        "chicken",
        "egg",
        "hotdog",
        "bean",
    ]
    return item_list


item_list = create_list()
for item in item_list:
    print(str(item))
