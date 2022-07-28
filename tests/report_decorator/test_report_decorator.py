from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

from .mocks import list_mock, expected_return_simple, expected_return_complete


def test_decorar_relatorio():
    assert (
        ColoredReport(SimpleReport).generate(list_mock)
        == expected_return_simple
    )
    assert (
        ColoredReport(CompleteReport).generate(list_mock)
        == expected_return_complete
    )
