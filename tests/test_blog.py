from app.models import Blog,User
from app import db

def setUp(self):

    self.user_James = User(username = 'James',password = 'potato', email = 'james@ms.com')
    self.new_blog = Blog(title='Review for movies',subtitle='This movie is the best thing since sliced bread',content='sipendi ujinga kabisa',user = self.user_James )

def tearDown(self):
    Blog.query.delete()
    User.query.delete()

def test_check_instance_variables(self):
    self.assertEquals(self.new_blog.title,'Review for movies')
    self.assertEquals(self.new_blog.subtitle,'This movie is the best thing since sliced bread')
    self.assertEquals(self.new_blog.content,'Sipendi ujinga kabisa')
    self.assertEquals(self.new_review.user,self.user_James)

def test_save_blog(self):
    self.new_blog.save_blog()
    self.assertTrue(len(Blog.query.all())>0)

def test_get_blog_by_id(self):

        self.new_blog.save_blog()
        got_blog = Blog.get_blog (12345)
        self.assertTrue(len(got_blog) == 1)
