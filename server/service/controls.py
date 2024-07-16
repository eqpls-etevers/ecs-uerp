# -*- coding: utf-8 -*-
'''
Equal Plus
@author: Hye-Churn Jang
'''

#===============================================================================
# Import
#===============================================================================
from common import UerpControl
from driver import RedisModel, ElasticSearch, PostgreSql
from integration.auth_kc_redis import AuthDriver

from schema.secret.certification import Authority, Server
from schema.secret.access import OpenSsh


#===============================================================================
# Implement
#===============================================================================
class Control(UerpControl):

    def __init__(self, api, config):
        UerpControl.__init__(
            self,
            api=api,
            config=config,
            authDriver=AuthDriver,
            cacheDriver=RedisModel,
            searchDriver=ElasticSearch,
            databaseDriver=PostgreSql
        )

    async def startup(self):
        await self.registerModel(Authority)
        await self.registerModel(Server)
        await self.registerModel(OpenSsh)

    async def shutdown(self): pass
