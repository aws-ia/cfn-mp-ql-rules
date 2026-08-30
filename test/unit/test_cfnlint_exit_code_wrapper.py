from types import SimpleNamespace
from unittest.mock import Mock, patch

import pytest

from cfn_mp_ql_rules import cfnlint_exit_code_wrapper as wrapper


def test_load_cfn_lint_entry_point_with_select_api():
    expected = object()
    entry_point = Mock()
    entry_point.load.return_value = expected
    available = Mock()
    available.select.return_value = [entry_point]

    with patch.object(wrapper, "entry_points", return_value=available):
        assert wrapper._load_cfn_lint_entry_point() is expected

    available.select.assert_called_once_with(
        group="console_scripts", name="cfn-lint"
    )


def test_load_cfn_lint_entry_point_with_legacy_mapping_api():
    expected = object()
    other = SimpleNamespace(name="other", load=Mock())
    target = SimpleNamespace(name="cfn-lint", load=Mock(return_value=expected))

    with patch.object(
        wrapper,
        "entry_points",
        return_value={"console_scripts": [other, target]},
    ):
        assert wrapper._load_cfn_lint_entry_point() is expected


def test_main_adds_rule_path_and_maps_lint_findings_to_success(monkeypatch):
    observed_arguments = []

    def cfn_lint_entry_point():
        observed_arguments.extend(wrapper.sys.argv[1:])
        return 4

    monkeypatch.setattr(
        wrapper,
        "_load_cfn_lint_entry_point",
        lambda: cfn_lint_entry_point,
    )
    monkeypatch.setattr(
        wrapper.sys, "argv", ["wrapped-cfn-lint", "template.yaml"]
    )

    with pytest.raises(SystemExit) as raised:
        wrapper.main()

    assert raised.value.code == 0
    assert observed_arguments == [
        f"-a={wrapper.Path(wrapper.__file__).resolve().parent}",
        "template.yaml",
    ]
