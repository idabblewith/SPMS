from django.db import models

from common.models import CommonModel

# Create your models here.


class ChatRoom(CommonModel):
    """
    Chat Room Model Definition
    """

    users = models.ManyToManyField(
        "users.User",
        related_name="chat_rooms",
    )

    def __str__(self) -> str:
        return f"Chat Room - {self.users}"

    class Meta:
        verbose_name = "Chat Room"
        verbose_name_plural = "Chat Rooms"


class Comment(CommonModel):
    user = models.ForeignKey(
        "users.User",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,  # OR DELETE - CLARIFY
    )
    category = models.ForeignKey(
        "categories.ProjectCategory",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    project = models.ForeignKey(
        "projects.Project",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    text = models.CharField(max_length=500)
    ip_address = models.CharField(
        max_length=45,
        null=True,
        blank=True,
    )  # Will be sent from front-end
    is_public = models.BooleanField(default=True)
    is_removed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.user.first_name} | {self.category}"

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"


class DirectMessage(CommonModel):
    """
    Chat Room Message Model Definition
    """

    text = models.TextField()
    user = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="messages",
    )
    chat_room = models.ForeignKey(
        "communications.ChatRoom",
        on_delete=models.CASCADE,
        related_name="messages",
    )
    ip_address = models.CharField(
        max_length=45,
        null=True,
        blank=True,
    )  # Will be sent from front-end
    is_public = models.BooleanField(default=True)
    is_removed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.user} says {self.text}"

    class Meta:
        verbose_name = "Direct Message"
        verbose_name_plural = "Direct Messages"


class DirectMessageReaction(CommonModel):
    """
    Model definition for Reactions to Direct Messages
    """

    class DMReactionChoices(models.TextChoices):
        THUMBUP = "thumbup", "Thumbs Up"
        THUMBDOWN = "thumbdown", "Thumbs Down"
        HEART = "heart", "Heart"
        BROKENHEART = "brokenheart", "Broken Heart"
        HUNDRED = "hundred", "Hundred"
        CONFUSED = "confused", "Confused"
        FUNNY = "funny", "Funny"
        SUPRISED = "suprised", "Suprised"

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="dm_reactions",
    )
    direct_message = models.ForeignKey(
        "communications.DirectMessage",
        on_delete=models.CASCADE,
        related_name="dm_reactions",
    )
    reaction = models.CharField(
        max_length=30,
        choices=DMReactionChoices.choices,
    )

    def __str__(self) -> str:
        return f"Reaction to {self.direct_message}"

    class Meta:
        verbose_name = "Direct Message Reaction"
        verbose_name_plural = "Direct Message Reactions"


class CommentReaction(CommonModel):
    """
    Model definition for Reactions to Comments
    """

    class CommentReactionChoices(models.TextChoices):
        THUMBUP = "thumbup", "Thumbs Up"
        THUMBDOWN = "thumbdown", "Thumbs Down"
        HEART = "heart", "Heart"
        BROKENHEART = "brokenheart", "Broken Heart"
        HUNDRED = "hundred", "Hundred"
        CONFUSED = "confused", "Confused"
        FUNNY = "funny", "Funny"
        SUPRISED = "suprised", "Suprised"

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="comment_reactions",
    )
    comment = models.ForeignKey(
        "communications.Comment",
        on_delete=models.CASCADE,
        related_name="comment_reactions",
    )
    reaction = models.CharField(
        max_length=30,
        choices=CommentReactionChoices.choices,
    )

    def __str__(self) -> str:
        return f"Reaction to {self.comment}"

    class Meta:
        verbose_name = "Comment Reaction"
        verbose_name_plural = "Comment Reactions"
