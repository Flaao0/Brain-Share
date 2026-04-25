from random import choice, randint

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils.text import slugify

from communities.models import StudentProfile
from mems.models import Meme
from notes.models import Category, Comment, Note


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = self._create_users()
        categories = self._create_categories()
        notes = self._create_notes(users, categories)
        self._create_comments(notes)
        self._create_memes(users)
        self.stdout.write(self.style.SUCCESS("Бд заполнено"))

    def _create_users(self):
        User = get_user_model()
        users = []

        if not User.objects.filter(username="admin").exists():
            admin = User.objects.create_superuser(
                "admin",
                "admin@example.com",
                "qwerty123",
            )
            StudentProfile.objects.get_or_create(user=admin)
            self.stdout.write("Это мы создали суперюзера")

        for i in range(1, 4):
            user, created = User.objects.get_or_create(
                username=f"user{i}",
                defaults={"email": f"user{i}@mail.com"},
            )

            if created:
                user.set_password("qwerty123")
                user.save()
                StudentProfile.objects.get_or_create(user=user)
                self.stdout.write(f"Создали юзера {user.username}")

            users.append(user)

        return users

    def _create_categories(self):
        names = ["Математика", "Программирование", "Физика"]
        categories = []

        for name in names:
            generated_slug = slugify(name, allow_unicode=True).replace(" ", "-")
            category, _ = Category.objects.get_or_create(
                slug=generated_slug,
                defaults={"name": name},
            )
            categories.append(category)

        self.stdout.write("Создали категории")
        return categories

    def _create_notes(self, users, categories):
        titles = ["Конспект лекции", "Практическая работа", "Шпаргалка по теме"]
        images = [
            "img/notes/note_1.jpg",
            "img/notes/note_2.jpg",
            "img/notes/note_3.jpg",
        ]
        notes = []

        for i in range(10):
            category = choice(categories)
            author = choice(users)
            note, _ = Note.objects.get_or_create(
                title=f"{choice(titles)} {i + 1}",
                defaults={
                    "content": "Полезный учебный материал для повторения темы.",
                    "image_path": choice(images),
                    "category": category,
                    "author": author,
                    "is_public": True,
                },
            )
            notes.append(note)

        self.stdout.write("Создали конспекты")
        return notes

    def _create_comments(self, notes):
        comments = [
            "Отличный материал, спасибо!",
            "Очень понятно объяснено.",
            "Добавил себе в закладки.",
            "Это помогло перед контрольной.",
        ]

        for _ in range(15):
            Comment.objects.create(
                note=choice(notes),
                text=choice(comments),
            )

        self.stdout.write("Создали комментарии")

    def _create_memes(self, users):
        meme_titles = [
            "Когда дедлайн завтра",
            "Перед экзаменом в 3 ночи",
            "Лаба сдана с первого раза",
            "Когда преподаватель похвалил",
        ]
        meme_images = [
            "img/mems/exam.jpg",
            "img/mems/session.jpg",
            "img/mems/study.jpg",
            "img/mems/success.jpg",
        ]

        for i in range(8):
            Meme.objects.get_or_create(
                title=f"{choice(meme_titles)} #{i + 1}",
                defaults={
                    "image_path": choice(meme_images),
                    "author": choice(users),
                    "likes": randint(0, 250),
                },
            )

        self.stdout.write("Создали мемы")
