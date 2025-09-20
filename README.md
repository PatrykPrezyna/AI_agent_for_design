# AI Agent for Design

A Python application for AI-powered design assistance.

## Prerequisites

Before setting up the environment, make sure you have the following installed on your system:

- **Python 3.8 or higher** - Download from [python.org](https://www.python.org/downloads/)
- **Git** - Download from [git-scm.com](https://git-scm.com/downloads)

## Environment Setup

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd AI_agent_for_design
```

### 2. Create a Virtual Environment

It's recommended to use a virtual environment to isolate your project dependencies:

#### Using venv (recommended):
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

#### Using conda (alternative):
```bash
# Create conda environment
conda create -n ai_agent_design python=3.9
conda activate ai_agent_design
```

### 3. Install Dependencies

```bash
# Install required packages
pip install -r requirements.txt

# Or if you don't have a requirements.txt yet, install common packages:
pip install numpy pandas matplotlib seaborn requests flask
```

### 4. Environment Variables (if needed)

Create a `.env` file in the project root for environment-specific variables:

```bash
# Create .env file
touch .env
```

Add your environment variables to the `.env` file:
```
# Example environment variables
API_KEY=your_api_key_here
DEBUG=True
DATABASE_URL=your_database_url_here
```

### 5. Verify Installation

Test that everything is set up correctly:

```bash
# Check Python version
python --version

# Check installed packages
pip list

# Run a simple test (if you have a main.py file)
python main.py
```

## Project Structure

```
AI_agent_for_design/
├── README.md
├── requirements.txt
├── .env
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── modules/
├── tests/
├── docs/
└── venv/ (created after setup)
```

## Development

### Running the Application

```bash
# Make sure virtual environment is activated
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Run the main application
python src/main.py
```

### Adding Dependencies

When adding new packages to your project:

```bash
# Install new package
pip install package_name

# Update requirements.txt
pip freeze > requirements.txt
```

### Deactivating Virtual Environment

When you're done working:

```bash
deactivate
```

## Troubleshooting

### Common Issues

1. **Python not found**: Make sure Python is installed and added to your PATH
2. **Permission errors**: Try running commands with `sudo` on macOS/Linux or as Administrator on Windows
3. **Virtual environment not activating**: Make sure you're in the correct directory and using the right activation script

### Getting Help

- Check the [Python documentation](https://docs.python.org/3/)
- Review the [pip documentation](https://pip.pypa.io/en/stable/)
- Search for specific error messages online

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.


set OPENAI_API_KEY=your_api_key_here
echo %OPENAI_API_KEY% 
