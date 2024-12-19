from auto_prefetch import ForeignKey, Model
from django.contrib.auth import get_user_model
from django.core.files.storage import storages
from django.db import models
from django.urls import reverse_lazy

from codebase.base.utils.abstracts import (
    BasePageModel,
    BaseSubmoduleFolder,
)

User = get_user_model()


class Book(BaseSubmoduleFolder, submodule="books"):
    """Book model as folder"""

    pdf = models.FileField(storage=storages["private"], null=True, upload_to="books/")


class Chapter(BasePageModel):
    """Article model"""

    book = ForeignKey("books.Book", on_delete=models.CASCADE)
    can_be_shown_in_home = models.BooleanField(default=True)
    display = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse_lazy("chapter-detail", kwargs={"slug": self.slug})


def get_chapter_file_path(obj, filename: str):
    folder = obj.article.folder_name
    subfolder = obj.article.subfolder_name
    return f"books/{folder}/{subfolder}/{filename}"


class ChapterFile(Model):
    """Article file model"""

    chapter = ForeignKey("books.Chapter", on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    file = models.FileField(upload_to=get_chapter_file_path)

    def __str__(self):
        return self.name
