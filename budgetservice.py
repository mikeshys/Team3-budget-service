class Period(object):
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end

    def overlapping_days(self, another):
        if self.start > self.end:
            return 0
        if self.end < another.start or self.start > another.end:
            return 0

        overlapping_end = self.end if self.end < another.end else another.end
        overlapping_start = self.start if self.start > another.start else another.start
        return (overlapping_end - overlapping_start).days + 1


class BudgetService(object):
    def query(self, start, end):
        period = Period(start, end)
        return sum(budget.overlapping_amount(period) for budget in self.get_budgets())

    def get_budgets(self):
        pass
