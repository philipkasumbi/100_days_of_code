facebook_posts = [
    {"likes": 21, "comments":2},
    {"likes": 13, "comments":2, "shares": 8},
    {"likes": 33, "comments":2, "shares": 1},
    {"comments":12, "shares": 5},
    {"comments":21, "shares": 7},
    {"likes": 19, "comments":10}
]
total_likes = 0
for post in facebook_posts:
    try:
        total_likes += post["likes"]
    except KeyError:
        post["likes"] = 0
        total_likes += post["likes"]
print(total_likes)