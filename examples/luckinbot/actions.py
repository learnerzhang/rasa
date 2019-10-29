#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-16 11:03
# @Author  : zhangzhen
# @Site    :
# @File    : actions.py.py
# @Software: PyCharm
from typing import List, Text

from rasa_sdk.events import SlotSet
from rasa_sdk import Action
from rasa_sdk import Tracker


class OrderAction(Action):
    RANDOMIZE = True

    def name(self):
        # type: () -> Text
        return "action_order_item"

    def run(self, dispatcher, tracker, domain):
        # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
        coffee = tracker.get_slot('coffee')
        tea = tracker.get_slot('tea')
        number = tracker.get_slot('number')
        temperature = tracker.get_slot('temperature')
        sugar = tracker.get_slot('sugar')

        temperature = temperature if temperature else "None"
        number = number if number else 1
        coffee = coffee if coffee else "None"
        sugar = sugar if sugar else "None"
        if tea:
            return [SlotSet("matches", "{}杯 - {}".format(number, tea))]
        elif coffee:
            return [SlotSet("matches", "{}杯 - {} {} {}".format(number, temperature, sugar, coffee))]
        else:
            return []
