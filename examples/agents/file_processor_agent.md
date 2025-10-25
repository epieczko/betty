# Name: file.processor

# Purpose:
Processes files through various transformations including format conversion,
compression, encryption, and batch operations.

# Inputs:
- file-list
- transformation-config

# Outputs:
- processed-files
- processing-report

# Skills Needed:
- file.convert
- file.compress
- file.encrypt
- batch.processor

# Implementation Notes:
The agent should support:
1. Format conversion (JSON ↔ YAML ↔ XML ↔ CSV)
2. Compression (gzip, zip, tar.gz, bz2)
3. Encryption/decryption (AES-256)
4. Batch operations on multiple files
5. Validation before and after processing
6. Error handling with rollback capability

Processing modes:
- Sequential: Process files one by one
- Parallel: Process multiple files concurrently
- Pipeline: Chain multiple transformations

Output report should include:
- Files processed successfully
- Files that failed with error details
- Processing time and performance metrics
- Storage space saved (for compression)
- Transformation details for each file
