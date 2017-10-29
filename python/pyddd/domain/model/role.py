# coding=utf-8


class Role:

    @staticmethod
    def convert(root, role):
        for name in dir(root):
            obj = getattr(root, name)
            if obj.__class__.__name__ == role:
                return obj

    @staticmethod
    def add_role(root, role):
        for attr in dir(role):
            if hasattr(root, attr):
                continue
            setattr(root, attr, getattr(role, attr))

