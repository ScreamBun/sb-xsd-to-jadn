from xsd_to_jadn import main


def test_xsd_creation():
    
    try:
        main('Data', 'Out')
    except Exception as e:
        print(f"Error: {e}")
        assert False, f"main() raised an exception: {e}"
    
    pass