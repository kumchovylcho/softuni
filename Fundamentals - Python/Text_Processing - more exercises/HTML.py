article_title = input()
content_of_article = input()
print(f"<h1>\n{4 * ' '}{article_title}\n</h1>")
print(f"<article>\n{4 * ' '}{content_of_article}\n</article>")
comment = input()
while comment != "end of comments":
    print(f"<div>\n{4 * ' '}{comment}\n</div>")
    comment = input()