import edpy.errors as errors
import edpy.buffer

def test_file_not_saved_error_init_incorrect_buffer():
    """Tests the creation of a FileNotSavedError object with incorrect args."""
    buff = "" # pass in a faulty buffer
    try:
        error = errors.FileNotSavedError(buff)
        assert False # Fail if it doesn't throw an exception
    except Exception:
        assert True # Pass if it does throw an exception


def test_file_not_saved_error_init_correct_buffer():
    """Tests the creation of a FileNotSavedError object with correct args."""
    buff = edpy.buffer.EditBuffer("dummy.file")
    try:
        error = errors.FileNotSavedError(buff)
    except:
        assert False # Fail the test

    assert error.buffer == buff # Make sure the buff was assigned correctly

def test_file_not_saved_error_run():
    """Tests if the exception throw prints the correct output."""
        buff = edpy.buffer.EditBuffer("dummy.file")
        error = errors.FileNotSavedError(buff)
        errString = "Buffer \'dummy.file\' not saved."

        try:
            raise error
        except errors.FileNotSavedError as e:
            assert str(e) == errString
