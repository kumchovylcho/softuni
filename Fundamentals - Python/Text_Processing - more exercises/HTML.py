def open_or_close_tag(tag: str, is_open: bool) -> str:
    return f"<{tag}>" if is_open else f"</{tag}>"


def create_tag_with_content(tag: str, empty_space: str, content: str) -> str:
    return (f"{open_or_close_tag(tag, True)}\n"
            f"{empty_space}"
            f"{content}\n"
            f"{open_or_close_tag(tag, False)}"
            )


spacing = 4 * " "
title_tag = "h1"
article_tag = "article"
comment_tag = "div"
end_of_comments_command = "end of comments"

for content_tag, content_text in ((title_tag, input()), (article_tag, input())):
    print(create_tag_with_content(content_tag, spacing, content_text))

comment = input()
while comment != end_of_comments_command:
    print(create_tag_with_content(comment_tag, spacing, comment))
    comment = input()



# article_title = input()
# content_of_article = input()
# print(f"<h1>\n{4 * ' '}{article_title}\n</h1>")
# print(f"<article>\n{4 * ' '}{content_of_article}\n</article>")
# comment = input()
# while comment != "end of comments":
#     print(f"<div>\n{4 * ' '}{comment}\n</div>")
#     comment = input()