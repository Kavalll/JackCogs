from typing import Any, Callable, ContextManager, Optional, TypeVar

from .cache import Cache

_KT = TypeVar("_KT")
_VT = TypeVar("_VT")
_T = TypeVar("_T", bound=Callable[..., Any])
_T_co = TypeVar("_T_co", covariant=True)

def cached(cache: Cache[_KT, _VT], key: _KT = ..., lock: Optional[ContextManager[_T_co]] = ...) -> Callable[[_T], _T]:
    """Decorator to wrap a function with a memoizing callable that saves
    results in a cache.

    """
    ...

def cachedmethod(cache: Cache[_KT, _VT], key: _KT = ..., lock: Optional[ContextManager[_T_co]] = ...) -> Callable[[_T], _T]:
    """Decorator to wrap a class or instance method with a memoizing
    callable that saves results in a cache.

    """
    ...
