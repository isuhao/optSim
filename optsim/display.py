# -*- coding:utf-8 -*-
'''
Created on Jul 26, 2014

@description This is an optical simulation program written for my lady
@author: andy
'''

import pygame
from pygame.locals import QUIT, KEYDOWN, K_SPACE, K_ESCAPE

class Canvas(object):
    '''
    classdocs
    '''

    def __init__(self, w=640, h=480, clr=True):
        '''
        Constructor
        '''
        pygame.init()
        self.width = int(w)
        self.height = int(h)
        self.clear = clr
        self.screen = pygame.display.set_mode((self.width, self.height), 0, 32)
        pygame.display.set_caption("optsim")
        
        self.interface_color = (100, 100, 150)
        
    def __draw_axis__(self):
        pass
    
    def draw(self, simulator):
        if self.clear:
            self.screen.fill((0, 0, 0))

        lights = simulator.getLights()
        for light in lights:
            self.__drawLight(light)
        
        interfaces = simulator.getInterfaces()
        for inter in interfaces:
            self.__drawInterface(inter)
            
        pygame.display.update()
        
        # 返回键盘、鼠标事件
        for event in pygame.event.get():
            if (event.type == QUIT):
                return 'quit'
            
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return 'esc'
                elif event.key == K_SPACE:
                    return 'space'
                else:
                    return None
        
    def __drawLight(self, light):
        if light.hitpoint is not None:
            pygame.draw.line(self.screen, self.__ColorForLightIntensity(light.intensity), self.__traslate(light.origin.toTuple()), self.__traslate(light.hitpoint.toTuple()), 1)
        else:
            line = light.toLine()
            p2_x = (line.point2.x - line.point1.x) * 100 + line.point1.x  # 直线原长是1，延长100倍
            p2_y = (line.point2.y - line.point1.y) * 100 + line.point1.y
            pygame.draw.line(self.screen, self.__ColorForLightIntensity(light.intensity), self.__traslate(line.point1.toTuple()), self.__traslate((p2_x, p2_y)), 1)
            
    def __drawInterface(self, inter):
        pygame.draw.line(self.screen, self.interface_color, self.__traslate(inter.start.toTuple()), self.__traslate(inter.end.toTuple()), 2)
        
        
    def __traslate(self, real_pos):
        return (self.width / 2.0 + real_pos[0], self.height / 2.0 - real_pos[1])
    
    def  __ColorForLightIntensity(self, inten):
        '''inten (0, 1] => (0, 255]'''
        R = G = int(inten * 255)
        B = int(inten * 50)
        return (R, G, B)
        
