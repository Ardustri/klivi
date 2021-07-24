
import os
import json
import tkinter as tk
from tkinter.constants import W

widget_alias = {
    "div": tk.Widget,
    "frame": tk.Frame,
    "button": tk.Button,
    "label": tk.Label,
    "text": tk.Text,
    "input": tk.Entry,
    "canvas": tk.Canvas,
    "radio-button": tk.Radiobutton,
    "menu": tk.Menu,
    "menu-button": tk.Menubutton,
    "check-button": tk.Checkbutton,
    "list-box": tk.Listbox,
}
a = ...


class Widget:
    def __init__(self, master, props, children):
        self.master = master
        self.props = props
        self.children = children


class Virtual_Model:  # aka virtual dom for gui
    def __init__(self):
        self

    def m(self, master, components, props, children):
        return {
            master,
            components,
            props,
            children,
        }

    # def create_components(self, vnode):
    #    if type(vnode) == 'str':
    #        return self.render.createTextNode(vnode)
    #    """
    #    el = self.render.createElement(vnode.tag)
    #    if vnode.props:
    #        Object.entries(vnode.props).forEach(([name, value]) =>
    #        el[name] = value;
#
    #
    #    if (vnode.children)
    #        vnode.children.forEach(child =>
    #        el.appendChild(createElement(child));
    #        );
    #
    #    return el;
    #    """

    def create():
        ...

    def render(self, json_tree: dict):
        app = dict(json_tree)
        #w = tk.Tk("app")
        for widget in json_tree:
            print(json_tree[widget])
            exec("")


a = '''
{
    "window": {
    }
}
'''
Virtual_Model().render(dict(json.loads(a)))


class Render:
    pass
