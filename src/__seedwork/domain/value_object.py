from dataclasses import dataclass, field
from __seedwork.domain.execption import InvalidUuidException
import uuid

@dataclass()
class UniqueEntityId:

    id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    def __validate(self):
        try:
            uuid.UUID(self.id)
        except ValueError as ex:
            raise InvalidUuidException() from ex


UniqueEntityId()