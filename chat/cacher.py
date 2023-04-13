from django.core.cache import cache


def clear():
    cache.clear()


def get(key):
    return cache.get(key)


def set(key, value):
    cache.set(key, value)


def get_or_set(key, value):
    return cache.get_or_set(key, value)
