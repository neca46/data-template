from data_template.main import main

def test_main_print_greetings(capsys):
    main()

    captured = capsys.readouterr()
    assert captured.out == "Hello from data-template!\n"