from pathlib import Path

def list_files(base_path, indent=0):
    for path in sorted(base_path.iterdir()):
        if path.is_dir():
            print('  ' * indent + f'[DIR] {path.name}')
            list_files(path, indent + 1)
        else:
            print('  ' * indent + f'  - {path.name}')

if __name__ == "__main__":
    base = Path('.')
    list_files(base)
