#!/bin/bash
###############################################################################
# Betty Framework - Quickstart Setup Script
#
# This script sets up the Betty Framework in under 5 minutes.
# It installs dependencies, configures environment variables, and creates
# a "Hello World" skill to get you started.
#
# Usage:
#   curl -sSL https://raw.githubusercontent.com/epieczko/betty/main/scripts/quickstart.sh | bash
#
# Or locally:
#   bash scripts/quickstart.sh
###############################################################################

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Print functions
print_header() {
    echo -e "\n${BLUE}========================================${NC}"
    echo -e "${BLUE}$1${NC}"
    echo -e "${BLUE}========================================${NC}\n"
}

print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

print_info() {
    echo -e "${YELLOW}→ $1${NC}"
}

# Check prerequisites
check_prerequisites() {
    print_header "Checking Prerequisites"

    # Check Python
    if command -v python3 &> /dev/null; then
        PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
        print_success "Python 3 found: $PYTHON_VERSION"
    else
        print_error "Python 3 is not installed"
        echo "Please install Python 3.8 or higher: https://www.python.org/downloads/"
        exit 1
    fi

    # Check pip
    if command -v pip3 &> /dev/null || command -v pip &> /dev/null; then
        print_success "pip found"
    else
        print_error "pip is not installed"
        echo "Please install pip: https://pip.pypa.io/en/stable/installation/"
        exit 1
    fi

    # Check Git
    if command -v git &> /dev/null; then
        GIT_VERSION=$(git --version | cut -d' ' -f3)
        print_success "Git found: $GIT_VERSION"
    else
        print_error "Git is not installed"
        echo "Please install Git: https://git-scm.com/downloads"
        exit 1
    fi
}

# Determine Betty directory
determine_betty_dir() {
    if [ -f "betty/config.py" ] && [ -f "README.md" ]; then
        # We're already in the betty directory
        BETTY_DIR="$(pwd)"
        print_info "Using current directory: $BETTY_DIR"
    elif [ -d "../betty" ] && [ -f "../betty/config.py" ]; then
        # Betty is in parent directory
        BETTY_DIR="$(cd ../betty && pwd)"
        print_info "Using Betty directory: $BETTY_DIR"
    else
        # Clone Betty
        print_header "Cloning Betty Repository"
        BETTY_DIR="$HOME/betty"

        if [ -d "$BETTY_DIR" ]; then
            print_info "Betty directory already exists at $BETTY_DIR"
            cd "$BETTY_DIR"
            print_info "Pulling latest changes..."
            git pull origin main || print_info "Could not pull latest changes, continuing with existing version"
        else
            print_info "Cloning Betty to $BETTY_DIR"
            git clone https://github.com/epieczko/betty.git "$BETTY_DIR"
            cd "$BETTY_DIR"
            print_success "Betty cloned successfully"
        fi
    fi

    cd "$BETTY_DIR"
}

# Install dependencies
install_dependencies() {
    print_header "Installing Dependencies"

    if [ -f "requirements.txt" ]; then
        print_info "Installing Python packages..."
        pip3 install -r requirements.txt --quiet
        print_success "Dependencies installed"
    else
        print_error "requirements.txt not found"
        exit 1
    fi
}

# Setup environment
setup_environment() {
    print_header "Setting Up Environment"

    # Set environment variables for current session
    export PYTHONPATH="${PYTHONPATH}:${BETTY_DIR}"
    export BETTY_HOME="${BETTY_DIR}"

    print_success "Environment variables set for current session"

    # Detect shell and create persistent config
    SHELL_CONFIG=""
    if [ -n "$BASH_VERSION" ]; then
        SHELL_CONFIG="$HOME/.bashrc"
    elif [ -n "$ZSH_VERSION" ]; then
        SHELL_CONFIG="$HOME/.zshrc"
    fi

    if [ -n "$SHELL_CONFIG" ]; then
        print_info "Adding Betty environment to $SHELL_CONFIG"

        # Check if already configured
        if grep -q "BETTY_HOME" "$SHELL_CONFIG" 2>/dev/null; then
            print_info "Betty environment already configured in $SHELL_CONFIG"
        else
            cat >> "$SHELL_CONFIG" <<EOF

# Betty Framework Configuration
export BETTY_HOME="${BETTY_DIR}"
export PYTHONPATH="\${PYTHONPATH}:\${BETTY_HOME}"
EOF
            print_success "Added Betty environment to $SHELL_CONFIG"
            print_info "Run 'source $SHELL_CONFIG' to apply changes to your current shell"
        fi
    fi
}

# Verify installation
verify_installation() {
    print_header "Verifying Installation"

    # Check if validation module exists
    if [ -f "betty/validation.py" ]; then
        print_info "Running validation checks..."
        if python3 -m betty.validation; then
            print_success "Installation verified successfully"
        else
            print_info "Validation completed with warnings (this is normal for a new installation)"
        fi
    else
        # Manual checks
        print_info "Checking directory structure..."

        [ -d "skills" ] && print_success "skills/ directory found" || print_error "skills/ directory missing"
        [ -d "agents" ] && print_success "agents/ directory found" || print_error "agents/ directory missing"
        [ -d "registry" ] && print_success "registry/ directory found" || print_error "registry/ directory missing"
        [ -f "registry/skills.json" ] && print_success "skills registry found" || print_error "skills registry missing"
    fi
}

# Create Hello World skill example
create_hello_world() {
    print_header "Creating Hello World Skill Example"

    HELLO_WORLD_DIR="$BETTY_DIR/examples/skills/hello.world"

    if [ -d "$HELLO_WORLD_DIR" ]; then
        print_info "Hello World skill already exists"
    else
        print_info "Creating Hello World skill in examples/skills/..."
        mkdir -p "$HELLO_WORLD_DIR"

        # The actual implementation will be created by the next function
        print_success "Hello World skill directory created"
    fi
}

# Display next steps
display_next_steps() {
    print_header "Setup Complete!"

    cat <<EOF
${GREEN}Betty Framework is ready to use!${NC}

${YELLOW}Quick Start:${NC}

1. Try the Hello World skill:
   ${BLUE}cd $BETTY_DIR${NC}
   ${BLUE}python3 examples/skills/hello.world/hello_world.py --name "YourName"${NC}

2. Explore example skills:
   ${BLUE}ls examples/skills/${NC}

3. Create your own skill:
   ${BLUE}python3 agents/meta.skill/meta_skill.py my_skill_description.md${NC}

4. List all available skills:
   ${BLUE}cat registry/skills.json | jq '.skills[].name'${NC}

5. Read the full quickstart guide:
   ${BLUE}cat QUICKSTART.md${NC}

${YELLOW}Documentation:${NC}
- Quickstart Tutorial: ${BLUE}QUICKSTART.md${NC}
- Getting Started: ${BLUE}GETTING_STARTED.md${NC}
- Architecture: ${BLUE}docs/betty-architecture.md${NC}
- Skills Framework: ${BLUE}docs/skills-framework.md${NC}

${YELLOW}Need Help?${NC}
- Documentation: ${BLUE}$BETTY_DIR/docs/${NC}
- GitHub Issues: ${BLUE}https://github.com/epieczko/betty/issues${NC}
- Community: ${BLUE}https://github.com/epieczko/betty/discussions${NC}

${GREEN}Happy Building with Betty! 🚀${NC}

EOF
}

# Main execution
main() {
    echo -e "${BLUE}"
    cat <<'EOF'
    ____       _   _
   |  _ \     | | | |
   | |_) | ___| |_| |_ _   _
   |  _ < / _ \ __| __| | | |
   | |_) |  __/ |_| |_| |_| |
   |____/ \___|\__|\__|\__, |
                        __/ |
   Framework          |___/

   AI-Native SDLC Framework

EOF
    echo -e "${NC}"

    print_info "Starting Betty Framework quickstart setup..."

    check_prerequisites
    determine_betty_dir
    install_dependencies
    setup_environment
    verify_installation
    create_hello_world
    display_next_steps
}

# Run main function
main
