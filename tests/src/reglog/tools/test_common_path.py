import pytest

@pytest.mark.ut
def test_bucket_name_is_correctly_imported():
    # Given / When
    from reglog.tools.common_path import BUCKET_NAME

    expected_bucket_name = "logistic-regression-course"

    # Then
    assert BUCKET_NAME == expected_bucket_name
