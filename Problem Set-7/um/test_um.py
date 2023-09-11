from um import count
import pytest

def main():
    test_upper_lower_case()
    test_um_with_words()
    test_surrounded_by_space()
    
def test_um_with_words():
    assert count('yumi') == 0
  


def test_surrounded_by_space():
    assert count('Hello um world') == 1
    assert count('!?.,UM,.?!') == 1



def test_upper_lower_case():
    assert count('Um, thanks for the album.') == 1
    assert count('Um, thanks, um...') == 2


if __name__ == '__main__':
    main()
