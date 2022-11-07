"""
Demo camera platform that has a fake camera.
For more details about this platform, please refer to the documentation
https://home-assistant.io/components/demo/
"""
import os
import time
import datetime
#from datetime import timedelta
import requests
import logging

import voluptuous as vol

from homeassistant.const import CONF_NAME
import homeassistant.util.dt as dt_util
from homeassistant.components.camera import Camera,PLATFORM_SCHEMA
import homeassistant.helpers.config_validation as cv

_LOGGER = logging.getLogger(__name__)



CONF_ID = 'id'
CONF_KEY = 'key'
CONF_SEC = 'sec'
CONF_NAME = 'name'
CONF_MAOYAN = 'ismaoyan'
PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_ID): cv.string,
    vol.Required(CONF_KEY): cv.string,
    vol.Required(CONF_SEC): cv.string,
    vol.Required(CONF_NAME): cv.string,
    vol.Required(CONF_MAOYAN): cv.string,
})


def setup_platform(hass, config, add_devices, discovery_info=None):
    """Set up the Demo camera platform."""
    add_devices([
        EzvizCamera(hass, config, CONF_NAME)
    ])


class EzvizCamera(Camera):
    """The representation of a Demo camera."""

    def __init__(self, hass, config, name):
        """Initialize ezviz camera component."""
        super().__init__()
        self._parent = hass
        self._name = config.get(CONF_NAME)
        self._motion_status = False
        self._isMaoyan = 'notmaoyan'
        _LOGGER.error("initconfig")
        self._isMaoyan = config.get(CONF_MAOYAN)
        _LOGGER.error('%s' % self._isMaoyan)
        self.appKey = config.get(CONF_KEY)
        self.appSecret = config.get(CONF_SEC)
        self.accessToken = ""
        self.deviceSerial = config.get(CONF_ID)
        self.expireTime = 0

        self._is_streaming = None
        self._is_video_history_enabled = False

        # Default to non-NestAware subscribed, but will be fixed during update
        self._time_between_snapshots = datetime.timedelta(seconds=30)
        self._last_image = None
        self._next_snapshot_at = None
        self._attr_unique_id = self._name + self.deviceSerial

#    def motion_detection_enabled(self):
#        r = requests.post('https://open.ys7.com/api/lapp/device/info', data={'accessToken':self.accessToken,'deviceSerial':self.deviceSerial})
#        result = r.json()
#        return result.get('defence') == 1

#    def enable_motion_detection(self):
#        r = requests.post('https://open.ys7.com/api/lapp/device/defence/set', data={'accessToken':self.accessToken,'deviceSerial':self.deviceSerial,'isDefence': 1})
#        self.schedule_update_ha_state()

#    def disable_motion_detection(self):
#        r = requests.post('https://open.ys7.com/api/lapp/device/defence/set', data={'accessToken':self.accessToken,'deviceSerial':self.deviceSerial,'isDefence': 0})
#        self.schedule_update_ha_state()

    def get_token(key,secret):
        r = requests.post('https://open.ys7.com/api/lapp/token/get', data={'appKey':key,'appSecret':secret})
        token_result = r.json()
        if (token_result['code']=='200'):
            self.accessToken = token_result['data']['accessToken']
            self.expireTime = token_result['data']['expireTime']
            return True
        else:
            return False
    def check_token_is_expired():
        now = int(round(time.time() * 1000))
        if (now > (self.expireTime-1000)):
            return True
        else:
            return False

    def get_device_capture(self):
        r = requests.post('https://open.ys7.com/api/lapp/device/capture', data={'accessToken':self.accessToken,'deviceSerial':self.deviceSerial,'channelNo':1,'quality':1})
        result = r.json()
        if (result['code']=='200'):
            return result['data']['picUrl']
        else:
            return 'error'

    def get_device_message(self):
        r = requests.post('https://open.ys7.com/api/lapp/alarm/device/list', data={'accessToken':self.accessToken,'deviceSerial':self.deviceSerial})
        result = r.json()
        if (result['code']=='200'):
            if len(result['data']) > 0:
                #_LOGGER.error(result)
                alarmType = result['data'][0]['alarmType']
                alarmTime = result['data'][0]['alarmTime']
                alarmPicUrl = result['data'][0]['alarmPicUrl']
                strtime = datetime.datetime.fromtimestamp(alarmTime/1000)
                return alarmPicUrl
            else:
                return 'error'
        else:
            return 'error'


    def _ready_for_snapshot(self, now):
        return (self._next_snapshot_at is None or
                now > self._next_snapshot_at)

    def camera_image(
              self, width: int , height: int
    ):
        """Return a faked still image response."""
        #_LOGGER.error("camera_image")
        now = dt_util.utcnow()
        if self._ready_for_snapshot(now):
            #_LOGGER.error("self._ready_for_snapshot")

            nowss = int(round(time.time() * 1000))

            if (nowss > (self.expireTime-1000)):
                #_LOGGER.error("nowss > (self.expireTime-1000)")
                r = requests.post('https://open.ys7.com/api/lapp/token/get', data={'appKey':self.appKey,'appSecret':self.appSecret})
                token_result = r.json()
                if (token_result['code']=='200'):
                    self.accessToken = token_result['data']['accessToken']
                    self.expireTime = token_result['data']['expireTime']
                    #_LOGGER.error("get token success")
                else:
                    _LOGGER.error("get token error")


            #r = requests.post('https://open.ys7.com/api/lapp/device/capture', data={'accessToken':self.accessToken,'deviceSerial':self.deviceSerial,'channelNo':1,'quality':1})
            #result = r.json()
            #if (result['code']=='200'):
            #    image_path = result['data']['picUrl']
            #else:
            #    _LOGGER.info("get image error")
            #    image_path = 'null'
            #    return None
            _LOGGER.error(self._isMaoyan)
            _LOGGER.error('%s' % self._isMaoyan)
            if self._isMaoyan == 'maoyan' :
                _LOGGER.error("is MaoYan")
                _LOGGER.error(self.deviceSerial)
                image_path = self.get_device_message()
            else:
                _LOGGER.error("not MaoYan")
                _LOGGER.error(self.deviceSerial)
                image_path = self.get_device_capture()
            #_LOGGER.error("Get camera image: %s" % image_path)
            #_LOGGER.error("Config: %s" % self._isMaoyan)
            if image_path == 'error':
                return None

            try:
                response = requests.get(image_path)
            except requests.exceptions.RequestException as error:
                _LOGGER.error("Error getting camera image: %s", error)
                return None

            self._next_snapshot_at = now + self._time_between_snapshots
            self._last_image = response.content

        return self._last_image

    @property
    def name(self):
        """Return the name of this camera."""
        return self._name

    @property
    def should_poll(self):
        """Camera should poll periodically."""
        return True
