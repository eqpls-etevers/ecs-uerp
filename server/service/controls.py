# -*- coding: utf-8 -*-
'''
Equal Plus
@author: Hye-Churn Jang
'''

#===============================================================================
# Import
#===============================================================================
from common import UerpControl
from driver import Redis, ElasticSearch, PostgreSql

from schema.sample.model import Blog, Message


#===============================================================================
# Implement
#===============================================================================
class Control(UerpControl):

    def __init__(self, api, config):
        UerpControl.__init__(
            self,
            api,
            config,
            cacheDriver=Redis,
            searchDriver=ElasticSearch,
            databaseDriver=PostgreSql
        )

    async def startup(self):
        await self.registerModel(Blog)
        await self.registerModel(Message)

    async def shutdown(self): pass
