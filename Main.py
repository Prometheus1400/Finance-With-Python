import matplotlib.pyplot as plt

# This program will simulate and help you decide investment amounts based on your income

class InvestmentAccount:
    # attributes N/A

    # constructor
    def __init__(self,amount,return_rate,weekly_invest=0):
        self.amount = amount
        self.return_rate = return_rate
        self.weekly_invest = weekly_invest
    def __str__(self):
        return f"broker account of ${self.amount} with an average annual return of {self.return_rate}%"

    # methods
    # this method creates a list of values for the next x years
    def get_future_list(self,num_years):
        account_val_list = []
        current_val = self.amount
        mult_fact = 1 + self.return_rate/100
        for i in range(num_years):
            account_val_list.append(current_val)
            current_val = round(current_val * mult_fact,2) + self.weekly_invest*52
        return account_val_list

    # this method will draw a graph representing the value of the account for the specified number of years
    def graph_account(self,num_years):
        # first a calculation of the value every year must be made
        value_list = self.get_future_list(num_years)
        plt.plot(value_list)
        plt.title('Account Value vs Time')
        plt.xlabel('Years From Now')
        plt.ylabel('Account Value (US dollar)')
        plt.ticklabel_format(useOffset=False, style='plain')
        plt.show()


# amount investing / to invest
invest_amt = 3870
# average annual return rate
invest_rtn = 8
# amount to invest weekly
recurring = 1000


my_account = InvestmentAccount(invest_amt,invest_rtn,recurring)
my_account.graph_account(40)