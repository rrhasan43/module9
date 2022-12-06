post = {
    'id': 100,
    'title': 'This is awsome title',
    'content': 'These are awsome contents',
    'author': 'awsome name',
    'category': 'awsome',
    'slug': 'awesome_title'
}

# post['sticky']= True
post.update({'sticky': True})
print(post)