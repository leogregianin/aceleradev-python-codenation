class CloudCost():

    def __init__(self):
        self.cost_msg_received = 0.00000040
        self.cost_function_per_exec = 0.0000002
        self.cost_function_per_second = 0.0002080
        self.count_function_execute = 2.0
        self.count_function_time = 3.0
        self.months = [1,2,3,4,5,6,7,8,9,10,11,12]

    def days_in_month(self, month):
        """
        Days per month
        Ignore bissexto year
        """
        if month in {1, 3, 5, 7, 8, 10, 12}:
            return 31
        if month == 2:
            return 28
        return 30

    def lambda_execution(self):
        return ((self.count_function_time * self.cost_function_per_second) + self.cost_function_per_exec)

    def app_execution(self, execution_times):
        return (((self.count_function_execute * self.lambda_execution()) + self.cost_msg_received) * execution_times)

    def month(self, execution_times, month_of_year):
        return self.app_execution(execution_times) * self.days_in_month(month_of_year)

    def year(self, execution_times):
        return [self.month(execution_times, month) for month in self.months]