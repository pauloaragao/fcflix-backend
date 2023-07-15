from datetime import datetime 
from typing import Optional
from dataclasses import dataclass, field
import unittest

@dataclass() #init, repr, eq
class Category:
    name: str
    description: Optional[str] = None
    is_active: Optional[bool] = True
    created_at: Optional[datetime] = field(default_factory=lambda: datetime.now())


