See detailed information in readme of contract, product_contract, fieldservice_sale.

# On the product

Make sure your product is set to field service tracking option 'line' or 'recurring',
is a contract = true, and a contract template is set.

Invoice policy should be set on "quantity ordered" if you want to charge a constant fee.

Invoice policy should be set on "quantity delivered" if you want to charge based on a number of fsm orders.

Field service tracking should usually set on create a recurring order.


# On the contract

Invoiceable stages let you define, for products with invoice policy = quantity ordered, what stages should be invoiced. For instance, you may want to charge for last minute cancellation of orders.

FSM Location should be set.
