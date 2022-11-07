class BaseError(Exception):
    massage = 'Чтото пошло не так'


class NotEnoughtSpaceError(BaseError):
    massage = 'Недостаточно места'


class NotEnoughtProductError(BaseError):
    massage = 'Недостаточно товара'


class TooManyDiffProductsError(BaseError):
    massage = 'Слишком много разных товаров'


class WrongRequestsError(BaseError):
    massage = 'Неправильный запрос'


class UnknownStorageError(BaseError):
    massage = 'Неизвестный склад'


class UnknownProductError(BaseError):
    massage = 'Неизвестный товар'
