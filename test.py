# def home():
#     posts = Posts.query.order_by(Posts.pub_date)
#     post1 = {'heading': '', 'subheading': '', 'author': '', 'date': '', 'show': '', 'postid': ''}
#     post2 = {'heading': '', 'subheading': '', 'author': '', 'date': '', 'show': '', 'postid': ''}
#     post3 = {'heading': '', 'subheading': '', 'author': '', 'date': '', 'show': '', 'postid': ''}
#     post4 = {'heading': '', 'subheading': '', 'author': '', 'date': '', 'show': '', 'postid': ''}
#     if posts.get(1):
#         post = posts.get(1)
#         post1 = {
#             'heading': post.heading,
#             'subheading': post.subheading,
#             'author': post.author,
#             'date': post.pub_date,
#             'show': 'true',
#             'postid': str(post.id)
#         }
#     if posts.get(2):
#         post = posts.get(2)
#         post2 = {
#             'heading': post.heading,
#             'subheading': post.subheading,
#             'author': post.author,
#             'date': post.pub_date,
#             'show': 'true',
#             'postid': str(post.id)
#         }
#     if posts.get(3):
#         post = posts.get(3)
#         post3 = {
#             'heading': post.heading,
#             'subheading': post.subheading,
#             'author': post.author,
#             'date': post.pub_date,
#             'show': 'true',
#             'postid': str(post.id)
#         }
#     if posts.get(4):
#         post = posts.get(4)
#         post4 = {
#             'heading': post.heading,
#             'subheading': post.subheading,
#             'author': post.author,
#             'date': post.pub_date,
#             'show': 'true',
#             'postid': str(post.id)
#         }
#     return render_template("index.html", post1=post1, post2=post2, post3=post3, post4=post4)

for i in id:
    post = posts.get(1)
    post1 = {
        'heading': post.heading,
        'subheading': post.subheading,
        'author': post.author,
        'date': post.pub_date,
        'show': 'true',
        'postid': str(post.id)
    }