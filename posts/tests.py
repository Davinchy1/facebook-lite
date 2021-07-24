from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from posts.models import Post, Share, Comment, Like

class PostTests(APITestCase):
    def test_create_post(self):
        """
        Ensure we can create a new tweet object.
        """
        user = User.objects.create_user(username="davinchy", password="johnson.py")

        url = reverse('post-list')
        data = {'text': 'DabApps', "user": user.id}
        response = self.client.post(url, data, format='json')
        response_data = response.json()
        print("COMPLETE")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().text, data['text'])
        self.assertEqual(response_data['text'], data['text'])

    def test_put_post(self):
        """
        Ensure we can create a new tweet object.
        """
        user = User.objects.create_user(username="davinchy", password="johnson.py")
        post = Post.objects.create(text="azad testing game ", user=user)

        url = reverse('post-detail',kwargs={"pk":post.id})
        data = {'text': 'For this Lagos?', "user": user.id, "post": post.id}
        response = self.client.put(url, data, format='json')
        response_data = response.json()
        print(response_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(Tweet.objects.count(), 1)
        # self.assertEqual(Tweet.objects.get().text, data['text'])
        # self.assertEqual(response_data['text'], data['text'])


    def test_patch_post(self):
        """
        Ensure we can create a new tweet object.
        """
        user = User.objects.create_user(username="davinchy", password="johnson.py")
        post = Post.objects.create(text="it's a testing game ", user=user)

        url = reverse('post-detail',kwargs={"pk":post.id})
        data = {'text': 'For this Lagos?', "user": user.id, "post": post.id}
        response = self.client.patch(url, data, format='json')
        response_data = response.json()
        print(response_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_1post(self):
        """
        Ensure we can create a new tweet object.
        """
        user = User.objects.create_user(username="davinchy", password="johnson.py")
        post = Post.objects.create(text="File! issa testing game ", user=user)

        url = reverse('post-detail',kwargs={"pk":post.id})
        # data = {'text': 'DabApps', "user": user.id}
        response = self.client.get(url, format='json')
        response_data = response.json()
        print(response_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Post.objects.count(), 1)
        # self.assertEqual(response_data[0]["text"], tweet.text)


    def test_get_post(self):
        """
        Ensure we can create a new post object.
        """
        user = User.objects.create_user(username="davinchy", password="johnson.py")
        post = Post.objects.create(text="azad testing game ", user=user)

        url = reverse('post-detail',kwargs={"pk":post.id})
        # data = {'text': 'DabApps', "user": user.id}
        response = self.client.get(url, format='json')
        response_data = response.json()
        print(response_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    
    def test_delete_post(self):
        """
        Ensure we can create a new post object.
        """
        user = User.objects.create_user(username="davinchy", password="johnson.py")
        post = Post.objects.create(text="testing game", user=user)

        url = reverse('post-detail', kwargs={'pk': post.id})
        response = self.client.delete(url, format='json')
        # response_data = response.json()
        # print(response_data)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class ShareTests(APITestCase):
    def test_create_retweet(self):
        """
        Ensure we can create a new retweet object.
        """
        user = User.objects.create_user(username="davinchy", password="johnson.py")
        post = Post.objects.create(text="this is a simple post", user=user)

        url = reverse('share-list')
        data = {'post': post.id, "user": user.id}
        response = self.client.post(url, data, format='json')
        response_data = response.json()
        print(response_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_get_share(self):
        """
        Ensure we can GET a new share object.
        """
        user = User.objects.create_user(username="davinchy", password="johnson.py")
        post = Post.objects.create(text="this is a simple post", user=user)

        url = reverse('share-list')
        data = {'post': post.id, "user": user.id}
        response = self.client.get(url, data, format='json')
        response_data = response.json()
        print(response_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        
    def test_delete_share(self):
        """
        Ensure we can GET a new share object.
        
        """
        user = User.objects.create_user(username="davinchy", password="johnson.py")
        post = Post.objects.create(text="created this post", user=user)
        share = Share.objects.create(user=user, post=post)

        url = reverse('like-detail', kwargs={"pk": share.id})
        # data = {'post': post.id, "like": like.id}
        response = self.client.delete(url, format='json')
        # response_data = response.json()
        # print(response_data)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class LikeTests(APITestCase):
    def test_create_like(self):
        """
        Ensure we can create a new like object.
        """
        user = User.objects.create_user(username="davinchy", password="johnson.py")
        post = Post.objects.create(text="created this post", user=user)

        url = reverse('like-list')
        data = {'post': post.id, "user": user.id}
        response = self.client.post(url, data, format='json')
        response_data = response.json()
        print(response_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_get_like(self):
        """
        Ensure we can GET a new like object.
        """
        user = User.objects.create_user(username="davinchy", password="johnson.py")
        post = Post.objects.create(text="my own post test", user=user)

        url = reverse('like-list')
        data = {'post': post.id, "user": user.id}
        response = self.client.get(url, data, format='json')
        response_data = response.json()
        print(response_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_1like(self):
        """
        Ensure we can GET a new like object.
        """
        user = User.objects.create_user(username="davinchy", password="johnson.py")
        post = Post.objects.create(text="django don loud ooo!!!", user=user)

        url = reverse('like-list')
        data = {'post': post.id, "user": user.id}
        response = self.client.get(url, data, format='json')
        response_data = response.json()
        print(response_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_delete_like(self):
        """
        Ensure we can GET a new like object.
        
        """
        user = User.objects.create_user(username="davinchy", password="johnson.py")
        post = Post.objects.create(text="created this post", user=user)
        like = Like.objects.create(user=user, post=post)

        url = reverse('like-detail', kwargs={"pk": like.id})
        # data = {'post': post.id, "like": like.id}
        response = self.client.delete(url, format='json')
        # response_data = response.json()
        # print(response_data)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CommentTests(APITestCase):
    def test_create_comment(self):
        """
        Ensure we can GET a new comment object.
        .
        """
        user = User.objects.create_user(username="davinchy", password="johnson.py")
        post = Post.objects.create(text="this is a comment", user=user)

        url = reverse('comment-list')
        data = {'post': post.id, "user": user.id}
        response = self.client.post(url, data, format='json')
        response_data = response.json()
        print(response_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_get_comment(self):
        """
        Ensure we can GET a new post object.
        """
        user = User.objects.create_user(username="davinchy", password="johnson.py")
        post = Post.objects.create(text="this is a simple post", user=user)

        url = reverse('comment-list')
        data = {'post': post.id, "user": user.id}
        response = self.client.get(url, data, format='json')
        response_data = response.json()
        print(response_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_delete_comment(self):
        """
        Ensure we can GET a new post object.
        """
        user = User.objects.create_user(username="davinchy", password="johnson.py")
        post = Post.objects.create(text="create a post", user=user)
        comment = Comment.objects.create(user=user, post=post, text="e go better!")

        url = reverse('comment-detail', kwargs={"pk": comment.id})
        # data = {'post': post.id, "like": like.id}
        response = self.client.delete(url, format='json')
        # response_data = response.json()
        # print(response_data)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
