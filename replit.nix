{ pkgs }: {
  deps = [
    pkgs.pip install -r requirements.txt
    pkgs.pytest test_main.py::test_one
  ];
}