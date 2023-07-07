import pathlib
from os.path import join
from os import mkdir, makedirs, sep
from shutil import copyfile, rmtree

from empire_p._scandir import scan_directory, PredefinedCallbacks
from empire_p._types import Args

from jinja2 import Environment, FileSystemLoader


def generate_template(
    template_file: str,
    **kwargs
) -> str:
    jinja_env = Environment(
        loader=FileSystemLoader(str(pathlib.Path(template_file).parent)),
    )
    template_schema = jinja_env.get_template(template_file.split(f'{sep}')[-1])

    return template_schema.render(
            **kwargs
    )


def input_default(prompt: str, default: str) -> str:
    if not (in_ := input(f'{prompt} [{default}] ')):
        return default
    return in_


def input_many(prompt: str) -> list[str]:
    result: list[str] = []
    while in_ := input(f'{prompt} (enter nothing to exit) '):
        result.append(in_)

    return result


def init():
    root_path: str = input('Enter project root path: ')
    project_name: str = input('Enter project name (ex: empire-console): ')
    project_description: str = input('Enter project description: ')
    project_version: str = input_default('Enter version: ', '1.0')
    project_code_name: str = input('Enter project name in-code (ex: econsole): ')
    minimum_python_version: str = input_default('Enter minimum python version: ', '3.10')
    classifiers: list[str] = [
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.10",
        "Typing :: Typed"
    ] + input_many('Enter additional classifiers')
    requirements: list[str] = [
        "empire_commons@https://github.com/Tombmyst-Empire/empire-commons/archive/refs/heads/master.zip"
    ] + input_many('Enter additional requirements')

    files: list[str] = scan_directory(
        join(str(pathlib.Path(__file__).parent.parent.parent), 'template'),
        recursive=True,
        on_entry_found_callback=PredefinedCallbacks.files_only
    )
    root_path = join(root_path, project_name).replace('/', sep).replace('\\', sep)
    print(f'Making directory "{root_path}"')
    try:
        mkdir(root_path)
    except FileExistsError:
        if input(f'{root_path} already exists! Enter y to delete it and continue: ').lower() == 'y':
            rmtree(root_path)
            mkdir(root_path)
        else:
            print('Aborting')
            return

    src_path: str = f'{root_path}/src/{project_code_name}'
    print(f'Making source code directory "{src_path}"')
    makedirs(src_path, exist_ok=True)
    open(f'{src_path}{sep}__init__.py', 'w').close()
    open(f'{src_path}{sep}main.py', 'w').close()

    doc_path: str = f'{root_path}/docs'
    print(f'Making source doc directory "{doc_path}" and subdirs')
    makedirs(doc_path, exist_ok=True)
    makedirs(f'{doc_path}/_static', exist_ok=True)
    makedirs(f'{doc_path}/_template', exist_ok=True)
    makedirs(f'{doc_path}/doctrees', exist_ok=True)
    makedirs(f'{doc_path}/generated', exist_ok=True)
    makedirs(f'{doc_path}/html', exist_ok=True)

    for a_file in files:
        print(f'Proceeding with file: {a_file}')
        destination_file = f'{root_path}{sep}{a_file.split(f"template{sep}")[1]}'
        if a_file.endswith('.j2'):
            destination_file = destination_file.replace('.j2', '')

            contents: str = generate_template(
                a_file,
                project_title=project_name.upper().replace('-', ' -- '),
                project_name=project_name,
                project_description=project_description,
                project_code_name=project_code_name,
                project_version=project_version,
                minimum_python_version=minimum_python_version,
                classifiers=classifiers,
                requirements=requirements,
                py_xxx_version=project_version.replace('.', '')
            )

            with open(destination_file, 'w', encoding='utf8') as f:
                f.write(contents)
        else:
            copyfile(a_file, destination_file)



if __name__ == '__main__':
    s = input()
    print('S', s)