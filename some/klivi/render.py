import os
import json
import tkinter

class Widget:
    def __init__(self, master, props, children):
        self.master = master
        self.props = props
        self.children = children


class Virtual_Model:  # aka virtual dom for gui
    def __init__(self):
        self.render = ""

    def component(self, master, components, props, children):
        return {
            master,
            components,
            props,
            children,
        }

    def create_components(self, vnode):
        if type(vnode) == 'str':
            return self.render.createTextNode(vnode)
        """
        el = self.render.createElement(vnode.tag)
        if vnode.props: 
            Object.entries(vnode.props).forEach(([name, value]) => 
            el[name] = value;

        
        if (vnode.children) 
            vnode.children.forEach(child => 
            el.appendChild(createElement(child));
            );
        
        return el;
        """


class Render:
    pass
