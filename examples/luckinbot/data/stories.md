## simple path with greet
* greet
  - utter_greet
* order_coffee{"coffee": "拿铁咖啡", "temperature": "加冰", "sugar": "加糖"}
  - utter_working_on_it
  - action_order_item
  - utter_order_item
 
## simple path
* order_coffee{coffee": "拿铁咖啡", "temperature": "不加冰", "sugar": "加糖"}
  - utter_working_on_it
  - action_order_item
  - utter_order_item

## coffee + temperature path with greet
* greet
  - utter_greet
* order_coffee{"coffee": "拿铁咖啡"}
  - utter_ask_temperature
* order_coffee{"temperature": "不加冰"}
  - utter_ask_sugar
* order_coffee{"sugar": "加糖"} 
  - utter_working_on_it
  - action_order_item
  - utter_order_item


## coffee + temperature path
* order_coffee{"coffee": "拿铁咖啡"}
  - utter_ask_temperature
* order_coffee{"temperature": "加冰"}
  - utter_ask_sugar
* order_coffee{"sugar": "半糖"} 
  - utter_working_on_it
  - action_order_item
  - utter_order_item


## temperature + coffee path with greet
* greet
  - utter_greet
* order_coffee{"temperature": "不加冰"}
  - utter_ask_coffee
* order_coffee{"coffee": "拿铁咖啡"}
  - utter_ask_sugar
* order_coffee{"sugar": "加糖"}
  - utter_working_on_it
  - action_order_item
  - utter_order_item


## none + coffee + temperature path with greet
* greet
  - utter_greet
* order_coffee
  - utter_ask_coffee
* order_coffee{"coffee": "拿铁咖啡"}
  - utter_ask_temperature
* order_coffee{"temperature": "加冰"}
  - utter_ask_sugar
* order_coffee{"sugar": "加糖"} 
  - utter_working_on_it
  - action_order_item
  - utter_order_item


* greet
  - utter_greet
* order_tea{"tea": "大红袍牛乳茶"}
  - utter_working_on_it
  - action_order_item
  - utter_order_item 

* greet
  - utter_greet
* order_tea
  - utter_ask_tea
* order_tea{"tea": "美人玛奇朵"}
  - utter_working_on_it
  - action_order_item
  - utter_order_item

* order_tea{"tea": "大红袍牛乳茶"}
  - utter_working_on_it
  - action_order_item
  - utter_order_item

## ask_name
* ask_name               
  - utter_ask_name
 
## say goodbye
* goodbye
  - utter_goodbye
