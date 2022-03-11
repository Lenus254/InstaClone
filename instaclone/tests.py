from django.test import TestCase
from .models import Post,Profile,Following,Comments
from django.contrib.auth.models import User


class FollowingTestClass(TestCase):
    def setUp(self):
        self.lenus=Following(username='lenus',followed='len')
                            
    def test_instance(self):
        self.assertTrue(isinstance(self.lenus,Following))
        
    def test_save_follower(self):
        self.lenus.save_follower()
        followers=Following.objects.all()
        self.assertTrue(len(followers) > 0)
        

class CommentTestClass(TestCase):
    def setUp(self):
        self.first=Comments(post=1,
                            username='lenas',
                            comment='Great post',
                            date='May 24, 2019, 12:41 a.m.',
                            count=0)

    def test_instance(self):
        self.assertTrue(isinstance(self.first,Comments))
        
        
class ProfileTestClass(TestCase):
    def setUp(self):
        user=User(username='lenus',first_name='langat',last_name='len')
        self.new_profile=Profile(user=user,profile_pic='/media/images/default.jpeg', bio='travel')
        
    def test_instance(self):
        self.assertTrue(isinstance( self.new_profile,Profile))
        

class CommentsTestClass(TestCase):

    def setUp(self):
        
        user=User(username='lenus',first_name='langat',last_name='len')
        self.comments=Comments.objects.create(post=1,username=user,comment='The best image', date=None,count=1)
        

        

    def test_instance(self):
            """Testing instance"""
            self.assertTrue(isinstance(self.comments, Comments))

    
   