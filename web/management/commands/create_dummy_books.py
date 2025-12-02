import random

from django.core.management.base import BaseCommand

from web.models import Book


class Command(BaseCommand):
    help = "Bookモデルのダミーデータを100件作成します"

    def handle(self, *args, **options):
        titles = [
            "Python入門",
            "Django実践ガイド",
            "機械学習の基礎",
            "データサイエンス入門",
            "Web開発の教科書",
            "アルゴリズムとデータ構造",
            "クラウドコンピューティング",
            "セキュリティの基本",
            "ネットワーク入門",
            "データベース設計",
            "フロントエンド開発",
            "バックエンド開発",
            "DevOps入門",
            "コンテナ技術",
            "マイクロサービス",
            "API設計",
            "テスト駆動開発",
            "リファクタリング",
            "デザインパターン",
            "クリーンコード",
        ]

        authors = [
            "山田太郎",
            "佐藤花子",
            "鈴木一郎",
            "田中美咲",
            "高橋健太",
            "伊藤さくら",
            "渡辺大輔",
            "中村愛",
            "小林翔",
            "加藤真理",
        ]

        books_to_create = []
        for i in range(100):
            title = f"{random.choice(titles)} Vol.{i + 1}"
            author = random.choice(authors)
            selled_year = random.randint(2015, 2025)
            selled_month = random.randint(1, 12)

            books_to_create.append(
                Book(
                    title=title,
                    author=author,
                    selled_year=selled_year,
                    selled_month=selled_month,
                )
            )

        Book.objects.bulk_create(books_to_create)
        self.stdout.write(
            self.style.SUCCESS(f"ダミーデータを{len(books_to_create)}件作成しました")
        )
