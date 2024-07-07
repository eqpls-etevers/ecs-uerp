# -*- coding: utf-8 -*-
'''
Equal Plus
@author: Hye-Churn Jang
'''

#===============================================================================
# Import
#===============================================================================
from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from stringcase import snakecase
from common import getConfig, Logger, MultiTask, AsyncRest

from .controls import Control

#===============================================================================
# SingleTone
#===============================================================================
config = getConfig('../module.ini')
Logger.register(config)
rootPath = f"/{snakecase(config['default']['title'])}"
api = FastAPI(
    title=config['default']['title'],
    separate_input_output_schemas=False,
    docs_url=f'{rootPath}/docs',
    openapi_url=f'{rootPath}/openapi.json'
)
ctrl = Control(api, config)

#===============================================================================
# API Interfaces
#===============================================================================
