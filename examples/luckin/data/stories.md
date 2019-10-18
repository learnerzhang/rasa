## simple path with greet
* greet
  - utter_greet
* order_item{"coffee": "拿铁咖啡", "temperature": "热的"}
  - utter_working_on_it
  - action_order_item
  - utter_order_item
 
## simple path
* order_item{"coffee": "拿铁咖啡", "temperature": "热的"}
  - utter_working_on_it
  - action_order_item
  - utter_order_item

## coffee + temperature path with greet
* greet
  - utter_greet
* order_item{"coffee": "拿铁咖啡"}
  - utter_ask_temperature
* order_item{"temperature": "热的"}
  - utter_working_on_it
  - action_order_item
  - utter_order_item


## coffee + temperature path
* order_item{"coffee": "拿铁咖啡"}
  - utter_ask_temperature
* order_item{"temperature": "热的"}
  - utter_working_on_it
  - action_order_item
  - utter_order_item


## temperature + coffee path with greet
* greet
  - utter_greet
* order_item{"temperature": "热的"}
  - utter_ask_coffee
* order_item{"coffee": "拿铁咖啡"}
  - utter_working_on_it
  - action_order_item
  - utter_order_item

## temperature + coffee
* order_item{"temperature": "热的"}
  - utter_ask_coffee
* order_item{"coffee": "拿铁咖啡"}
  - utter_working_on_it
  - action_order_item
  - utter_order_item

## none + coffee + temperature path
* order_item
  - utter_ask_coffee
* order_item{"coffee": "拿铁咖啡"}
  - utter_ask_temperature
* order_item{"temperature": "热的"}
  - utter_working_on_it
  - action_order_item
  - utter_order_item

## none + coffee + temperature path with greet
* greet
  - utter_greet
* order_item
  - utter_ask_coffee
* order_item{"coffee": "拿铁咖啡"}
  - utter_ask_temperature
* order_item{"temperature": "热的"}
  - utter_working_on_it
  - action_order_item
  - utter_order_item

## ask_name
* ask_name               
  - utter_ask_name
 
## say goodbye
* goodbye
  - utter_goodbye
