from app.data_transfer_objects import PolicyDTO
from app.exceptions import UnsupportedPolicy
from app.enums import PolicyEnum


def validate_policy(policy: PolicyDTO) -> None:
    policies = [policy.value for policy in PolicyEnum.__members__.values()]

    if policy.method not in policies:
        raise UnsupportedPolicy('The policy is not supported')
