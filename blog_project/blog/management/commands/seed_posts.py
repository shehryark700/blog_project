from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from blog.models import Comment, Post


SAMPLE_POSTS = [
    {
        'title': 'Welcome to Django Blog',
        'content': (
            "This is the first post on our brand new Django-powered blog!\n\n"
            "Django is a high-level Python web framework that encourages rapid "
            "development and clean, pragmatic design. In the coming posts we'll "
            "explore models, views, templates, authentication, and more."
        ),
    },
    {
        'title': 'Getting Started with Django Models',
        'content': (
            "Django models are the single, definitive source of information about "
            "your data. They contain the essential fields and behaviors of the data "
            "you're storing.\n\n"
            "In this post we cover defining fields, running migrations, and querying "
            "the database using Django's powerful ORM."
        ),
    },
    {
        'title': 'Building Templates with Django',
        'content': (
            "Django's template language lets you separate the design from the "
            "Python code, keeping your application clean and maintainable.\n\n"
            "We'll look at template inheritance, tags, filters, and how to organize "
            "static files like CSS and JavaScript."
        ),
    },
    {
        'title': 'User Authentication in Django',
        'content': (
            "Django ships with a full-featured authentication system out of the box, "
            "including login, logout, password management, and user registration.\n\n"
            "This post walks through wiring up the built-in auth views and customizing "
            "the templates to match your site's design."
        ),
    },
    {
        'title': 'Adding Comments and Search to Your Blog',
        'content': (
            "A blog isn't complete without a way for readers to leave comments and "
            "find the content they're looking for.\n\n"
            "We'll add a Comment model linked to posts, a simple search form that "
            "filters by title and content, and pagination to keep things tidy."
        ),
    },
    {
        'title': 'Deploying Your Django Application',
        'content': (
            "Once your blog is ready, it's time to share it with the world.\n\n"
            "This post covers preparing settings for production, collecting static "
            "files, and the basic steps for deploying to a hosting provider."
        ),
    },
]

SAMPLE_COMMENTS = [
    "Great post, thanks for sharing!",
    "This really helped me understand the concept better.",
    "Looking forward to the next one in this series.",
]


class Command(BaseCommand):
    help = 'Creates sample blog posts (and a demo author) for development.'

    def handle(self, *args, **options):
        author, created = User.objects.get_or_create(
            username='demo_author',
            defaults={'email': 'demo_author@example.com'},
        )
        if created:
            author.set_password('demopass123')
            author.save()
            self.stdout.write(self.style.SUCCESS('Created demo user "demo_author" (password: demopass123)'))

        created_count = 0
        for entry in SAMPLE_POSTS:
            post, was_created = Post.objects.get_or_create(
                title=entry['title'],
                defaults={
                    'author': author,
                    'content': entry['content'],
                    'status': 'published',
                },
            )
            if was_created:
                created_count += 1
                for body in SAMPLE_COMMENTS[:2]:
                    Comment.objects.create(post=post, author=author, body=body)

        self.stdout.write(self.style.SUCCESS(f'Created {created_count} sample posts.'))
