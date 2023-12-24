# config.py

# Import necessary packages
import os

# Define the base directory for the project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define the directory for the templates
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

# Define the default project structure
DEFAULT_PROJECT_STRUCTURE = {
    'src': {
        'main': {
            'python': {},
            'resources': {}
        },
        'test': {
            'python': {},
            'resources': {}
        }
    },
    'docs': {},
    'libs': {},
    'bin': {}
}

# Define the default template to be used for project structure generation
DEFAULT_TEMPLATE = 'default_template'

# Define the version control system to be used
VCS = 'git'

# Define the AI-driven optimization parameters
AI_OPTIMIZATION_PARAMS = {
    'algorithm': 'genetic',
    'population_size': 100,
    'mutation_rate': 0.01,
    'crossover_rate': 0.9
}

# Define the documentation automation parameters
DOC_AUTOMATION_PARAMS = {
    'format': 'markdown',
    'output_dir': os.path.join(BASE_DIR, 'docs')
}
