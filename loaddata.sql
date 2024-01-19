SELECT * FROM bangazonapi_order WHERE order_type_id NOT IN (SELECT id FROM bangazonapi_ordertype);

SELECT DISTINCT order_type_id FROM bangazonapi_order WHERE order_type_id NOT IN (SELECT id FROM bangazonapi_ordertype);

SELECT DISTINCT order_type_id FROM bangazonapi_order WHERE order_type_id NOT IN (SELECT id FROM bangazonapi_ordertype);

DELETE FROM bangazonapi_item WHERE id = 1;
