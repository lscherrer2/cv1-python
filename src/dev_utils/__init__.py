from typing import Optional
def todo (message: Optional[str] = None):
    message = message if message is not None else "Attempted to run not implimented code"
    raise NotImplementedError(message)
