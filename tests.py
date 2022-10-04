from main import soma

def test_soma():
  assert soma([1, 2, 3]) == 6, "Should be 6"

if __name__ == "__main__":
  test_soma()
  print("Everything passed")
