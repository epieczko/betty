# IaC Module Registry

## Document Information

**Purpose**: Catalog reusable Infrastructure-as-Code modules (Terraform, Pulumi, CloudFormation, Bicep) with versioning, documentation, compliance tracking, and usage examples to promote standardization and accelerate infrastructure provisioning.

**Format**: Markdown with module catalog and examples

**Target Audience**: Platform Engineers, Cloud Architects, DevOps Engineers, Infrastructure Teams

**Related Artifacts**:
- Terraform/Pulumi Code
- Cloud Provider Templates
- Environment Matrix
- Architecture Documentation

---

## Metadata

```yaml
version: "1.2.0"
created: "2024-01-05"
lastModified: "2024-01-22"
status: "Active"
documentOwner: "Platform Engineering Team"
classification: "Internal"
```

---

## 1. Module Registry Structure

### 1.1 Terraform Module Registry

**Repository Structure**:
```
terraform-modules/
├── README.md
├── modules/
│   ├── vpc/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   ├── outputs.tf
│   │   ├── README.md
│   │   ├── examples/
│   │   │   └── complete/
│   │   └── versions.tf
│   ├── eks-cluster/
│   ├── rds-postgres/
│   ├── s3-bucket/
│   └── cloudfront-distribution/
└── .github/
    └── workflows/
        └── terraform-ci.yml
```

---

## 2. Module Catalog

### 2.1 VPC Module

**Module**: `terraform-aws-vpc`
**Version**: `v3.2.0`
**Provider**: AWS
**Purpose**: Create production-ready VPC with public/private subnets, NAT gateways, and VPC endpoints

**File**: `modules/vpc/main.tf`

```hcl
# VPC Module
# Creates a production-ready VPC with multi-AZ support

variable "name" {
  description = "Name prefix for VPC resources"
  type        = string
}

variable "cidr" {
  description = "CIDR block for VPC"
  type        = string
  default     = "10.0.0.0/16"
}

variable "azs" {
  description = "Availability zones"
  type        = list(string)
  default     = ["us-east-1a", "us-east-1b", "us-east-1c"]
}

variable "private_subnets" {
  description = "Private subnet CIDR blocks"
  type        = list(string)
  default     = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
}

variable "public_subnets" {
  description = "Public subnet CIDR blocks"
  type        = list(string)
  default     = ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"]
}

variable "enable_nat_gateway" {
  description = "Enable NAT gateway for private subnets"
  type        = bool
  default     = true
}

variable "single_nat_gateway" {
  description = "Use single NAT gateway for cost savings"
  type        = bool
  default     = false
}

variable "enable_dns_hostnames" {
  description = "Enable DNS hostnames in VPC"
  type        = bool
  default     = true
}

variable "tags" {
  description = "Additional tags for resources"
  type        = map(string)
  default     = {}
}

# VPC
resource "aws_vpc" "this" {
  cidr_block           = var.cidr
  enable_dns_hostnames = var.enable_dns_hostnames
  enable_dns_support   = true

  tags = merge(
    var.tags,
    {
      Name = var.name
    }
  )
}

# Internet Gateway
resource "aws_internet_gateway" "this" {
  vpc_id = aws_vpc.this.id

  tags = merge(
    var.tags,
    {
      Name = "${var.name}-igw"
    }
  )
}

# Public Subnets
resource "aws_subnet" "public" {
  count                   = length(var.public_subnets)
  vpc_id                  = aws_vpc.this.id
  cidr_block              = var.public_subnets[count.index]
  availability_zone       = var.azs[count.index]
  map_public_ip_on_launch = true

  tags = merge(
    var.tags,
    {
      Name = "${var.name}-public-${var.azs[count.index]}"
      Tier = "Public"
    }
  )
}

# Private Subnets
resource "aws_subnet" "private" {
  count             = length(var.private_subnets)
  vpc_id            = aws_vpc.this.id
  cidr_block        = var.private_subnets[count.index]
  availability_zone = var.azs[count.index]

  tags = merge(
    var.tags,
    {
      Name = "${var.name}-private-${var.azs[count.index]}"
      Tier = "Private"
    }
  )
}

# NAT Gateways
resource "aws_eip" "nat" {
  count  = var.enable_nat_gateway ? (var.single_nat_gateway ? 1 : length(var.azs)) : 0
  domain = "vpc"

  tags = merge(
    var.tags,
    {
      Name = "${var.name}-nat-${count.index + 1}"
    }
  )
}

resource "aws_nat_gateway" "this" {
  count         = var.enable_nat_gateway ? (var.single_nat_gateway ? 1 : length(var.azs)) : 0
  allocation_id = aws_eip.nat[count.index].id
  subnet_id     = aws_subnet.public[count.index].id

  tags = merge(
    var.tags,
    {
      Name = "${var.name}-nat-${count.index + 1}"
    }
  )

  depends_on = [aws_internet_gateway.this]
}

# Output
output "vpc_id" {
  description = "VPC ID"
  value       = aws_vpc.this.id
}

output "private_subnet_ids" {
  description = "Private subnet IDs"
  value       = aws_subnet.private[*].id
}

output "public_subnet_ids" {
  description = "Public subnet IDs"
  value       = aws_subnet.public[*].id
}
```

**Usage Example**:

```hcl
module "vpc" {
  source  = "git::https://github.com/company/terraform-modules.git//modules/vpc?ref=v3.2.0"

  name               = "production-vpc"
  cidr               = "10.0.0.0/16"
  azs                = ["us-east-1a", "us-east-1b", "us-east-1c"]
  private_subnets    = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  public_subnets     = ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"]
  enable_nat_gateway = true
  single_nat_gateway = false

  tags = {
    Environment = "production"
    ManagedBy   = "terraform"
    CostCenter  = "infrastructure"
  }
}
```

---

### 2.2 EKS Cluster Module

**Module**: `terraform-aws-eks`
**Version**: `v2.5.0`
**Provider**: AWS
**Purpose**: Deploy production-grade EKS cluster with managed node groups

**File**: `modules/eks-cluster/main.tf`

```hcl
variable "cluster_name" {
  description = "EKS cluster name"
  type        = string
}

variable "cluster_version" {
  description = "Kubernetes version"
  type        = string
  default     = "1.28"
}

variable "vpc_id" {
  description = "VPC ID"
  type        = string
}

variable "subnet_ids" {
  description = "Subnet IDs for EKS cluster"
  type        = list(string)
}

variable "node_groups" {
  description = "EKS managed node group configurations"
  type = map(object({
    instance_types = list(string)
    capacity_type  = string
    min_size       = number
    max_size       = number
    desired_size   = number
    disk_size      = number
    labels         = map(string)
    taints         = list(object({
      key    = string
      value  = string
      effect = string
    }))
  }))
}

# EKS Cluster IAM Role
resource "aws_iam_role" "cluster" {
  name = "${var.cluster_name}-cluster-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = {
        Service = "eks.amazonaws.com"
      }
    }]
  })
}

resource "aws_iam_role_policy_attachment" "cluster_policy" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKSClusterPolicy"
  role       = aws_iam_role.cluster.name
}

# EKS Cluster
resource "aws_eks_cluster" "this" {
  name     = var.cluster_name
  role_arn = aws_iam_role.cluster.arn
  version  = var.cluster_version

  vpc_config {
    subnet_ids              = var.subnet_ids
    endpoint_private_access = true
    endpoint_public_access  = true
    public_access_cidrs     = ["0.0.0.0/0"]
  }

  enabled_cluster_log_types = ["api", "audit", "authenticator", "controllerManager", "scheduler"]

  depends_on = [aws_iam_role_policy_attachment.cluster_policy]
}

# Node Group IAM Role
resource "aws_iam_role" "node_group" {
  name = "${var.cluster_name}-node-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = {
        Service = "ec2.amazonaws.com"
      }
    }]
  })
}

resource "aws_iam_role_policy_attachment" "node_group_policies" {
  for_each = toset([
    "arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy",
    "arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy",
    "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly",
  ])

  policy_arn = each.value
  role       = aws_iam_role.node_group.name
}

# Node Groups
resource "aws_eks_node_group" "this" {
  for_each = var.node_groups

  cluster_name    = aws_eks_cluster.this.name
  node_group_name = each.key
  node_role_arn   = aws_iam_role.node_group.arn
  subnet_ids      = var.subnet_ids

  instance_types = each.value.instance_types
  capacity_type  = each.value.capacity_type
  disk_size      = each.value.disk_size

  scaling_config {
    desired_size = each.value.desired_size
    max_size     = each.value.max_size
    min_size     = each.value.min_size
  }

  labels = each.value.labels

  dynamic "taint" {
    for_each = each.value.taints
    content {
      key    = taint.value.key
      value  = taint.value.value
      effect = taint.value.effect
    }
  }

  depends_on = [
    aws_iam_role_policy_attachment.node_group_policies
  ]
}

output "cluster_id" {
  value = aws_eks_cluster.this.id
}

output "cluster_endpoint" {
  value = aws_eks_cluster.this.endpoint
}

output "cluster_ca_certificate" {
  value     = aws_eks_cluster.this.certificate_authority[0].data
  sensitive = true
}
```

**Usage Example**:

```hcl
module "eks" {
  source = "git::https://github.com/company/terraform-modules.git//modules/eks-cluster?ref=v2.5.0"

  cluster_name    = "production-eks"
  cluster_version = "1.28"
  vpc_id          = module.vpc.vpc_id
  subnet_ids      = module.vpc.private_subnet_ids

  node_groups = {
    general = {
      instance_types = ["m5.2xlarge"]
      capacity_type  = "ON_DEMAND"
      min_size       = 10
      max_size       = 50
      desired_size   = 15
      disk_size      = 200
      labels         = { workload = "general" }
      taints         = []
    }
    gpu = {
      instance_types = ["p3.2xlarge"]
      capacity_type  = "ON_DEMAND"
      min_size       = 0
      max_size       = 5
      desired_size   = 0
      disk_size      = 300
      labels         = { workload = "ml-inference" }
      taints = [{
        key    = "nvidia.com/gpu"
        value  = "true"
        effect = "NoSchedule"
      }]
    }
  }
}
```

---

## 3. Module Versioning & Publishing

### 3.1 Semantic Versioning

```
v{major}.{minor}.{patch}

v1.0.0 - Initial release
v1.1.0 - New features (backward compatible)
v1.1.1 - Bug fixes
v2.0.0 - Breaking changes
```

### 3.2 Git Tags

```bash
# Tag new version
git tag -a v1.2.0 -m "Add support for VPC endpoints"
git push origin v1.2.0

# Use specific version
module "vpc" {
  source = "git::https://github.com/company/terraform-modules.git//modules/vpc?ref=v1.2.0"
}
```

### 3.3 Module Registry (Terraform Cloud/Enterprise)

```hcl
module "vpc" {
  source  = "app.terraform.io/company/vpc/aws"
  version = "~> 1.2"  # Any 1.x version >= 1.2.0
}
```

---

## 4. Module Documentation

### 4.1 README Template

```markdown
# Module Name

## Description
Brief description of what this module does.

## Usage
Basic example of how to use the module.

## Inputs
| Name | Description | Type | Default | Required |
|------|-------------|------|---------|----------|
| name | Resource name | string | - | yes |

## Outputs
| Name | Description |
|------|-------------|
| id | Resource ID |

## Examples
Link to examples directory.

## Requirements
| Name | Version |
|------|---------|
| terraform | >= 1.5 |
| aws | >= 5.0 |

## Changelog
See CHANGELOG.md
```

---

## 5. Module Testing

### 5.1 Terraform Test

```hcl
# tests/vpc_test.tftest.hcl
run "setup" {
  module {
    source = "./tests/setup"
  }
}

run "create_vpc" {
  command = apply

  variables {
    name    = "test-vpc"
    cidr    = "10.0.0.0/16"
  }

  assert {
    condition     = aws_vpc.this.cidr_block == "10.0.0.0/16"
    error_message = "VPC CIDR mismatch"
  }
}

run "destroy_vpc" {
  command = destroy
}
```

### 5.2 Terratest (Go)

```go
package test

import (
    "testing"
    "github.com/gruntwork-io/terratest/modules/terraform"
    "github.com/stretchr/testify/assert"
)

func TestVPCModule(t *testing.T) {
    terraformOptions := &terraform.Options{
        TerraformDir: "../modules/vpc",
        Vars: map[string]interface{}{
            "name": "test-vpc",
            "cidr": "10.0.0.0/16",
        },
    }

    defer terraform.Destroy(t, terraformOptions)
    terraform.InitAndApply(t, terraformOptions)

    vpcID := terraform.Output(t, terraformOptions, "vpc_id")
    assert.NotEmpty(t, vpcID)
}
```

---

## 6. Module Registry Catalog

| Module | Version | Provider | Status | Compliance |
|--------|---------|----------|--------|------------|
| vpc | v3.2.0 | AWS | Active | PCI-DSS, SOC2 |
| eks-cluster | v2.5.0 | AWS | Active | PCI-DSS, SOC2 |
| rds-postgres | v1.8.0 | AWS | Active | PCI-DSS, HIPAA |
| s3-bucket | v2.1.0 | AWS | Active | All |
| cloudfront-distribution | v1.5.0 | AWS | Active | All |
| aks-cluster | v1.3.0 | Azure | Active | SOC2 |
| gke-cluster | v1.2.0 | GCP | Beta | SOC2 |

---

## 7. Change History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.2.0 | 2024-01-22 | Platform Team | Added EKS module, testing examples |
| 1.1.0 | 2024-01-10 | Infrastructure Team | Added VPC module catalog |
| 1.0.0 | 2024-01-05 | DevOps Team | Initial module registry |

---

## 8. Related Documentation

- [Terraform Best Practices](./terraform-best-practices.md)
- [Infrastructure as Code Guide](./iac-guide.md)
- [Environment Matrix](./environment-matrix.md)
- [Module Development Guide](./module-development.md)
