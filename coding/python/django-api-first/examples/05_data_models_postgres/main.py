"""Runnable example for lesson: 05_data_models_postgres."""
from dataclasses import dataclass
from textwrap import dedent


@dataclass(frozen=True)
class ModelField:
    name: str
    field_type: str
    note: str


@dataclass(frozen=True)
class ModelDefinition:
    name: str
    table_name: str
    fields: tuple[ModelField, ...]


def submission_model_snippet() -> str:
    return dedent(
        """
        class CollectionBatch(models.Model):
            source = models.CharField(max_length=40)
            created_at = models.DateTimeField(auto_now_add=True)

        class Submission(models.Model):
            batch = models.ForeignKey(CollectionBatch, on_delete=models.CASCADE, related_name='submissions')
            student_email = models.EmailField(db_index=True)
            score = models.IntegerField()
            payload = models.JSONField(default=dict)

            class Meta:
                ordering = ['-id']
                indexes = [models.Index(fields=['student_email', 'score'])]
        """
    ).strip()


def model_inventory() -> list[ModelDefinition]:
    return [
        ModelDefinition(
            "CollectionBatch",
            "collection_batch",
            (
                ModelField("source", "CharField(max_length=40)", "Track where submissions came from."),
                ModelField("created_at", "DateTimeField(auto_now_add=True)", "Preserve ingest timing."),
            ),
        ),
        ModelDefinition(
            "Submission",
            "submission",
            (
                ModelField("batch", "ForeignKey(CollectionBatch)", "Each submission belongs to one batch."),
                ModelField("student_email", "EmailField(db_index=True)", "Searchable identity column."),
                ModelField("payload", "JSONField(default=dict)", "Store raw API metadata."),
            ),
        ),
    ]


def migration_steps() -> list[str]:
    return [
        "python manage.py makemigrations",
        "python manage.py sqlmigrate backend_api 0001",
        "python manage.py migrate",
    ]


def main() -> None:
    print("Django ORM model example:")
    print(submission_model_snippet())
    print("\nModel inventory:")
    for model in model_inventory():
        print(f"- {model.name} -> db_table={model.table_name}")
        for field in model.fields:
            print(f"  * {field.name}: {field.field_type} ({field.note})")

    print("\nMigration workflow:")
    for step in migration_steps():
        print(f"- {step}")

    inventory = model_inventory()
    assert any(field.field_type.startswith("ForeignKey") for field in inventory[1].fields)
    assert migration_steps()[-1] == "python manage.py migrate"
    print("\nValidation: relationships and migration steps are present.")


if __name__ == "__main__":
    main()
