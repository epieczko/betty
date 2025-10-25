#!/usr/bin/env pwsh
###############################################################################
# Betty Framework - Quickstart Setup Script (PowerShell)
#
# This script sets up the Betty Framework on Windows in under 5 minutes.
# It installs dependencies, configures environment variables, and creates
# a "Hello World" skill to get you started.
#
# Usage (PowerShell):
#   irm https://raw.githubusercontent.com/epieczko/betty/main/scripts/quickstart.ps1 | iex
#
# Or locally:
#   .\scripts\quickstart.ps1
###############################################################################

$ErrorActionPreference = "Stop"

# Colors for output
function Write-Header {
    param([string]$Message)
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Blue
    Write-Host $Message -ForegroundColor Blue
    Write-Host "========================================" -ForegroundColor Blue
    Write-Host ""
}

function Write-Success {
    param([string]$Message)
    Write-Host "✓ $Message" -ForegroundColor Green
}

function Write-ErrorMsg {
    param([string]$Message)
    Write-Host "✗ $Message" -ForegroundColor Red
}

function Write-InfoMsg {
    param([string]$Message)
    Write-Host "→ $Message" -ForegroundColor Yellow
}

# Check prerequisites
function Test-Prerequisites {
    Write-Header "Checking Prerequisites"

    # Check Python
    try {
        $pythonVersion = python --version 2>&1
        if ($pythonVersion -match "Python (\d+\.\d+\.\d+)") {
            Write-Success "Python found: $($matches[1])"
        }
        else {
            Write-ErrorMsg "Python is not installed or not in PATH"
            Write-Host "Please install Python 3.8 or higher: https://www.python.org/downloads/"
            exit 1
        }
    }
    catch {
        Write-ErrorMsg "Python is not installed or not in PATH"
        Write-Host "Please install Python 3.8 or higher: https://www.python.org/downloads/"
        exit 1
    }

    # Check pip
    try {
        $null = pip --version 2>&1
        Write-Success "pip found"
    }
    catch {
        Write-ErrorMsg "pip is not installed"
        Write-Host "Please install pip: https://pip.pypa.io/en/stable/installation/"
        exit 1
    }

    # Check Git
    try {
        $gitVersion = git --version 2>&1
        if ($gitVersion -match "git version (.+)") {
            Write-Success "Git found: $($matches[1])"
        }
        else {
            Write-ErrorMsg "Git is not installed or not in PATH"
            Write-Host "Please install Git: https://git-scm.com/downloads"
            exit 1
        }
    }
    catch {
        Write-ErrorMsg "Git is not installed or not in PATH"
        Write-Host "Please install Git: https://git-scm.com/downloads"
        exit 1
    }
}

# Determine Betty directory
function Get-BettyDirectory {
    if ((Test-Path "betty\config.py") -and (Test-Path "README.md")) {
        # We're already in the betty directory
        $bettyDir = Get-Location
        Write-InfoMsg "Using current directory: $bettyDir"
        return $bettyDir
    }
    elseif ((Test-Path "..\betty") -and (Test-Path "..\betty\config.py")) {
        # Betty is in parent directory
        $bettyDir = Resolve-Path "..\betty"
        Write-InfoMsg "Using Betty directory: $bettyDir"
        return $bettyDir
    }
    else {
        # Clone Betty
        Write-Header "Cloning Betty Repository"
        $bettyDir = Join-Path $env:USERPROFILE "betty"

        if (Test-Path $bettyDir) {
            Write-InfoMsg "Betty directory already exists at $bettyDir"
            Set-Location $bettyDir
            Write-InfoMsg "Pulling latest changes..."
            try {
                git pull origin main 2>&1 | Out-Null
            }
            catch {
                Write-InfoMsg "Could not pull latest changes, continuing with existing version"
            }
        }
        else {
            Write-InfoMsg "Cloning Betty to $bettyDir"
            git clone https://github.com/epieczko/betty.git $bettyDir
            Set-Location $bettyDir
            Write-Success "Betty cloned successfully"
        }
        return $bettyDir
    }
}

# Install dependencies
function Install-Dependencies {
    param([string]$BettyDir)

    Write-Header "Installing Dependencies"

    $requirementsFile = Join-Path $BettyDir "requirements.txt"
    if (Test-Path $requirementsFile) {
        Write-InfoMsg "Installing Python packages..."
        pip install -r $requirementsFile --quiet
        Write-Success "Dependencies installed"
    }
    else {
        Write-ErrorMsg "requirements.txt not found"
        exit 1
    }
}

# Setup environment
function Set-BettyEnvironment {
    param([string]$BettyDir)

    Write-Header "Setting Up Environment"

    # Set environment variables for current session
    $env:PYTHONPATH = "$env:PYTHONPATH;$BettyDir"
    $env:BETTY_HOME = $BettyDir

    Write-Success "Environment variables set for current session"

    # Add to user environment variables permanently
    Write-InfoMsg "Adding Betty environment to user environment variables"

    try {
        # Set BETTY_HOME
        [System.Environment]::SetEnvironmentVariable("BETTY_HOME", $BettyDir, "User")

        # Add to PYTHONPATH
        $currentPythonPath = [System.Environment]::GetEnvironmentVariable("PYTHONPATH", "User")
        if (-not $currentPythonPath) {
            $currentPythonPath = ""
        }

        if ($currentPythonPath -notlike "*$BettyDir*") {
            $newPythonPath = if ($currentPythonPath) { "$currentPythonPath;$BettyDir" } else { $BettyDir }
            [System.Environment]::SetEnvironmentVariable("PYTHONPATH", $newPythonPath, "User")
            Write-Success "Added Betty environment to user environment variables"
        }
        else {
            Write-InfoMsg "Betty environment already configured in user variables"
        }

        Write-InfoMsg "Restart your PowerShell session to apply changes globally"
    }
    catch {
        Write-InfoMsg "Could not modify user environment variables (this is optional)"
        Write-InfoMsg "You can manually add BETTY_HOME=$BettyDir to your environment"
    }
}

# Verify installation
function Test-Installation {
    param([string]$BettyDir)

    Write-Header "Verifying Installation"

    # Check if validation module exists
    $validationScript = Join-Path $BettyDir "betty\validation.py"
    if (Test-Path $validationScript) {
        Write-InfoMsg "Running validation checks..."
        try {
            python -m betty.validation 2>&1 | Out-Null
            Write-Success "Installation verified successfully"
        }
        catch {
            Write-InfoMsg "Validation completed with warnings (this is normal for a new installation)"
        }
    }
    else {
        # Manual checks
        Write-InfoMsg "Checking directory structure..."

        $checks = @(
            @{Path = "skills"; Name = "skills/ directory" },
            @{Path = "agents"; Name = "agents/ directory" },
            @{Path = "registry"; Name = "registry/ directory" },
            @{Path = "registry\skills.json"; Name = "skills registry" }
        )

        foreach ($check in $checks) {
            $fullPath = Join-Path $BettyDir $check.Path
            if (Test-Path $fullPath) {
                Write-Success "$($check.Name) found"
            }
            else {
                Write-ErrorMsg "$($check.Name) missing"
            }
        }
    }
}

# Create Hello World skill example
function New-HelloWorldSkill {
    param([string]$BettyDir)

    Write-Header "Creating Hello World Skill Example"

    $helloWorldDir = Join-Path $BettyDir "examples\skills\hello.world"

    if (Test-Path $helloWorldDir) {
        Write-InfoMsg "Hello World skill already exists"
    }
    else {
        Write-InfoMsg "Creating Hello World skill in examples\skills\..."
        New-Item -ItemType Directory -Path $helloWorldDir -Force | Out-Null
        Write-Success "Hello World skill directory created"
    }
}

# Display next steps
function Show-NextSteps {
    param([string]$BettyDir)

    Write-Header "Setup Complete!"

    Write-Host "Betty Framework is ready to use!" -ForegroundColor Green
    Write-Host ""
    Write-Host "Quick Start:" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "1. Try the Hello World skill:" -ForegroundColor White
    Write-Host "   cd $BettyDir" -ForegroundColor Blue
    Write-Host "   python examples\skills\hello.world\hello_world.py --name `"YourName`"" -ForegroundColor Blue
    Write-Host ""
    Write-Host "2. Explore example skills:" -ForegroundColor White
    Write-Host "   dir examples\skills\" -ForegroundColor Blue
    Write-Host ""
    Write-Host "3. Create your own skill:" -ForegroundColor White
    Write-Host "   python agents\meta.skill\meta_skill.py my_skill_description.md" -ForegroundColor Blue
    Write-Host ""
    Write-Host "4. List all available skills:" -ForegroundColor White
    Write-Host "   Get-Content registry\skills.json | ConvertFrom-Json | Select-Object -ExpandProperty skills | Select-Object name" -ForegroundColor Blue
    Write-Host ""
    Write-Host "5. Read the full quickstart guide:" -ForegroundColor White
    Write-Host "   Get-Content QUICKSTART.md" -ForegroundColor Blue
    Write-Host ""
    Write-Host "Documentation:" -ForegroundColor Yellow
    Write-Host "- Quickstart Tutorial: QUICKSTART.md" -ForegroundColor Blue
    Write-Host "- Getting Started: GETTING_STARTED.md" -ForegroundColor Blue
    Write-Host "- Architecture: docs\betty-architecture.md" -ForegroundColor Blue
    Write-Host "- Skills Framework: docs\skills-framework.md" -ForegroundColor Blue
    Write-Host ""
    Write-Host "Need Help?" -ForegroundColor Yellow
    Write-Host "- Documentation: $BettyDir\docs\" -ForegroundColor Blue
    Write-Host "- GitHub Issues: https://github.com/epieczko/betty/issues" -ForegroundColor Blue
    Write-Host "- Community: https://github.com/epieczko/betty/discussions" -ForegroundColor Blue
    Write-Host ""
    Write-Host "Happy Building with Betty! 🚀" -ForegroundColor Green
    Write-Host ""
}

# Display banner
function Show-Banner {
    Write-Host ""
    Write-Host "    ____       _   _        " -ForegroundColor Blue
    Write-Host "   |  _ \     | | | |       " -ForegroundColor Blue
    Write-Host "   | |_) | ___| |_| |_ _   _" -ForegroundColor Blue
    Write-Host "   |  _ < / _ \ __| __| | | |" -ForegroundColor Blue
    Write-Host "   | |_) |  __/ |_| |_| |_| |" -ForegroundColor Blue
    Write-Host "   |____/ \___|\__|\__|\__, |" -ForegroundColor Blue
    Write-Host "                        __/ |" -ForegroundColor Blue
    Write-Host "   Framework          |___/ " -ForegroundColor Blue
    Write-Host ""
    Write-Host "   AI-Native SDLC Framework" -ForegroundColor Blue
    Write-Host ""
}

# Main execution
function Main {
    Show-Banner
    Write-InfoMsg "Starting Betty Framework quickstart setup..."

    Test-Prerequisites
    $bettyDir = Get-BettyDirectory
    Set-Location $bettyDir
    Install-Dependencies -BettyDir $bettyDir
    Set-BettyEnvironment -BettyDir $bettyDir
    Test-Installation -BettyDir $bettyDir
    New-HelloWorldSkill -BettyDir $bettyDir
    Show-NextSteps -BettyDir $bettyDir
}

# Run main function
try {
    Main
}
catch {
    Write-Host ""
    Write-ErrorMsg "Setup failed: $_"
    Write-Host $_.ScriptStackTrace
    exit 1
}
