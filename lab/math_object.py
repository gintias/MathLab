from dataclasses import dataclass, field
from typing import Any, Optional, Generic, TypeVar
from abc import ABC, abstractmethod

from .metadata import InitialMetadata

T = TypeVar("T", bound="MathObject")

@dataclass
class ObjectDraft(Generic[T]):
    """
    A newly instantiated mathematical payload 
    plus its initial metadata

    """
    obj: T
    metadata: InitialMetadata


# MathObject is never directly instantiated its always subclassed
# The @abstractmethod wrapper indicates which methods any concrete subclass must provide
# its own implementation of

class MathObject(ABC):
    """
    Abstract instantiation tempalte for 
    mathematical payloads
    """
    
    object_kind: str = "MathObject"
    
    @abstractmethod
    def validate(self) -> None:
        """
        Check that the payload is internally well-formed.

        """
        raise NotImplementedError
    
    @abstractmethod
    def canonical_key(self) -> tuple:
        """
        Return a hashable key for object-level equality.

        """
        raise NotImplementedError

    def canonial_key(self) -> tuple:
        """
        Compatibility alias for the earlier misspelling.
        New MathObject subclasses should implement canonical_key().
        """
        return self.canonical_key()
    
    @abstractmethod
    def display_payload(self) -> str:
        """
        Human-facing mathematical display of the payload.

        """
        raise NotImplementedError
    
    def default_metadata(self) -> InitialMetadata:
        """
        Fallback metadata if object was instantiated directly rather
        than through a rich factory. Override subclasses if needed.

        """
        return InitialMetadata()
    
