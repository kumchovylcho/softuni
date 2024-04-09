from unittest import TestCase, main

from tests.social_media import SocialMedia


class TestSocialMedia(TestCase):

    def setUp(self):
        self.social_media = SocialMedia("Tamer", "YouTube", 100, "program")

    def test_successful_initialization(self):
        self.assertEqual(self.social_media._username, "Tamer")
        self.assertEqual(self.social_media._platform, "YouTube")
        self.assertEqual(self.social_media._followers, 100)
        self.assertEqual(self.social_media._content_type, "program")
        self.assertEqual(self.social_media._posts, [])

    def test_unsuccessful_initialization(self):
        with self.assertRaises(ValueError) as ve:
            self.social_media = SocialMedia("Tamer", "Wrong", 100, "program")

        self.assertEqual(str(ve.exception), "Platform should be one of ['Instagram', 'YouTube', 'Twitter']")


        with self.assertRaises(ValueError) as ve:
            self.social_media.followers = -1

        self.assertEqual(str(ve.exception), "Followers cannot be negative.")

    def test_create_post(self):
        response = self.social_media.create_post("test")
        self.assertEqual(1, len(self.social_media._posts))
        self.assertEqual("New program post created by Tamer on YouTube.", response)

    def test_invalid_post_index(self):
        response = self.social_media.like_post(1)
        self.assertEqual("Invalid post index.", response)

    def test_max_likes_on_post_reached(self):
        self.social_media.create_post("test")
        for _ in range(10):
            self.social_media.like_post(0)

        response = self.social_media.like_post(0)
        self.assertEqual("Post has reached the maximum number of likes.", response)

    def test_like_a_post(self):
        self.social_media.create_post("test")

        response = self.social_media.like_post(0)
        self.assertEqual("Post liked by Tamer.", response)
        self.assertEqual(self.social_media._posts[0]["likes"], 1)

    def test_invalid_comment(self):
        self.social_media.create_post("test")

        response = self.social_media.comment_on_post(0, "test")
        self.assertEqual("Comment should be more than 10 characters.", response)

    def test_successful_comment(self):
        self.social_media.create_post("test")

        response = self.social_media.comment_on_post(0, "test test test")
        self.assertEqual("Comment added by Tamer on the post.", response)
        self.assertEqual(1, len(self.social_media._posts[0]["comments"]))


if __name__ == '__main__':
    main()