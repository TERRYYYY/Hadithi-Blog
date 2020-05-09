class Blog:

    all_blogs = []


    def save_blogs(self):
        Blog.all_blogs.append(self)


    @classmethod
    def clear_blogs(cls):
        Blog.all_blogs.clear()
    
    @classmethod
    def get_blogs(cls,id):

        response = []

        for blog in cls.all_blogs:
            if blog.id == id:
                response.append(blog)

        return response