# -*- coding: utf-8 -*-

from ws2812 import WS2812


led = WS2812(spi_bus=2, led_count=1)



led.show([(0,255,0)])
