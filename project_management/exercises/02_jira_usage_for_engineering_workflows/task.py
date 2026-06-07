TICKET = {
    'summary': 'Automate switch inventory collection',
    'status': 'In Progress',
    'acceptance_criteria': ['Pull SNMP identity', 'Store results', 'Document validation'],
}


def is_ready_for_review(ticket: dict[str, object]) -> bool:
    raise NotImplementedError
