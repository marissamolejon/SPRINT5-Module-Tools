"""
Exercise: Type-checking with mypy - Bank Accounts
Sprint 5 Prep
 
The original code had several bugs:
- open_account was called without the `balances` argument
- open_account was called with a float (9.13) and a string ("£7.13") instead of int pence
- format_pence_as_str was called instead of format_pence_as_string
"""
 
def open_account(balances: dict[str, int], name: str, amount: int) -> None:
    balances[name] = amount
 
 
def sum_balances(accounts: dict[str, int]) -> int:
    total = 0
    for name, pence in accounts.items():
        print(f"{name} had balance {pence}")
        total += pence
    return total
 
 
def format_pence_as_string(total_pence: int) -> str:
    if total_pence < 100:
        return f"{total_pence}p"
    pounds = int(total_pence / 100)
    pence = total_pence % 100
    return f"£{pounds}.{pence:02d}"
 
 
balances: dict[str, int] = {
    "Sima": 700,
    "Linn": 545,
    "Georg": 831,
}
 
# Fixed: added balances as first argument, and converted values to integer pence
open_account(balances, "Tobi", 913)   # £9.13 = 913 pence
open_account(balances, "Olya", 713)   # £7.13 = 713 pence
 
total_pence = sum_balances(balances)
total_string = format_pence_as_string(total_pence)  # Fixed: was format_pence_as_str
 
print(f"The bank accounts total {total_string}")
 