# main.py
import argparse
from models import initDb, addTransaction, queryTransactions

def main():
    initDb()
    
    parser = argparse.ArgumentParser(description="Transaction Manager")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser('add', help='Add a new transaction')
    add_parser.add_argument('date', type=str, help='Date of the transaction (YYYY-MM-DD)')
    add_parser.add_argument('category', type=str, help='Category of the transaction')
    add_parser.add_argument('amount', type=float, help='Amount of the transaction')
    add_parser.add_argument('description', type=str, nargs='?', default='', help='Description of the transaction')

    query_parser = subparsers.add_parser('query', help='Query transactions')
    query_parser.add_argument('query', type=str, help='SQL query to execute')

    args = parser.parse_args()

    if args.command == 'add':
        addTransaction(args.date, args.category, args.amount, args.description)
        print("Transaction added successfully.")
    elif args.command == 'query':
        results = queryTransactions(args.query)
        for row in results:
            print(row)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
