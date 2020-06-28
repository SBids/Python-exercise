# 14. Write a Python function to create the HTML string with tags around the
# word(s).


def add_tags(tag, words):
    print("HTML string : %s" % words)
    print("HTML tag : %s" % tag)
    return "<%s>%s</%s>" % (tag, words, tag)


print(add_tags('i', 'Python Tutorial'))
