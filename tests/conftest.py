import pytest


@pytest.fixture(params=[{
        'CustomerName': 'Ivan Ivanov',
        'UpdatedCustomerName': 'FirstName',
        'ContactName': 'Elon Musk',
        'UpdatedContactName': 'ContactName',
        'Address': 'Forsterstr. 23',
        'UpdatedAddress': 'Address',
        'City': 'Moscow',
        'UpdatedCity': 'City',
        'PostalCode': '659101',
        'UpdatedPostalCode': 'PostalCode',
        'Country': 'Russian',
        'UpdatedCountry': 'Country'
}])
def prepare_for_update_db(ctx, request):
    yield request.param
    ctx.page.input_sql_statement(f"DELETE FROM Customers WHERE CustomerName = '{request.param['UpdatedCustomerName']}'")
    ctx.page.submit()

@pytest.fixture(params=[{
    'CustomerName': 'Maks Kuznetsov',
    'ContactName': 'Elon Musk',
    'Address': 'Forsterstr. 23',
    'City': 'Novosibirsk',
    'PostalCode': '659100',
    'Country': 'Russian'
}])
def prepare_db(ctx, request):
    yield request.param
    ctx.page.input_sql_statement(f"DELETE FROM Customers WHERE CustomerName = '{request.param['CustomerName']}'")
    ctx.page.submit()
