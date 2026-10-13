"""TP 4 - Atelier décorateurs."""
import time
from functools import wraps


def chronometrer(_fonction=None, *, unite="s"):
    def decorateur(fonction):
        @wraps(fonction)
        def enveloppe(*args, **kwargs):
            debut = time.perf_counter(); resultat = fonction(*args, **kwargs)
            duree = time.perf_counter() - debut
            valeur = duree * 1000 if unite == "ms" else duree
            print(f"{fonction.__name__} a pris {valeur:.2f} {unite}")
            return resultat
        return enveloppe
    return decorateur if _fonction is None else decorateur(_fonction)


def majuscules(fonction):
    @wraps(fonction)
    def enveloppe(*args, **kwargs): return fonction(*args, **kwargs).upper()
    return enveloppe


def compter_appels(fonction):
    @wraps(fonction)
    def enveloppe(*args, **kwargs):
        enveloppe.appels += 1
        return fonction(*args, **kwargs)
    enveloppe.appels = 0
    return enveloppe


def verifier_positifs(fonction):
    @wraps(fonction)
    def enveloppe(*args, **kwargs):
        if any(isinstance(x, (int, float)) and x < 0 for x in args):
            raise ValueError("Les arguments doivent être positifs")
        return fonction(*args, **kwargs)
    return enveloppe


def memoriser(fonction):
    cache = {}
    @wraps(fonction)
    def enveloppe(*args, **kwargs):
        cle = (args, tuple(sorted(kwargs.items())))
        if cle not in cache: cache[cle] = fonction(*args, **kwargs)
        return cache[cle]
    return enveloppe


@memoriser
def fibonacci(n):
    return n if n < 2 else fibonacci(n - 1) + fibonacci(n - 2)


@chronometrer
def lente(): time.sleep(1)
lente()
print(fibonacci(30))
