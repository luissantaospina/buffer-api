from app.data_transfer_objects import PolicyDTO


def validate_policy(policy: PolicyDTO) -> bool:
    is_validate = True
    if policy.method not in ['FIFO', 'LIFO']:
        is_validate = False
    return is_validate
