import pytest
from operation import Operation

@pytest.mark.parametrize(
    "cents, op_type, description, expected_str_prefix",
    [
        (1122200, 'credit', 'ATM deposit', '[+]'),
        (50000, 'debit', 'Withdrawal', '[-]'),
        (123456, 'Credit', 'Case insensitive credit', '[+]'),
        (98765, 'Debit', 'Case insensitive debit', '[-]'),
    ]
)
def test_operacao_valida(cents, op_type, description, expected_str_prefix):
    op = Operation(cents, op_type, description)
    
    assert op.cents == cents
    assert op.op_type.value == op_type.lower()  # ajustado para lidar com Enum
    assert op.description == description
    assert str(op).startswith(expected_str_prefix)
