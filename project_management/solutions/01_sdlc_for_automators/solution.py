STAGES = ['Plan', 'Build', 'Test', 'Review', 'Release', 'Operate', 'Improve']


def before_release() -> list[str]:
    return STAGES[:5]
