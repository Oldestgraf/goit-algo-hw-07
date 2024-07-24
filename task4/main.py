class Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False

    def add_reply(self, text):
        self.replies.append(text)

    def remove_reply(self):
        self.is_deleted = True
        self.text = "Цей коментар було видалено."

    def display(self, space = 0):
        if self.is_deleted:
            print(" " * space + f"{self.text}")
        else:
            print(" " * space + f"{self.author}: {self.text}")
        for reply in self.replies:
            reply.display(space + 4)


root_comment = Comment("Яка чудова книга!", "Бодя")
reply1 = Comment("Книга повне розчарування :(", "Андрій")
reply2 = Comment("Що в ній чудового?", "Марина")

root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
reply1.add_reply(reply1_1)

reply1.remove_reply()

root_comment.display()
