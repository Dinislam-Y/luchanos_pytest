from my_funcs.file_workers import read_from_file

test_data = ['one\n', 'two\n', 'three']

file_way = "tests/test_file_workers/testfile.txt"


def create_test_data():
    with open("testfile.txt", "a") as f_o:
        f_o.writelines(test_data)


def test_read_from_file():
    create_test_data()
    assert test_data == read_from_file(file_way)


def test_read_from_file2():
    create_test_data()
    assert test_data == read_from_file(file_way)
