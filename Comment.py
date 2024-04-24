class Comment:

    count = 0

    def __init__(self, text, count):
        self.text = text
        self.count = count

    def upcount(self):
        self.count+=1

    @staticmethod
    def merge_comments(text1, text2):
        return f"{text1} {text2}"
    

my_comment = Comment("My comment",5)
print(my_comment.count)
his_comment = Comment("His comment",3)

print(my_comment.count, his_comment.count)
# print(Comment.merge_comments(my_comment.text, his_comment.text))

# my_comment.upcount()
# print(my_comment.count, his_comment.count)
