import os


def read_readme():
    """Read the content of the README.md file."""
    readme_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'README.md')
    with open(readme_path, 'r') as file:
        return file.read()


def test_readme_content():
    """Test that the README.md contains the expected updated text."""
    readme_content = read_readme()
    
    # Verify that the README contains the updated text and not the old text
    assert "Codecov's features and functionalities" in readme_content
    assert "features and functionalities of Codecov" not in readme_content
