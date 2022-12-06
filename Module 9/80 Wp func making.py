def wp_paragraph(p_text):
    code = f'<!-- wp:paragraph --> <p><strong>{p_text}</p> <!-- /wp:paragraph -->'
    return code
demo = 'Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, '

p = wp_paragraph(demo)
print(p)
