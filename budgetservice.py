class BudgetService(object):
    def query(self, start, end):
        if start > end:
            return 0

        total_amount = 0
        for budget in self.get_budgets():
            days_of_budget = budget.days()
            budget_last_day = budget.first_day().replace(day=days_of_budget)

            daily_amount = budget.amount / days_of_budget

            if end < budget.first_day() or start > budget_last_day:
                break

            overlapping_end = end if end < budget_last_day else budget_last_day
            overlapping_start = start if start > budget.first_day() else budget.first_day()
            overlapping_days = ((overlapping_end - overlapping_start).days + 1)
            total_amount += round(daily_amount * overlapping_days, 2)

        return total_amount

    def get_budgets(self):
        pass
