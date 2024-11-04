from abc import ABC, abstractmethod


class Interactor[Request, Response](ABC):
    @abstractmethod
    async def __call__(self, request: Request) -> Response:
        ...