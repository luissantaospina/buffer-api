from app.data_transfer_objects import PolicyDTO
from app.exceptions import UnsupportedPolicy


def validate_policy(policy: PolicyDTO) -> None:
    if policy.method not in ['FIFO', 'LIFO']:
        raise UnsupportedPolicy('The policy is not supported')
