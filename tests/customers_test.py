import pytest

from config.cfg import Base


class TestCustomer:
    @pytest.mark.parametrize(
        "sql,name,expected_address",
        [
            ("SELECT CustomerId,CustomerName,ContactName,Address,City,PostalCode, Country FROM Customers;", 'Giovanni Rovelli', 'Via Ludovico il Moro 22')
        ]
    )
    def test_find_address(self, ctx, sql, name, expected_address):
        ctx.open(Base.url)
        ctx.page.input_sql_statement(sql)
        ctx.page.submit()
        customers = ctx.page.get_customers()
        customer_address = ''
        for customer in customers.customers:
            if name == customer.contact_name:
                customer_address = customer.address
        assert expected_address == customer_address, 'Incorrect address'

    @pytest.mark.parametrize(
        "sql,expected_count",
        [
            ("SELECT CustomerId,CustomerName,ContactName,Address,City,PostalCode, Country FROM Customers where city='London';", 6)
        ]
    )
    def test_count_cities(self, ctx, sql, expected_count):
        ctx.open(Base.url)
        ctx.page.input_sql_statement(sql)
        ctx.page.submit()
        customers = ctx.page.get_customers()
        assert expected_count == len(customers.customers), 'Incorrect count rows'

    @pytest.mark.parametrize(
        "new_record,sql",
        [
            ("INSERT INTO Customers (CustomerName,ContactName,Address,City,PostalCode,Country) VALUES ('{CustomerName}','{ContactName}','{Address}','{City}','{PostalCode}','{Country}')", "SELECT CustomerId,CustomerName,ContactName,Address,City,PostalCode, Country FROM Customers WHERE CustomerName = '{CustomerName}';")
        ]
    )
    def test_insert_customer(self, ctx, prepare_db, new_record, sql):
        expected_params = prepare_db
        ctx.open(Base.url)
        self.__insert(ctx.page, new_record, expected_params)
        ctx.page.input_sql_statement(sql.format(CustomerName=expected_params['CustomerName']))
        ctx.page.submit()
        customers = ctx.page.get_customers().customers

        assert len(customers) > 0, "didn't insert new record"
        assert expected_params['CustomerName'] == customers[0].customer_name, 'Incorrect customer_name'
        assert expected_params['ContactName'] == customers[0].contact_name, 'Incorrect contact_name'
        assert expected_params['Address'] == customers[0].address, 'Incorrect address'
        assert expected_params['City'] == customers[0].city, 'Incorrect city'
        assert expected_params['PostalCode'] == customers[0].postal_code, 'Incorrect postal_code'
        assert expected_params['Country'] == customers[0].country, 'Incorrect country'

    @pytest.mark.parametrize(
        "insert_record, update_record,sql",
        [
            (
                    "INSERT INTO Customers (CustomerName,ContactName,Address,City,PostalCode,Country) VALUES ('{CustomerName}','{ContactName}','{Address}','{City}','{PostalCode}','{Country}')",
                    "UPDATE Customers SET CustomerName = '{CustomerName}', ContactName = '{ContactName}', Address = '{Address}',City='{City}',PostalCode='{PostalCode}',Country='{Country}' WHERE {condition};",
                    "SELECT CustomerId,CustomerName,ContactName,Address,City,PostalCode, Country FROM Customers WHERE CustomerName = '{CustomerName}';"
            )
        ]
    )
    def test_update_customer(self, ctx, prepare_for_update_db, insert_record, update_record, sql):
        ctx.open(Base.url)
        expected_params = prepare_for_update_db
        self.__insert(ctx.page, insert_record, expected_params)
        condition = f"CustomerName = '{expected_params['CustomerName']}'"
        sql_update_record = update_record.format(
            CustomerName=expected_params['UpdatedCustomerName'],
            ContactName=expected_params['UpdatedContactName'],
            Address=expected_params['UpdatedAddress'],
            City=expected_params['UpdatedCity'],
            PostalCode=expected_params['UpdatedPostalCode'],
            Country=expected_params['UpdatedCountry'],
            condition=condition
        )
        ctx.page.input_sql_statement(sql_update_record)
        ctx.page.submit()
        ctx.page.input_sql_statement(sql.format(CustomerName=expected_params['UpdatedCustomerName']))
        ctx.page.submit()
        customers = ctx.page.get_customers().customers

        assert len(customers) > 0, "didn't insert new record"
        assert expected_params['UpdatedCustomerName'] == customers[0].customer_name, 'Incorrect customer_name'
        assert expected_params['UpdatedContactName'] == customers[0].contact_name, 'Incorrect contact_name'
        assert expected_params['UpdatedAddress'] == customers[0].address, 'Incorrect address'
        assert expected_params['UpdatedCity'] == customers[0].city, 'Incorrect city'
        assert expected_params['UpdatedPostalCode'] == customers[0].postal_code, 'Incorrect postal_code'
        assert expected_params['UpdatedCountry'] == customers[0].country, 'Incorrect country'

    @pytest.mark.parametrize(
        "insert_record, delete_record,sql",
        [
            (
                    "INSERT INTO Customers (CustomerName,ContactName,Address,City,PostalCode,Country) VALUES ('Aleksandr Ivanov','Tom Ford','Lenina str. 1','Saint Petersburg','609101','Russian')",
                    "DELETE FROM Customers WHERE CustomerName = 'Aleksandr Ivanov'",
                    "SELECT CustomerId,CustomerName,ContactName,Address,City,PostalCode, Country FROM Customers WHERE CustomerName = 'Aleksandr Ivanov';"
            )
        ]
    )
    def test_delete_customer(self, ctx, insert_record, delete_record, sql):
        ctx.open(Base.url)
        ctx.page.input_sql_statement(insert_record)
        ctx.page.submit()
        ctx.page.input_sql_statement(sql)
        ctx.page.submit()
        customers = ctx.page.get_customers().customers
        assert len(customers) > 0, "didn't insert new record"
        assert 'Aleksandr Ivanov' == customers[0].customer_name, 'Incorrect customer_name'
        ctx.page.input_sql_statement(delete_record)
        ctx.page.submit()
        ctx.page.input_sql_statement(sql)
        ctx.page.submit()
        assert 'No result.' == ctx.page.empty_result()

    def __insert(self, page, insert_record, expected_params):
        sql_insert_record = insert_record.format(
            CustomerName=expected_params['CustomerName'],
            ContactName=expected_params['ContactName'],
            Address=expected_params['Address'],
            City=expected_params['City'],
            PostalCode=expected_params['PostalCode'],
            Country=expected_params['Country']
        )
        page.input_sql_statement(sql_insert_record)
        page.submit()
