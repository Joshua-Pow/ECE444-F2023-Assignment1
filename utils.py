from typing import Tuple


class utils():
    def reversed(num: int) -> int:
        """
        reverses a number

        Args:
            num (int): the number to reverse

        Returns:
            int: the reversed number
        """
        if isinstance(num, int):
            return int(str(num)[::-1])
        else:
            raise TypeError("num must be an int")

    def formater(s: int) -> Tuple[int, int]:
        """
        converts an int to base 2 and base 8

        Args:
            s (int): the number to convert

        Returns:
            tuple[int, int]: the number in base 2 and base 8
        """
        if isinstance(s, int):
            return [bin(s), oct(s)]
        else:
            raise TypeError("s must be an int")
