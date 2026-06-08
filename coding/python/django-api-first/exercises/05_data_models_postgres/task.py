"""Exercise starter for lesson: 05_data_models_postgres."""
from dataclasses import dataclass
from textwrap import dedent


@dataclass(frozen=True)
class ScoreRule:
    minimum: int
    maximum: int


def build_table_name(app_label: str, model_name: str) -> str:
    return f"{app_label}_{model_name.lower()}"


def validate_score(rule: ScoreRule, value: int) -> bool:
    return rule.minimum <= value <= rule.maximum


def relationship_summary(parent: str, child: str) -> str:
    return f"{child} has a ForeignKey to {parent}, so deleting the parent cascades to its rows."


def model_stub() -> str:
    return dedent(
        """
        class Submission(models.Model):
            batch = models.ForeignKey(CollectionBatch, on_delete=models.CASCADE)
            score = models.IntegerField()
            payload = models.JSONField(default=dict)
        """
    ).strip()


def run() -> None:
    print("Exercise: design Django ORM models with explicit schema choices.")
    rule = ScoreRule(0, 100)
    good_score = 88
    bad_score = 140

    print(f"- Table name: {build_table_name('backend_api', 'Submission')}")
    print(f"- Relationship: {relationship_summary('CollectionBatch', 'Submission')}")
    print(f"- Model stub: {model_stub()}")
    print(f"- Valid score? {good_score}: {validate_score(rule, good_score)}")
    print(f"- Valid score? {bad_score}: {validate_score(rule, bad_score)}")

    assert validate_score(rule, good_score) is True
    assert validate_score(rule, bad_score) is False
    print("Validation checked one accepted score and one rejected score.")


if __name__ == "__main__":
    run()
