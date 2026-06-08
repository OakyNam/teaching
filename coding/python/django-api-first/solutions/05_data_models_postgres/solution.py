"""Reference solution for lesson: 05_data_models_postgres."""
from dataclasses import dataclass
from textwrap import dedent


@dataclass(frozen=True)
class ModelPair:
    parent: str
    child: str
    on_delete: str


def model_solution_snippet() -> str:
    return dedent(
        """
        class Project(models.Model):
            name = models.CharField(max_length=80, unique=True)
            slug = models.SlugField(unique=True)

        class Submission(models.Model):
            project = models.ForeignKey(Project, on_delete=models.PROTECT, related_name='submissions')
            student_email = models.EmailField(db_index=True)
            score = models.PositiveIntegerField()
            created_at = models.DateTimeField(auto_now_add=True)

            class Meta:
                ordering = ['-created_at']
                constraints = [models.CheckConstraint(check=models.Q(score__lte=100), name='score_lte_100')]
        """
    ).strip()


def migration_summary() -> list[str]:
    return [
        "makemigrations generates a migration file from model changes.",
        "sqlmigrate previews the PostgreSQL SQL before running it.",
        "migrate applies the schema change in dependency order.",
    ]


def validate_pair(pair: ModelPair) -> bool:
    return pair.parent != pair.child and pair.on_delete in {"CASCADE", "PROTECT", "SET_NULL"}


def run() -> None:
    pair = ModelPair("Project", "Submission", "PROTECT")
    broken = ModelPair("Submission", "Submission", "DROP")
    print("Model solution:")
    print(model_solution_snippet())
    print("\nMigration summary:")
    for line in migration_summary():
        print(f"- {line}")

    assert validate_pair(pair) is True
    assert validate_pair(broken) is False
    print("\nValidation: model relationships and deletion rules were checked.")


if __name__ == "__main__":
    run()
