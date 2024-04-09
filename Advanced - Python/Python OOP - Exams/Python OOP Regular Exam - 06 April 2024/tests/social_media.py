class SocialMedia:
    def __init__(self, username: str, platform: str, followers: int, content_type: str):
        self._username = username
        self._platform = None
        self._validate_and_set_platform(platform)
        self._followers = followers
        self._content_type = content_type
        self._posts = []

    @property
    def platform(self):
        return self._platform

    @platform.setter
    def platform(self, value):
        self._validate_and_set_platform(value)

    @property
    def followers(self):
        return self._followers

    @followers.setter
    def followers(self, value):
        if value < 0:
            raise ValueError("Followers cannot be negative.")
        self._followers = value

    def _validate_and_set_platform(self, value):
        allowed_platforms = ['Instagram', 'YouTube', 'Twitter']
        if value not in allowed_platforms:
            raise ValueError(f"Platform should be one of {allowed_platforms}")
        self._platform = value

    def create_post(self, post_content: str):
        new_post = {'content': post_content, 'likes': 0, 'comments': []}
        self._posts.append(new_post)
        return f"New {self._content_type} post created by {self._username} on {self._platform}."

    def like_post(self, post_index: int):
        if 0 <= post_index < len(self._posts):
            post = self._posts[post_index]
            if post['likes'] < 10:
                post['likes'] += 1
                return f"Post liked by {self._username}."
            else:
                return f"Post has reached the maximum number of likes."
        else:
            return "Invalid post index."

    def comment_on_post(self, post_index: int, comment: str):
        post = self._posts[post_index]
        if len(comment) > 10:
            post['comments'].append({'user': self._username, 'comment': comment})
            return f"Comment added by {self._username} on the post."

        return "Comment should be more than 10 characters."
