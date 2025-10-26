# Training Data Card: [Dataset Name]

**Version**: 1.0.0
**Date**: 2025-01-15
**Dataset Owner**: [Team/Individual]
**Dataset ID**: [unique-dataset-id]

---

## Dataset Overview

**Dataset Name**: [dataset-name]
**Version**: 1.2.0
**Purpose**: [Primary use case for this dataset]
**License**: [CC-BY-4.0 | Proprietary | Public Domain]

**Collection Period**:
- Start Date: 2023-01-01
- End Date: 2024-12-31
- Collection Method: [How data was collected]

---

## Dataset Composition

**Size Statistics**:
- Total Records: 1,000,000
- Total Features: 125
- Storage Size: 45.0 GB
- Format: [Parquet | CSV | JSON | TFRecord]

**Data Distribution**:

| Class/Category | Count | Percentage |
|----------------|-------|------------|
| Class A | 750,000 | 75.0% |
| Class B | 250,000 | 25.0% |

**Feature Types**:
- Numerical: 85 features
- Categorical: 30 features
- Text: 8 features
- Image: 2 features

**Missing Data**:
| Feature | Missing % | Handling Strategy |
|---------|-----------|-------------------|
| feature_1 | 2.5% | Mean imputation |
| feature_2 | 0.8% | Forward fill |
| feature_3 | 5.2% | Dropped records |

---

## Demographic Composition

**Geographic Distribution**:
| Region | Records | Percentage |
|--------|---------|------------|
| North America | 600,000 | 60.0% |
| Europe | 250,000 | 25.0% |
| Asia Pacific | 100,000 | 10.0% |
| Other | 50,000 | 5.0% |

**Demographic Breakdown** (if applicable):
| Attribute | Distribution |
|-----------|--------------|
| Gender | Female: 48%, Male: 49%, Non-binary: 2%, Unknown: 1% |
| Age | 18-25: 25%, 26-40: 45%, 41-60: 25%, 60+: 5% |
| Language | English: 70%, Spanish: 15%, French: 10%, Other: 5% |

---

## Data Collection

**Collection Method**: [Web scraping | User surveys | System logs | Third-party provider]

**Data Sources**:
1. [Source 1: Description, Date range]
2. [Source 2: Description, Date range]
3. [Source 3: Description, Date range]

**Sampling Strategy**:
- Method: [Random | Stratified | Systematic | Convenience]
- Sample Rate: [Percentage or absolute number]
- Inclusion Criteria: [Criteria for inclusion in dataset]
- Exclusion Criteria: [Criteria for exclusion]

**Known Biases**:
- [ ] Geographic bias: Over-representation of North American users
- [ ] Temporal bias: More data from Q4 than other quarters
- [ ] Selection bias: [Description of selection bias]
- [ ] Survivorship bias: [Description if applicable]

---

## Data Quality

**Quality Metrics**:
| Metric | Score | Status |
|--------|-------|--------|
| Completeness | 95.2% | Good |
| Accuracy | 92.5% | Good |
| Consistency | 88.0% | Acceptable |
| Timeliness | 97.0% | Good |
| Validity | 91.0% | Good |

**Data Validation**:
- Schema Validation: [Tool used, pass/fail rate]
- Range Checks: [Min/max validation results]
- Format Validation: [Data type consistency]
- Cross-field Validation: [Logical consistency checks]

**Outlier Detection**:
- Method: [IQR | Z-score | Isolation Forest]
- Outliers Detected: [Number and percentage]
- Treatment: [Cap | Remove | Keep | Flag]

**Duplicate Records**:
- Exact Duplicates: [Number found, action taken]
- Near Duplicates: [Similarity threshold, number found]
- Deduplication Method: [Method used]

---

## Data Processing

**Preprocessing Pipeline**:
1. **Raw Data Ingestion**
   - Source: [Data source location]
   - Validation: [Initial validation checks]

2. **Cleaning**
   - Remove nulls: [Strategy]
   - Handle missing values: [Strategy per feature]
   - Remove duplicates: [Dedup logic]

3. **Transformation**
   - Normalization: [StandardScaler | MinMaxScaler | None]
   - Encoding: [One-hot | Label | Target encoding]
   - Feature engineering: [Derived features created]

4. **Validation**
   - Schema check: [Expectations validated]
   - Quality gates: [Pass/fail criteria]

**Feature Engineering**:
- [Feature 1]: [Description of how it was created]
- [Feature 2]: [Description of how it was created]
- [Interaction Features]: [Description]

**Data Splits**:
| Split | Records | Percentage | Strategy |
|-------|---------|------------|----------|
| Training | 700,000 | 70% | Temporal |
| Validation | 150,000 | 15% | Random |
| Test | 150,000 | 15% | Temporal holdout |

**Split Criteria**:
- Method: [Temporal | Random | Stratified]
- Temporal Cutoff: [Date if temporal split]
- Random Seed: 42
- Stratification Variables: [If stratified]

---

## Privacy & Consent

**Personal Information**:
- Contains PII: [Yes | No]
- PII Types: [Email, Name, Address, IP Address, etc.]
- PII Treatment: [Anonymization, Pseudonymization, Hashing]

**Consent**:
- Consent Obtained: [Yes | No | N/A]
- Consent Type: [Explicit | Implicit | Legitimate Interest]
- Consent Mechanism: [How consent was collected]
- Right to Withdraw: [Yes | No]

**Privacy Measures**:
- Anonymization: [Method and effectiveness]
- De-identification: [K-anonymity level, if applicable]
- Differential Privacy: [Epsilon value, if applied]
- Secure Storage: [Encryption at rest, access controls]

**Compliance**:
- GDPR: [Compliant | Needs Review | N/A]
- CCPA: [Compliant | Needs Review | N/A]
- HIPAA: [Compliant | Needs Review | N/A]
- Special Categories (GDPR Article 9): [Yes | No]

**Data Retention**:
- Retention Period: [Duration]
- Deletion Procedures: [How data is deleted]
- Archive Policy: [Long-term storage approach]

---

## Ethical Considerations

**Sensitive Attributes**:
| Attribute | Included | Justification |
|-----------|----------|---------------|
| Race/Ethnicity | [Yes/No] | [Why included or excluded] |
| Gender | [Yes/No] | [Why included or excluded] |
| Age | [Yes/No] | [Why included or excluded] |
| Religion | [Yes/No] | [Why included or excluded] |

**Potential Harms**:
- [ ] **Representation Harm**: [Description of potential harm]
  - Mitigation: [How mitigated]
- [ ] **Allocation Harm**: [Description of potential harm]
  - Mitigation: [How mitigated]
- [ ] **Privacy Risk**: [Description of potential harm]
  - Mitigation: [How mitigated]

**Fairness Assessment**:
- Demographic Parity: [Analysis results]
- Representation Quality: [Quality across groups]
- Proxy Variables: [Identification of proxy variables]

**Ethics Review**:
- IRB Approval: [Yes | No | N/A]
- Ethics Committee Review: [Yes | No]
- Review Date: [YYYY-MM-DD]
- Outcome: [Approved | Conditional | Rejected]

---

## Intended Use

**Primary Use Cases**:
1. [Use case 1: Description]
2. [Use case 2: Description]
3. [Use case 3: Description]

**Out-of-Scope Uses**:
- [ ] **[Use case 1]**: [Why out of scope]
- [ ] **[Use case 2]**: [Why out of scope]
- [ ] **High-stakes decisions**: [e.g., Not validated for medical diagnosis]

**Target Population**:
- Geographic: [Regions where data is representative]
- Demographic: [Populations adequately represented]
- Temporal: [Time period of relevance]

---

## Known Limitations

**Data Limitations**:
- [ ] **Temporal Coverage**: Data from 2023-2024 may not reflect 2025+ patterns
- [ ] **Geographic Bias**: Over-representation of North American users
- [ ] **Under-represented Groups**: [List under-represented populations]
- [ ] **Class Imbalance**: 75%/25% split between classes

**Collection Limitations**:
- [ ] **Sampling Bias**: [Description of sampling limitations]
- [ ] **Measurement Error**: [Sources of measurement error]
- [ ] **Data Drift**: [Known temporal changes in distribution]

**Quality Limitations**:
- [ ] **Missing Data**: 2-5% missing values in key features
- [ ] **Label Noise**: [Estimated label error rate]
- [ ] **Annotation Quality**: [Inter-annotator agreement metrics]

---

## Annotation Process

**Annotation Method**: [Manual | Semi-automated | Fully automated]

**Annotators**:
- Number of Annotators: [N]
- Annotator Background: [Demographics, qualifications]
- Annotator Training: [Training provided]
- Compensation: [How annotators were compensated]

**Annotation Quality**:
| Metric | Value |
|--------|-------|
| Inter-annotator Agreement (Cohen's Kappa) | 0.85 |
| Krippendorff's Alpha | 0.82 |
| Fleiss' Kappa | 0.83 |
| Label Accuracy (on gold standard) | 92% |

**Annotation Guidelines**:
- Guidelines Document: [Link to annotation guidelines]
- Ambiguity Resolution: [How edge cases handled]
- Quality Control: [Validation process]

**Multiple Annotations**:
- Overlap: [Percentage of examples with multiple annotations]
- Aggregation Method: [Majority vote | Weighted average | Expert arbitration]

---

## Dataset Versioning

**Version History**:
| Version | Date | Changes | Backward Compatible |
|---------|------|---------|---------------------|
| 1.0.0 | 2024-01-15 | Initial release | N/A |
| 1.1.0 | 2024-06-01 | Added 100K records | Yes |
| 1.2.0 | 2025-01-15 | Rebalanced classes, fixed label noise | No |

**Version Control**:
- Storage: [DVC | Delta Lake | Git LFS | S3 versioning]
- Checksum: sha256:abc123...
- Lineage: [Parent dataset, transformations applied]

**Breaking Changes** (v1.1.0 → v1.2.0):
- [Change 1: Impact on existing models]
- [Change 2: Impact on existing models]

---

## Access & Distribution

**Access**:
- Location: s3://bucket/datasets/dataset-name-v1.2.0
- Access Control: [RBAC roles required]
- Request Process: [How to request access]

**Distribution**:
- Public: [Yes | No]
- Restricted: [Access criteria]
- Download: [URL or procedure]

**Citation**:
```
[Organization]. (2025). [Dataset Name] (Version 1.2.0) [Data set]. 
Available from https://example.com/datasets/dataset-name
```

**Terms of Use**:
- License: [CC-BY-4.0 | Proprietary | Other]
- Attribution Required: [Yes | No]
- Commercial Use: [Allowed | Prohibited | Restricted]
- Derivatives: [Allowed | Prohibited | Share-alike]

---

## Maintenance & Updates

**Update Frequency**: [Quarterly | Annually | As needed]

**Update Triggers**:
- [ ] Scheduled refresh (quarterly)
- [ ] New data available from sources
- [ ] Quality issues identified
- [ ] Distribution drift detected

**Deprecation Plan**:
- Deprecation Notice: [90 days advance notice]
- Replacement Dataset: [Link to successor dataset]
- End-of-Life Date: [YYYY-MM-DD]

**Contact**:
- Dataset Owner: [name@example.com]
- Support: [support-channel]
- Issues: [GitHub issues or Jira]

---

## Related Artifacts

**Model Cards**: [Links to models trained on this dataset]
**Data Lineage**: [Upstream data sources]
**Data Quality Reports**: [Quality assessment reports]

---

**Template Version**: 1.0
**Based on**: Datasheets for Datasets (Gebru et al.), Data Nutrition Labels, GDPR Article 30
