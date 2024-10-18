from pathlib import Path

from django.conf import settings
from django.core.files import File
from django.db.models import Q
from huey import crontab
from huey.contrib import djhuey as huey
from django.utils.text import slugify

from ..base.telegram import Bot
from .models import Article, ArticleFile


def check_md_file_conventions(article_file_path: Path) -> bool:
    return all(
        (
            article_file_path.name[:2] in settings.LANGUAGE_CODES,
            len(article_file_path.read_text().split("\n")),
            article_file_path.read_text().strip().startswith("#"),
        )
    )


@huey.db_periodic_task(crontab(hour="0", minute="1"))
def sync_articles_dairly___():
    pass


def sync_articles_dairly():
    """
    Read the contents of the 'articles' submodule and save them in the database.
    To know which contents to sync, check out the setting SYNC_ARTICLE_FOLDERS.
    """

    # definitions and checks
    to_admin = "🔄 Syncing articles\n\n"

    folders = getattr(settings, "SYNC_ARTICLE_FOLDERS", ())

    if len(folders) == 0:
        Bot.to_admin(to_admin + "No folders found while syncing articles. Check SYNC_ARTICLE_FOLDERS")
        return

    try:
        iter(folders)
    except TypeError:
        Bot.to_admin(to_admin + "The variable for folders is not iterable. Check SYNC_ARTICLE_FOLDERS")
        return

    articles_path = getattr(settings, "ARTICLES_MARKDOWN_PATH", None)

    if not isinstance(articles_path, Path):
        Bot.to_admin(to_admin + "No path for articles found while syncing articles. Check ARTICLES_MARKDOWN_PATH")
        return

    if not articles_path.is_dir():
        Bot.to_admin(to_admin + "The 'articles' path is not a directory. Check ARTICLES_MARKDOWN_PATH")
        return

    # Scanning
    for folder in folders:
        folder_path = articles_path / folder

        if not folder_path.is_dir():
            to_admin += f"🔴 {folder} is not listed\n\n"
            continue

        for subfolder_path in folder_path.iterdir():
            if not subfolder_path.is_dir():
                continue

            body_replacements = {}
            to_admin += f"✍ {folder}/{subfolder_path.name}\n"
            db_article = Article.objects.get_or_create(folder=folder, subfolder=subfolder_path.name)[0]

            # Markdown files (.md) need to be proccessed first
            for md_file_path in (p for p in subfolder_path.iterdir() if p.name.endswith(".md")):
                if not check_md_file_conventions(md_file_path):
                    to_admin += f"⚠️ File '{md_file_path.name}' does not meet conventions"
                    continue

                lang_code = md_file_path.name[:2]
                title = md_file_path.read_text().split("\n")[0].replace("#", "").strip()
                body_text = "\n".join(md_file_path.read_text().split("\n")[1:]).strip()
                setattr(db_article, f"title_{lang_code}", title)
                setattr(db_article, f"slug_{lang_code}", slugify(title))
                setattr(db_article, f"body_{lang_code}", body_text)
                setattr(db_article, "folder", folder)
                setattr(db_article, "subfolder", subfolder_path.name)

            # The other files are proccessed afterwards
            for other_file_path in (p for p in subfolder_path.iterdir() if not p.name.endswith(".md")):
                db_articlefile = ArticleFile.objects.get_or_create(article=db_article, name=other_file_path.name)[0]
                db_articlefile.file = File(other_file_path.open(mode="rb"), name=other_file_path.name)
                db_articlefile.save()
                body_replacements[f"]({db_articlefile.name})"] = f"]({db_articlefile.file.url})"

            # Adjust article body field if the markdown file includes files.
            for local, remote in body_replacements.items():
                for lang_code in settings.LANGUAGE_CODES:
                    new_value = getattr(db_article, f"body_{lang_code}").replace(local, remote)
                    setattr(db_article, f"body_{lang_code}", new_value)

            # Save all object attributes in the database
            db_article.save()

    # Delete articles that could not be processed
    qs = Article.objects.filter(Q(title__in=[None, ""]) | Q(body__in=[None, ""]))
    if qs.count() > 0:
        to_admin += "\n😔Articles not possible to create:\n"
    for obj in qs:
        to_admin += f"{obj.folder}/{obj.subfolder}\n"
    qs.delete()

    Bot.to_admin(to_admin)