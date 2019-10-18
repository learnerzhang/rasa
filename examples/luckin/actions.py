#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-16 11:03
# @Author  : zhangzhen
# @Site    :
# @File    : actions.py.py
# @Software: PyCharm
from typing import List

from rasa_sdk import Action
from rasa_sdk.events import SlotSet


class ActionReportWeather(Action):
    RANDOMIZE = True

    def name(self):
        # type: () -> Text
        return "action_order_item"

    def run(self, dispatcher, tracker, domain):
        # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
        coffee = tracker.get_slot('coffee')
        temperature = tracker.get_slot('temperature')
        temperature = temperature if temperature else "None"
        coffee = coffee if coffee else "None"
        print(temperature + " " + coffee)
        return [SlotSet("matches", "{} {}".format(temperature, coffee))]
