#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-22 10:21
# @Author  : zhangzhen
# @Site    : 
# @File    : extractor.py
# @Software: PyCharm
import logging
from typing import Any

from rasa.nlu.extractors import EntityExtractor
from rasa.nlu.training_data import Message
import pprint
import json
import re

logger = logging.getLogger(__name__)


class LuckinEntityExtractor(EntityExtractor):
    provides = ["entities"]

    def __init__(self, component_config=None):
        super(LuckinEntityExtractor, self).__init__(component_config)
        self.rule = {
            "tea": ["大红袍牛乳茶", "大红袍啵啵茶", "黑糖啵啵牛乳", "大红袍脏脏茶", "抹茶牛乳", "招牌啵啵", "黑糖啵啵", "经典奶茶", "红豆奶茶", "椰果奶茶", "仙草奶茶",
                    "燕麦奶茶", "经典双拼", "红茶玛奇朵", "茉莉玛奇朵", "美人玛奇朵", "大红袍玛奇朵", "柠檬美人脆啵啵", "柠檬绿茶脆啵啵", "百香柠檬脆啵啵", "金桔柠檬脆啵啵",
                    "凤梨百香脆啵啵", "芒芒百香脆啵啵", "凤梨百香三重奏", "芒芒百香三重奏"],
            "coffee": ["陨石拿铁", "拿铁", "香草拿铁", "焦糖拿铁", "标准美式", "加浓美式", "焦糖标准美式", "焦糖加浓美式", "银河气泡美式", "金橘气泡美式", "黑金气泡美式",
                       "奥瑞白", "卡布奇洛", "焦糖玛奇朵", "摩卡"],
            "sugar": ["无糖", "半分糖|少糖", "全糖"],
            "temperature": ["冰", "热", "少冰", "不加冰"]
        }
        self.patterns = {
            dim: [re.compile(v, re.I) for v in vs] for dim, vs in self.rule.items()
        }

    def process(self, message: Message, **kwargs: Any):
        extracted = []
        for dim, patterns in self.patterns.items():
            for pattern in patterns:
                tokens = pattern.finditer(message.text)
                for token in list(tokens):
                    # print(token.start(), token.end(), token.group())
                    extracted.append(self.token2json(dim, token))
        message.set("entities", message.get("entities", []) + extracted, add_to_output=True)

    def token2json(self, dim, token):
        return {
            'body': token.group(),
            'entity': dim,
            'start': token.start(),
            'end': token.end(),
            'value': token.group()
        }


if __name__ == '__main__':
    luckin = LuckinEntityExtractor()
    msg = Message(text="加浓美式A31322318，加浓美式居留许可号码：08360609，有效期至：20180705。。")
    luckin.process(msg)
    pprint.pprint(msg.data)
