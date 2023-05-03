from my_funcs.file_workers import read_from_file


def test_read_from_file():
    test_data = ['one\n', 'two\n', 'three']
    assert test_data == read_from_file("tests/testfile.txt")
